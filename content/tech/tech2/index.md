---
title: Data Efficient and Weakly Supervised Computational Pathology on Whole Slide Images
date: 2024-12-12
authors: ["戴揚紘", ""]
commentable: true
categories: [數位病理]
tags: [Digital pathology]
isCJKLanguage: true
draft: false
url_code: 'https://github.com/mahmoodlab/CLAM'
url_source: 'https://arxiv.org/abs/2004.09666'
---
<!--more-->
# Abstract
The rapidly emerging field of computational pathology has the potential to enable objective diagnosis, therapeutic response prediction and identification of new morphological features of clinical relevance. However, deep learning-based computational pathology approaches either require manual annotation of gigapixel whole slide images (WSIs) in fully-supervised settings or thousands of WSIs with slide-level labels in a weakly-supervised setting. Moreover, whole slide level computational pathology methods also suffer from domain adaptation and interpretability issues. These challenges have prevented the broad adaptation of computational pathology for clinical and research purposes. Here we present CLAM - Clustering-constrained attention multiple instance learning, an easy-to-use, high-throughput, and interpretable WSI-level processing and learning method that only requires slide-level labels while being data efficient, adaptable and capable of handling multi-class subtyping problems. CLAM is a deep-learning-based weakly-supervised method that uses attention-based learning to automatically identify sub-regions of high diagnostic value in order to accurately classify the whole slide, while also utilizing instance-level clustering over the representative regions identified to constrain and refine the feature space. In three separate analyses, we demonstrate the data efficiency and adaptability of CLAM and its superior performance over standard weakly-supervised classification. We demonstrate that CLAM models are interpretable and can be used to identify well-known and new morphological features. We further show that models trained using CLAM are adaptable to independent test cohorts, cell phone microscopy images, and biopsies. CLAM is a general-purpose and adaptable method that can be used for a variety of different computational pathology tasks in both clinical and research settings.