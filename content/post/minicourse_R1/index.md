---
title: 迷你課程:R語言-1
date: 2024-12-04
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
# Quick look
今天介紹R的data type:
1. Atomic vector
2. Vector
3. List
4. Matrix
5. Array

# Atomic vector
Atomic Vector 是 R 中最基本的資料類型之一，它只能包含相同類型的資料，例如數字、字串或布林值。

種類:
1. Numeric（數值）
2. Character（字串）
3. Logical（布林值）
4. Integer（整數）
5. Complex（複數）

Atomic vector可以很容易地用`c(...)`來建構起向量。
### Examples
```r
# 建立不同類型的 Atomic Vector
numeric_vec <- c(1.5, 2.3, 4.8)    # 數值向量
integer_vec <- c(1L, 2L, 3L)
character_vec <- c("apple", "banana", "cherry")  # 字串向量
logical_vec <- c(TRUE, FALSE, TRUE)  # 布林向量

# 查看資料類型
class(numeric_vec)
class(character_vec)
class(logical_vec)

```
我們可以針對atomic vector做一般的向量操作。而布林值的運算會先被轉成integer，再做加總。
```r
# 向量操作
numeric_vec * 2  # 每個元素乘以2
character_vec[1] # 獲取第一個元素
sum(logical_vec) # 計算布林值的數值總和 (TRUE = 1, FALSE = 0)
```
sum(logical_vec) 中的運算涉及`coercion(類型強制轉換)`，因為布林值(TRUE 和 FALSE) 被自動轉換為數值(1 和 0))來進行數學運算。

而向量有許多特性：
1. `length()`: 會得到向量長度。
2. `names()`: 會得到向量名稱。

而R有一個特殊的函式叫replacement function，也就是很多函式都可以藉由`指派`的方式改變某內容特徵：
```r
names(vector)<- c('Jackson', 'Joseph', 'Joanne')
```
這個在日後的數據處理非常常用，需要牢記。


### 何謂coercion?
`Coercion`是R中將一種資料類型自動轉換為另一種類型的過程。在這個例子中，邏輯型(logical)被轉換為數值(numeric)。

如果不小心將不同的data type用`c(...)`存到vector中，R會自動Coercion，並轉成higher type。而何謂higher type? R會依據下列的排序來將資料型態轉換為其中比較高階的類別：
> logical<integer<double<complex<character

而R也有一寫好用的`manual coercion`函式，如as.開頭的：
1. as.integer()
2. as.character()
3. as.double()
4. as.complex()

另外要使用迴圈時可以使用`as(c(x,x,x), 'character')`來轉換S4物件內之元素，比較方便。

---
# List
List 是一種可以容納不同資料類型或結構的`容器`，例如數字、字串、甚至是向量或矩陣。是一種non-atomic vector，且儲存過程不會產生`coercion`。

## Examples
```r
# 建立一個 List
my_list <- list(
  name = "John",
  age = 25,
  scores = c(85, 90, 78)
)

# 查看 List 中的元素
my_list$name
my_list$scores[2]  # 第二個成績
```

注意上面的my_list存了三個不同型態的元素，而且都賦予一個名稱。List的名稱可以用`$`取出來。如：

```
my_list$name
```
```
#>
$name
[1] "John"

```
也可以用雙括號`[[1]]`的方式取出來：
```
my_list[[1]]
```
```
#>
[1] "John"
```

這邊注意，在R裡面`[[]]`與`[]`取出的內容是不同的:
1. []會返回元素，但保持原來的結構。
2. [[]]會返回元素，但會移除結構。

簡單來說就是用`[]`取出的東西會維持list的型態，但是用`[[]]`取出的東西則**屬於**那個元素的型態，如果是`John`，那就是`character`型態。

---
# Matrix
Matrix 是一種二维的atomic vector，必須有相同的資料類型。

### Example
可以用`dim()`來將向量轉變成矩陣
```r
a <- 1:8
dim(a) <- c(4,2)
```
會得到
```
#>
      [,1] [,2]
[1,]    1    5
[2,]    2    6
[3,]    3    7
[4,]    4    8
```
而若是將矩陣的dimension attribute刪除，會將矩陣復原為向量。如：
```r
#復原成向量
dim(a) <- NULL
```
也可以直接用`matrix()`來建立矩陣。
```r
# 建立矩陣
my_matrix <- matrix(1:9, nrow = 3, ncol = 3)  # 3x3 矩陣

# 取出元素
my_matrix[2, 3]  # 第二row第三column的元素

# 矩陣操作
my_matrix * 2      # 每個元素乘以2
rowSums(my_matrix) # 計算每行的總和
colMeans(my_matrix) # 計算每列的平均值
```
另外R有一個特殊的`回收`概念，就是當給的元素數量低於要求時，會依狀況重複出現：
```r
matrix(1:3,3,4)
```
```
#>
     [,1] [,2] [,3] [,4]
[1,]    1    1    1    1
[2,]    2    2    2    2
[3,]    3    3    3    3
```
---
# Array
Array 是多維的數據結構，可以看作是矩陣的擴展。

### Example
```r
# 建立三維陣列
my_array <- array(1:12, dim = c(2, 3, 2))  # 2x3x2 陣列
```
```
#>
, , 1

     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

, , 2

     [,1] [,2] [,3]
[1,]    7    9   11
[2,]    8   10   12

```

```r
# 查看元素，注意第幾層是放在最後一個
my_array[1, 2, 2]  # 第2層中的第1row第2column的值
```
```
#>
[1] 9
```

```r
# 查看維度
dim(my_array)
```
```
#>
[1] 2 3 2
```
---
### 其他特殊值
1. NA: 表示missing value，是一種place holder，會顯示出來。
2. NULL: 是一種長度為0的物件，與NA不同，無法印出來，在需要刪除某些物件的時候可以派上用場。
3. Inf, -Inf: 也是一種place holder。
---
# 課程摘要

| 資料類型       | 特性                    | 範例                              |
|----------------|-------------------------|-----------------------------------|
| Atomic Vector  | 單一類型元素，1D       | `c(1, 2, 3)`                     |
| List           | 不同類型元素，1D       | `list(a = 1, b = "text")`        |
| Matrix         | 相同類型元素，2D       | `matrix(1:6, nrow = 2, ncol = 3)`|
| Array          | 相同類型元素，多維     | `array(1:12, dim = c(2, 3, 2))`  |