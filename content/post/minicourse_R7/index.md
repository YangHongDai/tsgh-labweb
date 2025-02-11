---
title: 迷你課程:R語言-7~錯誤的處理
date: 2025-01-15
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在 R 中，處理`異常（Exception）` 和 `錯誤（Error）`是開發過程中的關鍵，能有效避免因不預期的錯誤導致程式崩潰。本篇文章將介紹如何使用 `try`、`tryCatch` 和 `condition handling` 來應對錯誤情境，確保程式能夠順利執行。

---
## 什麼是錯誤與例外？
當執行函數時，可能會遇到錯誤。例如，嘗試對非 square 矩陣求逆時，會拋出錯誤：
```r
inverse <- function(M) { solve(M) }

mat <- matrix(1:10, 5, 2)  # 非方陣
inverse(mat)
# Error: 'a' (5 × 2) must be square

mat <- diag(x = 1:5)  # 可逆方陣
inverse(mat)  # 正常運行

mat <- diag(x = rep(0, 5))  # 奇異矩陣
inverse(mat)
# Error: system is computationally singular: reciprocal condition number = 0
```
當矩陣不是方陣或是奇異矩陣（行列式為 0），函數 solve() 會拋出錯誤，導致程式終止。因此，我們需要適當的錯誤處理機制。

---
## 使用 try 忽略錯誤
`try()` 允許程式在錯誤發生時繼續執行，而不會中斷：
```r
mat <- diag(x = rep(0, 5))
res <- try(invmat <- inverse(mat))  # 錯誤不會終止程式

mat <- diag(x = rep(2, 5))
res <- try(invmat <- inverse(mat))  # 正常運行
```
這樣，即使 inverse(mat) 出錯，程式也不會崩潰。

---
## 使用 tryCatch 進行錯誤處理
`tryCatch()` 提供更細緻的錯誤處理方式，允許我們針對特定錯誤自訂處理方式：
```r
library("rlang")

mat <- matrix(1:10, 5, 2)
res <- catch_cnd(inverse(mat))  # 捕捉錯誤訊息
```
舉例來說，我們可以寫一個函數來計算一組矩陣的逆，並對錯誤做適當處理：
```r
inverse_list <- function(matrix_list) {
    inverse_list <- list()
    for (j in 1:length(matrix_list)) {
        print(j)
        inverse_list[[j]] <- tryCatch(
            expr = { solve(matrix_list[[j]]) },
            error = function(cnd) { print(cnd) }  # 當錯誤發生時，輸出錯誤訊息
        )
    }
    return(inverse_list)
}

matrix_list <- list(diag(x = 1:5), diag(x = rep(0, 5)), matrix(1:10, 5, 2))
ilist <- inverse_list(matrix_list)  # 執行函數
ilist
```
當發生錯誤時，程式不會崩潰，而是輸出錯誤訊息並繼續執行後續的矩陣求逆。

---
## 讓 tryCatch() 返回更具意義的結果
當錯誤發生時，除了輸出錯誤訊息，還可以讓函數返回更具意義的值，例如 NA：
```r
inverse_list <- function(matrix_list) {
    inverse_list <- list()
    for (j in 1:length(matrix_list)) {
        print(j)
        inverse_list[[j]] <- tryCatch(
            expr = { solve(matrix_list[[j]]) },
            error = function(cnd) {
                print(cnd)
                return(NA)  # 發生錯誤時，返回 NA
            }
        )
    }
    return(inverse_list)
}

ilist <- inverse_list(matrix_list)
ilist  # 錯誤矩陣返回 NA
```
這樣當矩陣無法求逆時，我們可以用 NA 表示，而不是直接崩潰。

---
## 根據錯誤訊息進一步處理
我們可以檢查錯誤訊息，根據不同錯誤類型做不同處理：
```r
cnd1 <- catch_cnd(solve(matrix_list[[2]]))
str(cnd1)  # 檢視錯誤訊息
cnd1$message
cnd1$call

cnd2 <- catch_cnd(solve(matrix_list[[3]]))
str(cnd2)
cnd2$message
cnd2$call
```
利用 grepl() 檢查錯誤類型：
```r
grepl("is exactly singular", cnd1$message)  # TRUE
grepl("is exactly singular", cnd2$message)  # FALSE
grepl("must be square", cnd1$message)       # FALSE
grepl("must be square", cnd2$message)       # TRUE
```
這些條件幫助我們決定如何處理錯誤。

---
## 進一步改進錯誤處理邏輯
根據錯誤訊息，提供更具體的處理方式：
```r
inverse_list <- function(matrix_list) {
    inverse_list <- list()
    for (j in 1:length(matrix_list)) {
        print(j)
        inverse_list[[j]] <- tryCatch(
            expr = { solve(matrix_list[[j]]) },
            error = function(cnd) {
                if (grepl("is exactly singular", cnd$message)) {
                    return(array(NA, dim(matrix_list[[j]])))  # 奇異矩陣回傳 NA 矩陣
                } else if (grepl("must be square", cnd$message)) {
                    stop(cnd$message)  # 非方陣直接終止
                } else {
                    stop(cnd$message)  # 其他錯誤同樣終止
                }
            }
        )
    }
    return(inverse_list)
}

ilist <- inverse_list(matrix_list)
```
這樣：
- 奇異矩陣 返回全 NA 矩陣。
- 非方陣 直接終止程式。

---
## 提前檢查矩陣是否符合條件
為了提高效率，我們可以事先檢查矩陣是否為 square，避免不必要的運算：
```r
inverse_list <- function(matrix_list) {
    inverse_list <- list()

    for (j in 1:length(matrix_list)) {
        if (nrow(matrix_list[[j]]) != ncol(matrix_list[[j]])) {
            stop(paste("Matrix", j, "is not square."))
        }
    }

    for (j in 1:length(matrix_list)) {
        print(j)
        inverse_list[[j]] <- tryCatch(
            expr = { solve(matrix_list[[j]]) },
            error = function(cnd) {
                if (grepl("is exactly singular", cnd$message)) {
                    warning(paste("Matrix", j, "is singular"))
                    return(array(NA, dim(matrix_list[[j]])))
                } else {
                    stop(cnd$message)
                }
            }
        )
    }
    return(inverse_list)
}

```
這樣可以事先篩選不符合條件的矩陣，提高效率。

--
## 課程小結
在 R 語言的開發過程中，錯誤處理至關重要，尤其是在需要確保程式能夠持續執行而不崩潰的情境下。本篇文章介紹了 try()、tryCatch() 以及 condition handling 的使用方式，幫助我們有效管理錯誤並根據不同情境做適當處理。

我們首先透過 try() 讓程式在遇到錯誤時不會中斷，但 try() 只能簡單忽略錯誤，無法提供詳細錯誤處理機制。因此，tryCatch() 提供了更進階的解法，允許我們針對特定錯誤定義不同的回應方式，例如記錄錯誤訊息、返回特定值（如 NA）、甚至根據錯誤類型執行不同處理邏輯。

此外，我們進一步結合錯誤訊息解析（catch_cnd()），透過 grepl() 檢查錯誤內容，實現更細緻的錯誤分類與應對，例如：

奇異矩陣（Singular Matrix） → 返回 全 NA 矩陣 以確保數據格式一致。
非方陣（Non-Square Matrix） → 直接終止程式，避免不必要的運算。