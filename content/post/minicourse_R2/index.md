---
title: 迷你課程:R語言-2
date: 2024-12-05
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
今天介紹R的兩種重要資料結構：
1. **Data Frame**: 傳統的資料表格式，類似於spreadsheet。
2. **Tibble**: Data Frame 的現代化版本，具有更直觀的特性與優化。

---

## Data Frame
Data Frame 是 R 中常用的資料結構之一，主要用於存儲行列形式的數據。每個`column`可以包含不同的數據類型(數字、字串、布林值等)，其實就是將list數據框化，但每`row`內的數據類型必須一致。

---
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
---
## Data frame的操作
```r
df$Name  # 使用column name
df[, "Age"]  # 使用column name
df[["Score"]]  # 使用雙中括號

# 獲取row
df[1, ]  # 第一row

# 獲取特定元素，與matrix類似
df[2, 3]  # 第2 row第3 column

```

---
## Data Frame 的特性
允許帶有名稱的列和行:
可以使用 `names()`設置column名，也可以用`rownames()`設置row名。
```r
names(df) <- c("姓名", "年齡", "成績")
```
若有需要，也可以將data frame轉換為矩陣：
```r
as.matrix(df)
```
## 常用函數
```r
# 查看結構與摘要
str(df)  # 查看結構
summary(df)  # 查看摘要統計
```
---------

## Tibble

Tibble是`tidyverse`套件中的Data Frame，提供更友好的功能，特別適合處理大型或複雜數據。

---
## 建立 Tibble
可以使用`tibble()`函數來建立Tibble：
```r
# 載入 tidyverse
library(tibble)

# 建立一個 Tibble
tb <- tibble(
  Name = c("John", "Alice", "Bob"),
  Age = c(25, 30, 28),
  Score = c(85.5, 92.0, 78.5)
)

# 查看 Tibble
print(tb)
```

```
#>
# A tibble: 3 × 3
  Name    Age Score
  <chr> <dbl> <dbl>
1 John     25  85.5
2 Alice    30  92.0
3 Bob      28  78.5
```
Tibble僅顯示前幾行和列的數據，幫助我們快速預覽，避免大數據集導致的視覺上的overload。另外tibble輸出的數據框會帶入每一column的資料型態，幫助我們迅速了解數據框。

---

## Tibble 的優勢
1. 不自動轉換資料類型。
2. 輸出格式簡潔，特別適合大數據集。
3. 使用 $ 提取列，與 Data Frame 一樣簡單。

---
## Tibble與Data Frame的比較
```r
# 將 Data Frame 轉換為 Tibble
tb_from_df <- as_tibble(df)

# 查看差異
class(df)  # "data.frame"
class(tb_from_df)  # "tbl_df" "tbl" "data.frame"
```

---
## Data Frame 與 Tibble 的操作對比
| 功能                | Data Frame                             | Tibble                            |
|---------------------|-----------------------------------------|------------------------------------|
| 建立資料結構        | `data.frame()`                         | `tibble()`                        |
| 取值方式            | `df[1, "Name"]` 或 `df$Name`           | `tb[1, "Name"]` 或 `tb$Name`      |
| 資料類型轉換        | 預設將字串轉換為因子                   | 不會自動轉換字串                  |
| 輸出格式            | 完整列印，可能過多                     | 友好格式，適合大數據              |
| 結構查看            | `str(df)`                              | `glimpse(tb)`                     |

---
## 使用dplyr與Tibble結合
1. data frame 也可以用dplyr串接，但是tibble的設計可以讓整體更簡潔。使用`dplyr`操作時，特別是在篩選`filter`和分組`group_by`中處理字串數據時更加直觀。
2. tibble()不允許引用不存在的column，而data.frame()則可能返回 NULL，這容易導致隱蔽錯誤。
3. 支持非標準列名：Tibble 支持包含空格或特殊字符的列名，而Data Frame通常需要更複雜的處理。
```r
# 載入 tidyverse
library(tidyverse)

# 篩選年齡大於27的資料
filtered_tb <- tb %>% 
  filter(Age > 27)

# 新增一欄，計算加權分數
tb <- tb %>%
  mutate(Weighted_Score = Score * 0.9)

# 排序
tb <- tb %>%
  arrange(desc(Age))
```
```r
tb <- tibble(
  'Name A' = c("John", "Alice", "Bob"),
  Age = c(25, 30, 28),
  Score = c(85.5, 92.0, 78.5)
)

#tibble可以允許中間有空格的column name，但是data frame則會自動將空格縮成.，會導致錯誤
tb$`Name A`
```

關於tidyverse的部分，後續我會專門做介紹。

---------
## 課程摘要
| 資料類型       | 特性                                  | 範例                              |
|----------------|---------------------------------------|-----------------------------------|
| Data Frame     | 行列結構，row內類型一致，column間可不同    | `data.frame(Name, Age, Score)`   |
| Tibble         | 現代化 Data Frame，靈活且友好         | `tibble(Name, Age, Score)`       |