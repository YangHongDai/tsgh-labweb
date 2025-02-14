---
title: 迷你課程:R語言-8~Debugging
date: 2025-02-14
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: true
---
<!--more-->
## Quick look
在 R 中，程式錯誤`（Error）`與異常`（Exception）`處理是開發過程中不可或缺的一環。有效的 Debugging 技術能幫助開發者迅速找出錯誤，提升程式的穩定性與可維護性。本篇文章將介紹 R 語言中的 5 種除錯方法，包括 try()、tryCatch()、debug()、browser() 以及 RStudio 的 code breakpoints，幫助你更有效率地修正錯誤。

---
## 基本錯誤示範與問題描述
假設我們要計算條件期望（Conditional Expectation） 在多變量常態分佈下:
我們定義一個函數 cond_exp() 來計算條件期望：

### 定義共變異數矩陣與數據向量
```r
n <- 10
A <- matrix(rnorm(n*n), n, n)
S <- A %*% t(A)
y <- A %*% rnorm(n)

# 條件期望計算函數
cond_exp <- function(S, y, i1, i2){
    y2hat <- S[i2,i1] %*% solve(S[i1,i1], y[i1])
    return(y2hat)
}

# 測試函數
cond_exp(S, y, 1:(n-1), n)
cond_exp(S, y, n-2, (n-1):n)  # 可能產生錯誤
```

---
如果執行後發生錯誤，如何有效除錯？以下介紹 5 種方法。
## 方法 1: 手動檢查變數 (Print Statements)
透過 print() 逐步檢查變數：
```r
cond_exp <- function(S, y, i1, i2){
    print("S21")
    print(S[i2,i1])
    print("S11")
    print(S[i1,i1])
    print("y1")
    print(y[i1])
    print(solve(S[i1,i1], y[i1]))
    print(dim(S[i2,i1]))
    print(dim(solve(S[i1,i1], y[i1])))
    y2hat <- S[i2,i1] %*% solve(S[i1,i1], y[i1])
    return(y2hat)
}
cond_exp(S, y, n-2, (n-1):n)
```
這種方法適用於簡單錯誤，但當函數過於複雜時，效率較低。

## 方法 2: 使用 try() 忽略錯誤
`try()` 可確保程式繼續執行，即使發生錯誤：
```r
res <- try(cond_exp(S, y, n-2, (n-1):n))
print(res)
```
但 `try()` 只適合錯誤處理，不適用於深度除錯。

## 方法 3: 使用 debug() 逐步執行
那有沒有更簡單的方式，可以進入函示一虧究竟呢？ R 提供了 `debug()`， 讓我們進入函數內部：
```r
debug(cond_exp)
cond_exp(S, y, n-2, (n-1):n)
undebug(cond_exp)  # 停止 debug 模式
```
在我們想要除錯的函式使用`debug()`後，執行函式會進入`debug`模式
在`console`會出現`Browse`模式，我們可以使用不同的操作來找出錯誤的地方：

1. `n (Next)`：執行下一步，會依序出現執行後的變數於暫存環境，此時可以針對變數做操作，但如果該行還沒執行，則無法針對該變數進行操作。

2. `s (Step)`：進入子函數內部

3. `f (Finish)`：執行至函數結束

4. `c (Continue)`：繼續執行至結束

5. `Q (Quit)`：退出 debug 模式

#### Let's fix this
因為S11 或S21 轉換時出現向量而不是矩陣，因此在運算時導致維度不吻合。
```r
cond_exp <- function(S, y, i1, i2){
      y1 <- y[i1]
      S11 <- S[i1,i1, drop=FALSE] # 避免在subset matrix 時返回向量
      S21 <- S[i2,i1, drop=FALSE] # 避免在subset matrix 時返回向量
    y2hat <- S[i2,i1] %*% solve(S[i1,i1], y[i1])
    return(y2hat)
}
```

## 方法 4: 使用 browser() 設定斷點
`browser()` 允許在程式特定位置進入除錯模式：
```r
cond_exp <- function(S, y, i1, i2){
    y1 <- y[i1]
    S11 <- S[i1,i1]
    S21 <- S[i2,i1]
    browser()
    y2hat <- S21 %*% solve(S11, y1)
    return(y2hat)
}
cond_exp(S, y, n-2, (n-1):n)
```
當執行到 browser()，程式會暫停，允許手動輸入指令來檢查變數。如此一來不用像上面`debug()`一樣需要用`n`一個一個去執行每一行來產生變數，也就是不必從頭開始除錯，但前提是我們知道錯誤在哪一行。

## 方法 5: 使用 traceback() 追蹤錯誤發生位置
當函數內部的函數發生錯誤時，`traceback()` 可找出錯誤來源：
```r
f1 <- function(x){ y2 <- f2(x); return(y2) }
f2 <- function(x){ y1 <- f3(x); y2 <- y1 - mean(y1); return(y2) }
f3 <- function(x){ return(solve(x)) }

f1(matrix(0,2,2))  # 會發生錯誤
traceback()  # 追蹤錯誤來源
```
錯誤原因是 f3 函數中的 solve(x) 呼叫無法處理輸入的矩陣。solve 函數用於計算矩陣的逆，但前提是矩陣`必須是可逆的`。當您提供一個全為零的 2x2 矩陣時，該矩陣是`奇異的（行列式為零）`，不可逆，這導致 solve 函數無法計算其逆矩陣，從而產生錯誤。
`traceback()`這種方法適合偵測函數`嵌套過深`導致的錯誤。

## 課程小結
R 語言提供多種強大的 Debugging 工具，包括：
1. 手動 print() 檢查變數（適合簡單錯誤）
2. try() 忽略錯誤（適合錯誤處理，但不適用於深度 Debugging）
3. debug() 進入函數內部（適合逐步檢查）
4. browser() 設定程式斷點（適合特定位置 Debugging）
5. traceback() 追蹤錯誤位置（適合偵測嵌套錯誤）



