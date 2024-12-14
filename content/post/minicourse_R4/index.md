---
title: 迷你課程:R語言-4~Function的定義與運用
date: 2024-12-14
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在 R 語言中，函數能夠幫助我們培養重複使用和結構化程式的能力。本篇文章將介紹：
1. R 函數如何定義。
2. 函數使用的優化方式。
3. 常用的有用函數和工具。

---
## 如何定義函數
基本定義如下：
```r
my_function <- function(arg1, arg2) {
  result <- arg1 + arg2
  return(result)
}

my_function(5, 10) # 返回 15

```
- `function()` 定義函數。

- `參數 (例如 arg1 和 arg2)` 可指定`多個`。

- `return()` 指定返回值，若未指定則`默認返回最後一行的計算結果`。
  
我們可以根據上面的格式來寫一個寫當的平方函數：
```r
square <- function(x){
y <- x^2
return(y)
}

```
函數在R也是一種物件（object），所以這邊新建立的square也是一個函數物件，可以用來進行輸入參數的平方運算，然後返回運算後的值，但其實這個寫法可以再精簡，因為如果你還記得，未指定則`默認返回最後一行的計算結果`，所以可以精簡成：
```r
square <- function(x){
x^2
}
```
如此一來square(3)就會自動印出9，同樣的結果，但是少了`assignment`與`return`兩個操作。

---

## 默認值
R 允許在定義函數時設定參數的默認值，這樣就不用在運算時每次都要把全部參數寫出來：
```r
my_function <- function(arg1, arg2 = 10) {
  result <- arg1 + arg2
  return(result)
}

my_function(5) # 返回 15，因為 arg2 默認為 10
```

---

## 不定數量參數
R 允許定義不定數量的參數：
```r
my_function <- function(...) {
  args <- list(...)
  sum(args)
}

my_function(1, 2, 3, 4) # 返回 10
```
再看另一個例子：
```r
fun <- function(..., fun=mean, p =0.5){
  x <- c(...)
  x-fun(x)
}

fun(10,30,40,50)
```
因為可以讓使用者輸入任意數量的數字，然後再轉換成向量，增加函式的彈性。
```
#>
[1] -22.5  -2.5   7.5  17.5
```
---
## 避免重複代碼
將常用函數放到函數裡，以減少重複代碼：
```r
normalize <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

normalize(c(1, 2, 3, 4, 5)) 
```
---
## 加入錯誤處理
使用 stop() 來對函數輸入進行檢查：
```r
safe_divide <- function(a, b) {
  if (b == 0) stop("分母不能為 0")
  a / b
}

safe_divide(10, 2) # 返回 5
safe_divide(10, 0) # 結束執行並出現錯誤訊息
```
---
## 搭配do.call()
使用 `do.call()` 來加強函數的呼叫：
```r
sum_values <- function(...) {
  sum(...)
}

do.call(sum_values, list(1, 2, 3, 4)) # 返回 10
```
> 需要注意的是，do.call() 的第一個參數為函數名稱，第二個參數為需要被這個函數呼叫的元素list，如果list中只有一個atomic vector，該函數將把這個向量作為單一參數處理（例如，作為一個整體傳遞）。如果list中有數個vectors，do.call() 會將 list 的元素解構為函數的獨立參數，依序傳入。如把vector1中的第一個元素和vector2中的第一個元素當作參數，以此類推。

```r
# 單一 atomic vector 作為 list 中唯一元素
do.call(sum, list(c(1, 2, 3, 4)))  # 等同於 sum(c(1, 2, 3, 4))，結果是 10

# 多個向量作為 list 中的元素
do.call(paste, list(c("A", "B"), c("C", "D"), sep = "-"))
# 等同於 paste("A", "C", sep = "-") 和 paste("B", "D", sep = "-")
# 結果是 "A-C" 和 "B-D"
```

如果還記得data frame 是list的集合，所以我們可以將data frame 當成參數。如果要新增一欄list做處理，需要用`c()`:
```r
df <- data.frame(first = c(1,2,3),
                 second = c(2,4,6))
do.call(paste, c(df,'+'))
```
會得到：
```
#>
[1] "1 2 +" "2 4 +" "3 6 +"
```
---
## 使用重要套件
和 purrr 套件配合：
```r
library(purrr)

square <- function(x) x^2
map(c(1, 2, 3, 4), square) # 返回 1, 4, 9, 16
```
> map為purrr套件中的好用函式，之後會專門討論。

---
## 輸入驗證
```r
library(assertthat)
assert_that(is.numeric(10)) # 通過
```

---
## 接合與對齊
使用`mapply()` 與 `apply()` 。
```r
mapply(function(x, y) x + y, 1:3, 4:6) # 返回 5, 7, 9
```
`mapply()` 是一個向量化函數，適用於對`多個向量`或`列表`同時應用一個函數。它的功能相當於對多個`對應元素進行逐一計算`。

其實不難發現，上面的運算等同於：
```r
do.call(function(x, y) x + y, list(c(1,2,3), c(4,5,6)))
```

```r
mat <- matrix(1:6, nrow = 2)
apply(mat, 1, sum)  # 對每一列求和
# Output: c(9, 12)

apply(mat, 2, sum)  # 對每一欄求和
# Output: c(3, 7, 11)
```

| 功能         | `mapply()`                     | `apply()`                                   |
|--------------|---------------------------------|---------------------------------------------|
| 適用場景     | 對多個向量或列表逐一操作       | 對矩陣或數據框的行或列進行批量操作          |
| 輸入數據類型 | 向量、列表                     | 矩陣、數據框                                |
| 返回值       | 簡化後的向量或列表             | 矩陣、數據框，或者簡化後的向量              |
| 常見應用     | 處理多組向量對應元素的計算     | 操作數據的每一行或每一列     

---

## 課程小結
| 主題             | 特性                                  | 範例                                       |
|------------------|---------------------------------------|--------------------------------------------|
| 函數定義         | 使用 `function()` 定義帶有參數和返回值的函數 | `my_function <- function(x, y) x + y`      |
| 默認值           | 可為函數參數設定默認值                | `my_function <- function(x, y = 10)`       |
| 不定數量參數     | 使用 `...` 接收任意數量的輸入參數       | `my_function <- function(...) sum(...)`    |
| 重複代碼優化     | 通過函數封裝常用邏輯來減少重複代碼     | `normalize <- function(x) (x - min(x)) / (max(x) - min(x))` |
| 錯誤處理         | 使用 `stop()` 進行輸入檢查與報錯       | `safe_divide <- function(a, b) if (b == 0) stop("分母不能為 0")` |
| `do.call()`       | 將列表解構為函數參數                  | `do.call(sum, list(1, 2, 3, 4))`           |
| 搭配 purrr 套件  | 使用 `map()` 對向量逐一應用函數         | `map(c(1, 2, 3), ~ .x^2)`                 |
| 向量化運算       | 使用 `mapply()` 處理多組向量            | `mapply(function(x, y) x + y, 1:3, 4:6)`   |
| 行列操作         | 使用 `apply()` 處理矩陣行或列的計算      | `apply(matrix(1:6, nrow = 2), 1, sum)`     |
