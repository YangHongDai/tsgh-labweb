---
title: 新文章發表於Journal of Translational Medicine

event: 文章連結
event_url: 'https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-023-03931-z'

#location: 線上
#address:
#  street: 450 Serra Mall
 # city: Stanford
  #region: CA
  #postcode: '94305'
  #country: Taiwan

summary: Incorporating knowledge of disease-defining hub genes and regulatory network into a machine learning-based model for predicting treatment response in lupus nephritis after the first renal flare
abstract: ''

# Talk start and end times.#
#   End time can optionally be hidden by prefixing the line with `#`.
#date: '2024-02-07'
#date_end: '2024-02-07'
#all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2023-02-03'

authors: ['戴揚紘','李定頡']
tags: []

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

video:
  url: ''
  caption: 'Video credit: [**YouTube**](https://www.youtube.com/watch?v=bVHMlVoop68)'
  focal_point: Center

url_code: ''
url_pdf: ''
#url_slides: '/slides/slide.pdf'
url_video: 'https://www.youtube.com/watch?v=bVHMlVoop68'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides:

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:

#Slides can be added in a few ways:

#- **Create** slides using Wowchemy's [_Slides_](https://docs.hugoblox.com/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file
#- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
#- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://docs.hugoblox.com/writing-markdown-latex/).

#Further event details, including page elements such as image galleries, can be added to the body of this page.
---
# Title
Incorporating knowledge of disease-defining hub genes and regulatory network into a machine learning-based model for predicting treatment response in lupus nephritis after the first renal flare
# Abstract
Background:Identifying candidates responsive to treatment is important in lupus nephritis (LN) at the renal flare (RF) because an effective treatment can lower the risk of progression to end-stage kidney disease. However, machine learning (ML)-based models that address this issue are lacking.

Methods:Transcriptomic profiles based on DNA microarray data were extracted from the GSE32591 and GSE112943 datasets. Comprehensive bioinformatics analyses were performed to identify disease-defining genes (DDGs). Peripheral blood samples (GSE81622, GSE99967, and GSE72326) were used to evaluate the effect of DDGs. Single-sample gene set enrichment analysis (ssGSEA) scores of the DDGs were calculated and correlated with specific immunology genes listed in the nCounter panel. GSE60681 and GSE69438 were used to examine the ability of the DDGs to discriminate LN from other renal diseases. K-means clustering was used to obtain the separate gene sets. The clustering results were extended to data derived using the nCounter technique. The least absolute shrinkage and selection operator (LASSO) algorithm was used to identify genes with high predictive value for treatment response after the first RF in each cluster. LASSO models with tenfold validation were built in GSE200306 and assessed by receiver operating characteristic (ROC) analysis with area under curve (AUC). The models were validated by using an independent dataset (GSE113342).

Results:Forty-five hub genes specific to LN were identified. Eight optimal disease-defining clusters (DDCs) were identified in this study. Th1 and Th2 cell differentiation pathway was significantly enriched in DDC-6. LCK in DDC-6, whose expression positively correlated with various subsets of T cell infiltrations, was found to be differentially expressed between responders and non-responders and was ranked high in regulatory network analysis. Based on DDC-6, the prediction model had the best performance (AUC: 0.75; 95% confidence interval: 0.44–1 in the testing set) and high precision (0.83), recall (0.71), and F1 score (0.77) in the validation dataset.

Conclusions:Our study demonstrates that incorporating knowledge of biological phenotypes into the ML model is feasible for evaluating treatment response after the first RF in LN. This knowledge-based incorporation improves the model's transparency and performance. In addition, LCK may serve as a biomarker for T-cell infiltration and a therapeutic target in LN.