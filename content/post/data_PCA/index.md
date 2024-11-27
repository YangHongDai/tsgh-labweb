---
title: 數據科學技術盤點:主成分分析？
date: 2024-11-25
authors: ["戴揚紘", ""]
commentable: true
categories: [數據科學]
tags: [data science, diemensionality reduction, visualization]
isCJKLanguage: true
---
<!--more-->
## Quick look 
主成分分析（Principal component analysis, PCA）是一種強大且直觀的數據降維技術，被廣泛應用於臨床研究與醫學數據分析中。作為醫師，在日常工作中，我們經常面對大量的病患數據，例如基因表達數據、影像數據、實驗室檢驗值等。PCA能夠幫助我們提取數據的關鍵特徵，將高維度的資料轉換成易於解釋的低維度數據，從而揭示潛在的生物學意義。

- 想要瞭接基本概念，可以看**StatQuest**的[影片](https://www.youtube.com/watch?v=FgakZw6K1QQ)
- 想快速了解數學概念的，可以看李政軒老師的[影片](https://www.youtube.com/watch?v=JUPU8mJryL4&t=234s)

# 主成分分析的數學基礎
## 核心思想
PCA的目的是將高維數據投影到一組新的互相正交的坐標軸上（稱為主成分），這些軸的排列方式使得：

1. 第一個主成分最大程度地捕捉數據的變異性；
2. 第二個主成分捕捉剩餘變異性，且與第一主成分正交，依此類推。

也就是在一堆雜亂的數據中，找到變異程度最大的主軸來最大程度的代表這群資料，接著PCA會逐步找到與這些主軸正交的其他軸，這些軸共同構成一組新的坐標系。而所有原始數據的值都會重新投影到新的軸上。每個空間中的數據點可以被所有主成分<span style="color: red; font-weight: bold">**線性加成**</span>的方式來還原原始數據。整個過程可以大致簡化成如下的公式：

<div style="overflow-x: auto;">
$$
S = C_{\text{mean}} + t_1C_1 + t_2C_2 + \dots \text{(t:主成分權重; C:主成分)}
$$
</div>

## PCA的目的
我自己在分析基因數據的時候也很常用到PCA，甚至有些R bioconductor package也將PCA當成是標準前處理過程，但其實一開始都會思考，目前有其他降維工具，為何PCA還是很多人用？關於PCA的目的，初略有以下三點：
1. 利用降維，去除高關聯性多餘的維度
2. 利用視覺化在2維的座標上，發現離群值或異常值
3. 跟隨最大離散程度的軸向，保留原始訊息

由此可見，PCA可以幫助在目前動則維度數百的資料集中，還能用視覺化分析主要數據，並且評估哪些特徵維度不具有分群的效果，而可以考慮刪除或用其他方式過濾。

## 數學過程
整個過程概念是先找到空間中數據點的平均值*x-mean*，即數據的中心點，然後以*x-mean*為原點，尋找通過此點的一個方向向量*e*，對於所有數據點*xi*，計算他們相對於*x-mean*的差值，並將這些差值投影到方向*e*上，在*e*方向上的投影值的總變異性(即投影值平方的總和)如果達到最大值，則*e*為第一主成分。
這邊的*e*為長度為1的單位向量，也就是需要經過正規化(normalization)處理，此單位化向量確保了比較不同方向時，投影的變異性(方差)完全由數據本身決定，而非向量的長度。

所有數據點投影後的長度可以表達為：
<div style="overflow-x: auto;">
$$
\
e^T (\ x_1 - \bar{x}), e^T (\ x_2 - \bar{x}), \dots, e^T (\ x_n - \bar{x})
\
$$
</div>


而在*e*上的數據變異度為：
<div style="overflow-x: auto;">
$$
\
\sigma^2 = \frac{1}{n} \sum_{i=1}^n \left( e^T (\ x_i - \bar{x}) - 0 \right)^2
\
$$
</div>

接下來把上面的公式拆開：
平方公式可以看成兩個相同的元素相乘。
<div style="overflow-x: auto;">
$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^{n} \left(e^T (x_i - \bar{x}) \right)^2 = \frac{1}{n} \sum_{i=1}^{n} \left(e^T (x_i - \bar{x}) \right) \left(e^T (x_i - \bar{x}) \right)^T
$$
</div>

然而拆開為兩個矩陣，若要達到可以相乘的目的，後面的矩陣我們需要將其轉置。這邊我們回憶一下:
$$
(AB)^T=B^TA^T
$$
所以上面的公式可以變換成:
<div style="overflow-x: auto;">
$$
\frac{1}{n} \sum_{i=1}^n \left(e^T (x_i - \bar{x})\right) \left((x_i - \bar{x})^T e\right)
$$
</div>
<div style="overflow-x: auto;">
$$
=e^T \left( \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(x_i - \bar{x})^T \right) e = e^T \Sigma e
$$
</div>
到這邊我們已經可以發現，中間大框框包圍著的部分其實就是<span style="color: red; font-weight: bold">共變異矩陣(covariance matrix)！</span> 到此，我們已經可以看出來PCA要解的其實就是共變異矩陣。


## 實際運用
古人云：千言萬語不如一行code，我們來直接用R來玩玩看PCA是怎麼達成並且視覺化的。
 
#未寫完 待續













