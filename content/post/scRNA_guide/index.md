---
title: 初探單細胞定序
date: 2024-12-09
authors: ["戴揚紘", ""]
commentable: true
categories: [單細胞定序]
tags: [scRNA-seq, data science]
isCJKLanguage: true
draft: true
---
<!--more-->
## Quick look
單細胞定序已經在近年成為各大實驗室不可或缺的關鍵技術之一，讓我們從過去將組織混雜在一起的bulk RNA-seq精細化到單細胞的解析度，也讓我們可以針對一顆腫瘤做細部的分類，、甚至推測細胞分化的路徑，今天我們要讀的[文章](https://www.nature.com/articles/s41596-018-0073-y)算是比較舊的nature protocol review article (2018)，但針對我們想要做單細胞定序分析的人來說是很推薦的入門讀物之一。

## scRNA-seq 席捲科學界
scRNA-seq 顯著增加了我們對組織、器官和細胞之間複雜性的交互作用。隨著自動化處理流程的演進與微流體（microfluidic）技術的發明，scRNA-seq的延展性（scalability）大幅的提升。

過往的實驗設計通常是基於某一個假說或是`假設（hypothesis）`，但若是這個假設錯誤或是不成立，就要花額外的時間從另外一個假設著手，這種`hypothesis-driven`的方式比較費時。自從有了scRNA-seq後，我們可以一探每一顆細胞的全基因組、蛋白質組甚至是表觀遺傳基因組，從hypothesis-driven過渡到`data-driven`的實驗設計，大幅降低bulk狀態下帶來的`biased analysis`。

但因為scRNA-seq的研究太專一化，不同的樣本有截然不同的處理步驟，而數據分析也依據不同的需求而有所不同，因此在研究設計上無法將一套準則套用在所有的實驗上，但也因為這個限制，近年有層出不窮的protocol、tools或是網頁工具出現，試圖來優化及改善整條從樣本製備到數據分析的過程 (圖一)。

![fig1](fig1.png '圖一 單細胞定序流程')

## 樣本製備
樣本本身的品質對整個scRNA-seq的流程是最重要的，雖然先前大部分都需要新鮮活的細胞，但實務上如果要在取出每個腫瘤後立即分解成單細胞懸浮液其實頗具挑戰性，因此目前有不少protocol是允許使用固定後腫瘤或細胞，也允許冷凍後仍完整的細胞核RNA，一來可以讓我們可以好好計畫樣本製備的流程，二來也不影響後續數據的分析，可以參考目前10X Genomics釋出的[GEM-X FLEX protocol](https://www.10xgenomics.com/support/single-cell-gene-expression-flex/documentation/steps/library-prep/gem-x-flex-gene-expression-reagent-kit-for-multiplex-samples)。

其他一些注意事項如下：
1. 使用`無核酸酶`試劑和耗材。
2. 減少樣本溶液的`轉移`與`離心`操作以避免細胞損傷。
3. 篩選較大的細胞團塊和細胞死亡後的雜質與碎片。最好在`30分鐘內`用酵素分解細胞團塊，避免團塊聚集。
4. 適合的懸浮液緩衝液組成：`無鈣、鎂的PBS`。含牛血清白蛋白以減少聚集。比較敏感的細胞、幹細胞可能需要其他的緩衝液來增加存活。

## 細胞懸浮液的製備
血液樣本可以用密度梯度離心（density centrifugation）的方式來分離，例如Ficoll-Paque 或 Histopaque-1077 的方式來捕捉特定單細胞，但是實體組織必須要利用機械（mechanical）或是酵素來分解組織塊來取得單細胞懸浮液。
1. 機械方式：可以用剪刀或是剃刀將組織切成小碎塊，通常約大小 1mm x 1mm x 1mm，才能增加與酵素接觸的表面積。
2. 酵素分解：切成小塊後，要接著用酵素做分解，針對不同的組織有不同的酵素組合，可以參考圖二。

![fig2](fig2.png '圖二 不同組織所建議的分解酵素')

值得注意的是，在樣本製備的過程中，活的細胞有可能會因為過程中遭遇的stress而導致某些反應性基因的表現改變，因此過程中需要盡可能地減少stress。

另外就是針對像神經元所在的組織中，神經元彼此之間交聯的程度有可能會導致細胞分離的過程不完全。針對這個問題可以考慮破壞細胞膜的方式來取得完整的細胞核做分析，而用細胞核內部的RNA做分析雖然會降低每顆細胞最終的解析度，但是已能提供足夠訊息來解析細胞態 （cell type deconvolution）。

## 單細胞捕獲
目前許多不同的方式來達成單細胞的捕獲：
1. Microdissection
2. Pipetting
3. Fluorescence-activated cell sorting (FACS)
4. Microfluidics

後面兩個技術為high-throughput，可以有效率的捕獲大量的單細胞。FACS 帶有特定螢光的細胞`挑`出來，並收集到微孔板（microtiter plate）中；而microfluidics 是利用integrated fluidic circuits (IFC)、油滴或是奈米板（nanowell）、來同時收集及處理細胞，`減少試劑的使用`。有些時候為了降低背景噪音及最大化定序的表現，可以在使用microfluidic 系統前先用FACS或`MACS（magnetic-activated cell sorting`）來移除死細胞或是雜質。

## 樣本大小與組成

