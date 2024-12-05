---
title: 迷你課程:R語言-2
date: 2024-12-06
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R, DataFrame, Tibble]
isCJKLanguage: true
draft: false
---
<!--more-->
# Quick look
今天介紹R的兩種重要資料結構：
1. **Data Frame**: 傳統的資料表格式，類似於spreadsheet。
2. **Tibble**: Data Frame 的現代化版本，具有更直觀的特性與優化。

# Data Frame
Data Frame 是 R 中常用的資料結構之一，主要用於存儲行列形式的數據。每個`column`可以包含不同的數據類型（數字、字串、布林值等），但每`row`內的數據類型必須一致。

## 建立 Data Frame
可以使用 `data.frame()` 函數來建立 Data Frame：

```r
# 建立一個 Data Frame
df <- data.frame(
  Name = c("John", "Alice", "Bob"),
  Age = c(25, 30, 28),
  Score = c(85.5, 92.0, 78.5)
)

# 查看 Data Frame
print(df)
```
```
#>
   Name Age Score
1  John  25  85.5
2 Alice  30  92.0
3   Bob  28  78.5
```

### Data frame的操作
```r
df$Name  # 使用column name
df[, "Age"]  # 使用column name
df[["Score"]]  # 使用雙中括號

# 獲取row
df[1, ]  # 第一row

# 獲取特定元素，與matrix類似
df[2, 3]  # 第2 row第3 column

```
### Data Frame 的特性
允許帶有名稱的列和行:
可以使用 `names()`設置column名，也可以用`rownames()`設置row名。
```r
names(df) <- c("姓名", "年齡", "成績")
```
若有需要，也可以將data frame轉換為矩陣：
```r
as.matrix(df)
```
### 常用函數
```r
# 查看結構與摘要
str(df)  # 查看結構
summary(df)  # 查看摘要統計
```
---------

Tibble

Tibble 是 tidyverse 套件中的現代化 Data Frame，提供更友好的功能，特別適合處理大型或複雜數據。

建立 Tibble
可以使用 tibble() 函數來建立 Tibble：

Tibble 的優勢
不自動轉換資料類型:
不像 Data Frame，Tibble 不會將字串自動轉換為因子（Factor）。
顯示友好的輸出:
輸出格式簡潔，特別適合大數據集。
更靈活的子集選擇:
使用 $ 提取列，與 Data Frame 一樣簡單。
Tibble 與 Data Frame 的比較