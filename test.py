import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import statsmodels.api as sm
from statsmodels.discrete.count_model import ZeroInflatedPoisson, ZeroInflatedNegativeBinomialP
from scipy.stats import chisquare

# Configuration

np.random.seed(42)

# 1. Enhanced Data Simulation with Clear Zero-Inflation and Overdispersion ----------
def simulate_healthcare_data(n_samples=1000):
    """Generate synthetic data with strong zero-inflation and overdispersion"""
    # Patient characteristics
    age = np.random.normal(loc=50, scale=15, size=n_samples).clip(18, 90)
    income = np.random.lognormal(mean=3, sigma=0.5, size=n_samples)
    chronic_disease = np.random.binomial(1, p=0.3, size=n_samples)
    
    # Count process parameters (create overdispersion)
    true_lambda = np.exp(0.03 * age + 0.8 * chronic_disease - 0.02 * income - 2)
    dispersion = 0.5  # Controls overdispersion

    # Zero-inflation process (strong signal)
    zi_probs = logistic(-0.1 * age + 0.2 * income - 2)
    is_zero = np.random.binomial(1, zi_probs)

    # Corrected Negative Binomial counts
    n = 1 / dispersion  # Overdispersion parameter
    p = 1 / (1 + true_lambda * dispersion)  # Success probability
    visits = np.random.negative_binomial(n=n, p=p, size=n_samples)

    # Apply zero-inflation
    visits = np.where(is_zero, 0, visits)

    return pd.DataFrame({
        'Age': age,
        'Income': income,
        'Chronic_Disease': chronic_disease,
        'Visits': visits
    })


def logistic(x):
    return 1 / (1 + np.exp(-x))

# 2. Model Fitting with Convergence Assurance -------------------------------------
def fit_model(model_class, y, X, model_name):
    """Fit models with convergence safeguards"""
    X = sm.add_constant(X)
    
    # Custom starting parameters
    if model_name == 'ZIP':
        start_params = np.concatenate([
            [0.5, -0.5, 0.5, -0.5],  # Count model params
            [0.5]                     # Zero-inflation params
        ])
    elif model_name == 'ZINB':
        start_params = np.concatenate([
            [0.5, -0.5, 0.5, -0.5],  # Count model params
            [0.5],                   # Zero-inflation params
            [0.5]                     # Dispersion param
        ])
    else:
        start_params = None
    
    model = model_class(y, X)
    return model.fit(
        method='lbfgs',
        start_params=start_params,
        maxiter=1000,
        disp=0
    )

# 3. Enhanced Model Comparison ----------------------------------------------------
def compare_models(models, X_train, X_test, y_train, y_test):
    """Comprehensive model comparison with statistical tests"""
    results = []
    
    for name, model_class in models.items():
        # Fit model with convergence handling
        try:
            fitted = fit_model(model_class, y_train, X_train, name)
        except Exception as e:
            print(f"Error fitting {name}: {str(e)}")
            continue
        
        # Training fit metrics
        train_metrics = {
            'Log-Likelihood': fitted.llf,
            'AIC': fitted.aic,
            'BIC': fitted.bic
        }
        
        # Test predictions
        X_test_sm = sm.add_constant(X_test)
        pred = fitted.predict(X_test_sm)
        
        # Prediction metrics
        test_metrics = {
            'MAE': mean_absolute_error(y_test, pred),
            'MSE': mean_squared_error(y_test, pred),
            'RMSE': np.sqrt(mean_squared_error(y_test, pred))
        }
        
        # Overdispersion test (for Poisson models)
        if name == 'Poisson':
            chi2, p = chisquare(freq=y_test, f_exp=pred)
            train_metrics['Overdispersion_p'] = p
        
        results.append({
            'Model': name,
            **train_metrics,
            **test_metrics,
            'Params': len(fitted.params),
            'Converged': 'Yes' if fitted.mle_retvals['converged'] else 'No'
        })
        
        # Diagnostic plots
        plot_model_diagnostics(fitted, y_test, X_test_sm, name)
    
    return pd.DataFrame(results)

def plot_model_diagnostics(model, y_true, X, name):
    """Generate diagnostic visualizations"""
    pred = model.predict(X)
    residuals = y_true - pred
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    
    # Zero-inflation comparison
    zero_prop = pd.DataFrame({
        'Actual': (y_true == 0).astype(int),
        'Predicted': (pred < 0.5).astype(int)
    }).mean()
    zero_prop.plot(kind='bar', ax=ax[0], title='Zero Proportion Comparison')
    
    # Residual distribution
    sns.histplot(residuals, kde=True, ax=ax[1], bins=30)
    ax[1].set_title('Residual Distribution')
    
    plt.suptitle(f'{name} Diagnostics')
    plt.tight_layout()
    plt.show()

# 4. Execution Pipeline -----------------------------------------------------------
# Generate enhanced data
df = simulate_healthcare_data(1000)
X = df[['Age', 'Income', 'Chronic_Disease']]
y = df['Visits']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    'Poisson': sm.Poisson,
    'ZIP': ZeroInflatedPoisson,
    'ZINB': ZeroInflatedNegativeBinomialP
}

# Compare models
results_df = compare_models(models, X_train, X_test, y_train, y_test)
print("\n📊 Enhanced Model Comparison:")
print(results_df.sort_values('AIC'))

# 5. Statistical Validation of Zero-Inflation --------------------------------------
def vuong_test(poisson_model, zip_model):
    """Perform Vuong test for model comparison"""
    llf_poi = poisson_model.llf
    llf_zip = zip_model.llf
    n = len(poisson_model.model.endog)
    
    # Calculate test statistic
    m = llf_zip - llf_poi
    v = np.var(m)
    z = np.sqrt(n) * (np.mean(m)/np.sqrt(v))
    
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z)))
    return z, p_value

# Perform formal tests
poisson = fit_model(sm.Poisson, y_train, X_train, 'Poisson')
zip = fit_model(ZeroInflatedPoisson, y_train, X_train, 'ZIP')
z_stat, p_value = vuong_test(poisson, zip)

print(f"\n🔍 Vuong Test (ZIP vs Poisson): Z = {z_stat:.2f}, p = {p_value:.4f}")

# 6. Final Recommendations --------------------------------------------------------
print("\n💡 Enhanced Recommendations:")
print("1. Use ZINB when both excess zeros and overdispersion are present")
print("2. Validate zero-inflation with Vuong test before choosing ZIP")
print("3. Always check convergence status and residual diagnostics")
print("4. Consider feature engineering for zero-inflation components")