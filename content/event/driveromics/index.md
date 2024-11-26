---
title: 新 Preprint 發表於 biorxiv
event: 文章連結
event_url: 'https://www.biorxiv.org/content/10.1101/2024.07.21.604474v1'

#location: 線上
#address:
#  street: 450 Serra Mall
 # city: Stanford
  #region: CA
  #postcode: '94305'
  #country: Taiwan

summary: DriverOmicsNet-An Integrated Graph Convolutional Network for Multi-Omics Exploration of Cancer Driver Genes
#abstract: 
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2024-07-21'
#date_end: '2024-02-07T15:00:00Z'
#all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2024-07-21'

authors: ['戴揚紘', '沈伯鍵']
tags: []

# Is this a featured talk? (true/false)
featured: false

#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

video:
  url: ''
  caption: 'Video credit: [**YouTube**](https://www.youtube.com/watch?v=bVHMlVoop68)'
  focal_point: Center

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides:

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
#projects:

#Slides can be added in a few ways:

#- **Create** slides using Wowchemy's [_Slides_](https://docs.hugoblox.com/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file
#- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
#- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://docs.hugoblox.com/writing-markdown-latex/).

#Further event details, including page elements such as image galleries, can be added to the body of this page.
---
# Title
DriverOmicsNet-An Integrated Graph Convolutional Network for Multi-Omics Exploration of Cancer Driver Genes
# Abstract
Background: Cancer is a complex and heterogeneous group of diseases driven by genetic mutations and molecular changes. Identifying and characterizing cancer driver genes (CDgs) is crucial for understanding cancer biology and guiding precision oncology. Integrating multi-omics data can reveal the intricate molecular interactions underlying cancer progression and treatment responses.

Methods: We developed a graph convolutional network (GCN) framework, DriverOmicsNet, that integrates multi-omics data using STRING protein-protein interaction (PPI) networks and correlation-based weighted correlation network analysis (WGCNA). We applied this framework to 15 cancer types, analyzing 5555 tumor samples to predict cancer-related features such as homologous recombination deficiency (HRD), cancer stemness, immune clusters, tumor stage, and survival outcomes.

Findings: DriverOmicsNet demonstrated superior predictive accuracy and model performance metrics across all target labels when compared with GCN models based on STRING network alone. Gene expression emerged as the most significant feature, reflecting the dynamic and functional state of cancer cells. The combined use of STRING PPI and WGCNA networks enhanced the identification of key driver genes and their interactions.

Interpretation: Our study highlights the effectiveness of using GCNs to integrate multi-omics data for precision oncology. The integration of STRING PPI and WGCNA networks provides a comprehensive framework that improves predictive power and facilitates the understanding of cancer biology, paving the way for more tailored treatments.


