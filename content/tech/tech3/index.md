---
title: Sequence modeling and design from molecular to genome scale with Evo
date: 2024-12-21
authors: ["戴揚紘", ""]
commentable: true
categories: [論文技術分享]
tags: [Computational biology]
isCJKLanguage: true
draft: false
url_code: 'https://github.com/evo-design/evo'
url_source: 'https://www.science.org/doi/10.1126/science.ado9336'
---
<!--more-->
近期發表於《科學》期刊的研究介紹了Evo，一種具備7億參數的基因組基礎模型 (Foundation model)，能夠從單個核苷酸到整個基因組進行序列建模和設計。 Evo使用`StripedHyena`架構，能夠以接近線性的計算和記憶體擴展來處理長序列，實現`單核苷酸`級別的解析度。 
該模型在`OpenGenome`資料集上進行訓練，該資料集包含約270萬個原核生物和噬菌體基因組序列，總計約3000億個標記。 Evo在DNA、RNA和蛋白質等多種生物模式下的`零樣本 (Zero shot)`功能預測任務中表現出色，並能夠生成功能性生物系統，如CRISPR-Cas複合物和轉座子。 

- 架構：採用了 StripedHyena，這是一種`混合注意力-卷積架構`，能夠以單核苷酸級別的解析度高效處理長序列數據。
- 訓練：基於 270 萬個基因組進行訓練，支持最長 131kb 的上下文長度。
- 應用：在突變效應的零樣本預測，以及操縱子、CRISPR 系統和大型基因組序列的生成方面有著出色表現。

## 何謂Zero shot?
Zero-shot prediction 指的是一種機器學習模型能夠在從未見過或未特別訓練過的任務上進行推斷和預測的能力。這種方法的核心理念是利用模型的泛化能力，讓模型在沒有明確針對目標任務的標訓練數據下，依賴其先前學到的知識完成新任務。