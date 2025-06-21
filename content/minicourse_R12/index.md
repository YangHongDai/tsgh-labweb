---
title: 迷你課程:R語言-12~R 線性與邏輯迴歸建模教學：以內建資料 mtcars 與 Titanic 為例
date: 2025-04-11
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look

---
## 套件與資料讀取
```r
library(dplyr)  # 引入 dplyr 套件，用於資料整理與分組運算
```

## 使用 mtcars 進行多元線性迴歸分析
mtcars 是 R 內建的汽車數據集，每列是一種車款，變數包含馬力、油耗、重量等。

#### Step 1：檢視資料
```r
head(mtcars)
summary(mtcars)
```
我們觀察變數 mpg（Miles per Gallon，油耗）與其他變數的關係。

#### Step 2：簡單線性迴歸
```r
plot(mtcars$wt, mtcars$mpg)
model1 <- lm(mpg ~ wt, data = mtcars)
abline(model1, col = "blue")
summary(model1)
```

wt 為車重，mpg 為油耗。通常車越重油耗越差，這裡我們驗證其線性關係。

#### Step 3：多元線性迴歸（加入變數）
```r
model2 <- lm(mpg ~ wt + hp + cyl, data = mtcars)
summary(model2)
```
除了車重 wt，我們加上馬力 hp 與汽缸數 cyl。看是否這些變數能進一步解釋油耗的變異性。

#### Step 4：殘差檢查與變數可視化
```r
par(mfrow=c(2,2))
plot(model2)
```
用基本的 plot() 函數檢查殘差圖，觀察模型是否違反假設（如常態性、線性、等變異性等）。

---
## Titanic 資料集：邏輯迴歸分析

#### Step 1：讀取 Titanic 資料（內建於 titanic 套件或簡化自 Kaggle 資料）
```r
titanic <- read.csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
head(titanic)
```

#### Step 2：簡單統計與轉換
```r
library(dplyr)
titanic <- titanic |> select(Survived, Pclass, Sex, Age) |> filter(!is.na(Age))
titanic$Survived <- as.factor(titanic$Survived)
titanic$Pclass <- as.factor(titanic$Pclass)
```

我們挑選部分欄位進行簡化分析。將 Survived、Pclass 轉為類別變數。

#### Step 3：建立邏輯迴歸模型
```r
model_logit <- glm(Survived ~ Sex + Age + Pclass, data = titanic, family = "binomial")
summary(model_logit)
```
這是最基本的 logistic regression，解釋哪些變數與存活有關。

#### Step 4：預測機率與視覺化
```r
pred <- predict(model_logit, type = "response")
titanic$pred_prob <- pred

boxplot(pred_prob ~ Survived, data = titanic, col = c("red", "green"))
```
- type = "response" 可得每人存活機率。
- 使用 boxplot() 看機率與實際存活是否有明顯區別。

#### Step 5：建立分類標準並評估
```r
titanic$pred_class <- ifelse(pred > 0.5, 1, 0)
table(Predicted = titanic$pred_class, Actual = titanic$Survived)
```
使用閾值 0.5 建立二元分類，並建立混淆矩陣觀察預測效果。