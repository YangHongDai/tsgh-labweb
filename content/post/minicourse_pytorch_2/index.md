---
title: 迷你課程:PyTorch-2-工作流程基礎
date: 2025-09-12
authors: ["戴揚紘", ""]
commentable: true
categories: [PyTorch迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
參考了這個教學[網站](https://www.learnpytorch.io/00_pytorch_fundamentals/#introduction-to-tensors)，以及我自己在Udemy購買的線上課程

## 我們要做什麼？
- 建立一條已知參數的直線資料（線性回歸）。
- 用 PyTorch 建立模型、定義損失與最佳化器。
- 進行訓練（fitting）、推論（inference）與評估。
- 存檔與讀檔。
- 最後把流程整合起來（含裝置無關 GPU/CPU 寫法）。
- 提供練習題檢核你的理解。

## 環境載入
```python
import torch
from torch import nn
import matplotlib.pyplot as plt
torch.__version__  # e.g. '1.12.1+cu113'
```

## 資料（準備與載入）
#### 概念
1. 機器學習的資料可以是表格、影像、聲音、文字……
2. 這些資料必須先轉換成`numerical input`或`numerical representation`
3. 本次課用直線資料示範。
先建立線性關係 y = weight * X + bias 作為真實資料，再讓模型去學習這個關係。

#### 已知參數
```python
weight = 0.7
bias = 0.3
```

#### 建立自變數與標籤
```python
start, end, step = 0, 1, 0.02
X = torch.arange(start, end, step).unsqueeze(dim=1)  # 形狀 (N,1) 因為dim=1 是在第二個dim位置 
#記得針對matrix or tensor 變數為大寫
#向量或純量為小寫
y = weight * X + bias

X[:10], y[:10]
```

## 訓練/測試切分
模型訓練中的重要的一步就是將數據分成`訓練集`及`驗證集`與`測試集`。
- `訓練集 (類似學習教材)`: 模型從這邊學習pattern，約需要`60-80%`，`必要`。
- `驗證集 (類似模擬考)`: 模型從這邊微調模型，約需要`10-20%`，`不一定需要`。
- `測試集 (類似正式考試)`: 測試模型是否可以用在一般情境，約需要`10-20%`，`必要`。
```python
##也可以用scikit learn 的train_test_split 
train_split = int(0.8 * len(X))  # 80/20
X_train, y_train = X[:train_split], y[:train_split]
X_test,  y_test  = X[train_split:], y[train_split:]
```
#### 視覺化（建議）
可以用來探索輸入進模型的數據，通常建議用視覺化來感受一下數據的分佈。
```python
def plot_predictions(train_data=X_train,              
                     train_labels=y_train,
                     test_data=X_test,  test_labels=y_test,
                     predictions=None):
    plt.figure(figsize=(10, 7))
    ##Plot training data in blue
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
    #Plot testing data in green
    plt.scatter(test_data,  test_labels,  c="g", s=4, label="Testing data")

    if predictions is not None:
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    plt.legend(prop={"size": 14})

plot_predictions()
```
[!Fig1]('Fig1.png 圖一 訓練集與測試集散布圖')

#### 建立模型
方式 A：用 nn.Parameter 手刻線性回歸
```python
class LinearRegressionModel(nn.Module):
      #幾乎所有PyTorch所有程式都繼承nn.Module
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, dtype=torch.float), requires_grad=True)
        self.bias    = nn.Parameter(torch.randn(1, dtype=torch.float), requires_grad=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias

torch.manual_seed(42)
model_0 = LinearRegressionModel()
list(model_0.parameters())      # 檢查參數
model_0.state_dict()            # 或者看 state_dict
```
> 裡面的`nn.Parameter()`是建立PyTorch模型參數的特有方法，要讓某個張量被視為`可學習權重`：用 nn.Parameter 放到 nn.Module 的屬性上。所以只要是 model.parameters() 要看得到、optimizer 要更新、state_dict 要保存 的，請用 nn.Parameter。

這個模型做了什麼？
1. 從建立`random value` (weight與bias)開始。
2. 檢視Training data並`修正random value`到更好的(`更接近的`)的數值 (就是我們用來建立數據所使用的weight與bias)
3. 如何達到? a. 使用`gradient descent`; b. 使用`backpropagation`


#### 推論模式與預測（尚未訓練）
```python
with torch.inference_mode():
    y_preds = model_0(X_test)
plot_predictions(predictions=y_preds)
```
初次預測會很差，因為參數是亂數，尚未學習。

#### 訓練模型（建立損失與最佳化器 + 訓練/測試迴圈）
- 損失與最佳化器
- 回歸常用：MAE（L1Loss）、MSE（MSELoss）
- 最佳化器常用：SGD、Adam
```python
loss_fn  = nn.L1Loss()  # MAE
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01)
訓練/測試迴圈（100 個 epoch）
torch.manual_seed(42)
epochs = 100
train_loss_values, test_loss_values, epoch_count = [], [], []

for epoch in range(epochs):
    # ---- Train ----
    model_0.train()
    y_pred = model_0(X_train)
    loss = loss_fn(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # ---- Test ----
    model_0.eval()
    with torch.inference_mode():
        test_pred = model_0(X_test)
        test_loss = loss_fn(test_pred, y_test.type(torch.float))

    if epoch % 10 == 0:
        epoch_count.append(epoch)
        train_loss_values.append(loss.detach().numpy())
        test_loss_values.append(test_loss.detach().numpy())
        print(f"Epoch: {epoch} | MAE Train Loss: {loss} | MAE Test Loss: {test_loss}")
```
#### 繪製學習曲線
```python
plt.plot(epoch_count, train_loss_values, label="Train loss")
plt.plot(epoch_count, test_loss_values,  label="Test loss")
plt.title("Training and test loss curves")
plt.ylabel("Loss"); plt.xlabel("Epochs"); plt.legend()
查看學到的參數
print("Learned params:", model_0.state_dict())
print(f"Ground truth -> weight={weight}, bias={bias}")
```
#### 用訓練後模型做推論（Inference）
三步驟：
```python
model.eval()
進入 with torch.inference_mode():
模型與資料要在同一裝置上（CPU/GPU）
model_0.eval()
with torch.inference_mode():
    y_preds = model_0(X_test)
plot_predictions(predictions=y_preds)
```
#### 模型儲存與載入
儲存 state_dict()（建議做法）
```python
from pathlib import Path
MODEL_PATH = Path("models"); MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_NAME = "01_pytorch_workflow_model_0.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

torch.save(obj=model_0.state_dict(), f=MODEL_SAVE_PATH)
載入到同型模型
loaded_model_0 = LinearRegressionModel()
loaded_model_0.load_state_dict(torch.load(MODEL_SAVE_PATH))

loaded_model_0.eval()
with torch.inference_mode():
    loaded_preds = loaded_model_0(X_test)

# 驗證與原預測一致
(loaded_preds == y_preds).all()
只存 state_dict() 的好處：與目錄/類別不強綁定，跨專案更穩定。
6. 全部串起來（裝置無關、用 nn.Linear 版本）
設定裝置
import torch
from torch import nn
import matplotlib.pyplot as plt

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
資料
weight, bias = 0.7, 0.3
start, end, step = 0, 1, 0.02
X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias

train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test,  y_test  = X[train_split:], y[train_split:]

plot_predictions(X_train, y_train, X_test, y_test)
模型（nn.Linear）
class LinearRegressionModelV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear_layer(x)

torch.manual_seed(42)
model_1 = LinearRegressionModelV2().to(device)
next(model_1.parameters()).device  # 確認裝置
訓練
loss_fn  = nn.L1Loss()
optimizer = torch.optim.SGD(model_1.parameters(), lr=0.01)

torch.manual_seed(42)
epochs = 1000

# 資料丟到裝置
X_train = X_train.to(device); y_train = y_train.to(device)
X_test  = X_test.to(device);   y_test  = y_test.to(device)

for epoch in range(epochs):
    model_1.train()
    y_pred = model_1(X_train)
    loss = loss_fn(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    model_1.eval()
    with torch.inference_mode():
        test_pred = model_1(X_test)
        test_loss = loss_fn(test_pred, y_test)

    if epoch % 100 == 0:
        print(f"Epoch: {epoch} | Train loss: {loss} | Test loss: {test_loss}")
```

#### 參數檢視
```python
from pprint import pprint
print("Learned params:")
pprint(model_1.state_dict())
print(f"Ground truth -> weight={weight}, bias={bias}")
```

#### 推論與視覺化
```python
model_1.eval()
with torch.inference_mode():
    y_preds = model_1(X_test)

plot_predictions(predictions=y_preds.cpu())  # 繪圖前放回 CPU
存檔與載入（再次確認）
from pathlib import Path
MODEL_PATH = Path("models"); MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_NAME = "01_pytorch_workflow_model_1.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

torch.save(model_1.state_dict(), MODEL_SAVE_PATH)

loaded_model_1 = LinearRegressionModelV2()
loaded_model_1.load_state_dict(torch.load(MODEL_SAVE_PATH))
loaded_model_1.to(device)

loaded_model_1.eval()
with torch.inference_mode():
    loaded_model_1_preds = loaded_model_1(X_test)

(loaded_model_1_preds == y_preds).all()
```

#### 模組/名詞速查
- torch.nn：神經網路積木（層、損失函數…）。
- nn.Module：所有模型的基底類別；需實作 forward()。
- nn.Parameter：可學習參數（requires_grad=True）。
- torch.optim：最佳化器（SGD、Adam…）。
- torch.inference_mode()：推論時關閉梯度等，加速前向傳播。
- model.train() / model.eval()：切換訓練/評估模式（影響 Dropout/BN 等）。

---
## 練習題（每一步都要做，建議使用裝置無關寫法）
資料建立
用 weight=0.3、bias=0.9 產生至少 100 筆直線資料。
80%/20% 切分訓練/測試。
視覺化訓練/測試點。
建模
以 nn.Module 子類別建立模型：用 兩個 nn.Parameter（weight、bias，requires_grad=True）或改用 nn.Linear(1,1)。
在 forward() 實作線性回歸公式。
建立實例並檢查 state_dict()。
損失與最佳化器
用 nn.L1Loss() 與 torch.optim.SGD(model.parameters(), lr=0.01)。
訓練
訓練 300 個 epoch。
每 20 epoch 在測試集評估一次並印出訓練/測試損失。
推論與視覺化
用訓練後模型在測試集產生預測，並與原始資料一起畫圖。
若資料在 GPU，繪圖前 .cpu()。
存檔與讀檔
把模型的 state_dict() 存到檔案。
以新實例讀回 state_dict()，在測試集做預測，確認與原模型預測逐元素相等。
