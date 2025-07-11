---
title: 迷你課程:R語言-12~R 套件
date: 2025-06-28
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
學會在 R/RStudio 中使用 devtools + roxygen2 開發一個完整的 R 套件，並了解每個檔案/資料夾的結構、功能與開發流程。

---
## 建立 Package 骨架
```r
install.packages(c("devtools", "roxygen2", "testthat", "usethis"))
```
#### devtools
提供開發 R 套件的核心功能，如 `load_all()`, `check()`, `document()`, `install()` 等，是現代 R 套件開發的核心工具。
---
#### roxygen2
`roxygen2` 是 R 語言中用來`自動產生文件（documentation）的套件`，它的目的是：`將函數註解與文件寫在一起`，然後自動產生符合 R 套件規範的 `.Rd 說明檔`與 `NAMESPACE`。

##### 傳統的 R 套件開發，需要你分別：
1. 寫函數在 `R/*.R 裡`
2. 寫說明`文件在 `man/*.Rd` 檔案（這是繁瑣的手動寫 LaTeX-like 的語法）
3. 修改 `NAMESPACE `檔案手動加上 `export()` 等宣告

非常容易出錯。

而 roxygen2 解決這些問題，讓你：

- 只要在每個函數上方寫好 `#'` 標記的文件區塊
用 `devtools::document()` 一指令，就會`自動幫你產生 .Rd 和 NAMESPACE`。

##### 常見roxygen2 標籤:
- `@param`: 說明輸入參數
- `@return`: 說明回傳值
- `@export`: 表示這個函數會對外開放使用
- `@examples`: 給出範例用法
- `@import`:匯入其他 package 的函數
- `@seealso`:指向相關函數
- `@details`:補充更多詳細說明

---
#### testthat
最常用的 R 套件測試框架。可撰寫單元測試、自動化測試流程，與 devtools::check() 無縫整合，確保函數正確性。

#### usethis
專為快速建立、組織 R 套件架構而設計。可用來建立專案、函數檔案、測試、vignette、LICENSE…等，簡化大量手動操作。


## 建立專案與初始結構

```r
usethis::create_package("MyPacakge")
```
此時會在Rstudio預設的`Home`自動生成以下基本結構:
```r
MyPackage/
├── DESCRIPTION
├── NAMESPACE
├── R/
├── weatherAPI2.Rproj
├── .Rbuildignore
└── .gitignore
```
如果沒有指定路徑，套件位置會出現在:
- macOS / Linux: ~/（home folder）
- Windows: C:/Users/你的帳號/

#### 如何避免自動跳出 RStudio 專案？
如果你只想生成 package 而不切換 session，可以加參數：
```r
usethis::create_package("~/your/path/MyPacakge", open = FALSE)
```

---
## 每個檔案／資料夾解釋
- DESCRIPTION: 套件的 metadata（名稱、作者、版本、依賴套件）
- NAMESPACE: 宣告哪些函數對外暴露（由 roxygen2 自動產生），檔案開頭會顯示: `Generated by roxygen2: do not edit by hand`
- R/: 放置你寫的所有 .R 原始程式碼檔案
- .Rbuildignore: 指定哪些檔案不應被打包，例如 .Rproj, .git/ 等
- .gitignore: Git 專案忽略的檔案規則
- MyPacakge.Rproj: RStudio 專案設定檔

## 撰寫函數與註解
```r
#' Retrieve cancer data for patient and subtype
#'
#' @param pat patient data
#' @param sub cancer subtypes
#' @return A list with cancer patient information
#' @export
get_cancer_data <- function(pat, sub) {
  myurl <- paste0("https://api.cancer.gov/data/", pat, ",", sub)
  cancer_list <- jsonlite::fromJSON(myurl)
  return(cancer_list)
}

```
#### @param, @return, @export 是什麼？
- `@param`: 描述函數的輸入參數
- `@return`: 說明函數回傳的東西
- `@export`: 表示這個函數會被放到 `NAMESPACE`，使用者可以直接呼叫

#### 設定與說明檔案 DESCRIPTION
在創立新的套件位置後，記得改變當前路徑，不然如果要執行`usethis`會抓不到。
```r
setwd(MyPackage)
usethis::use_description(fields = list(
  Title = "Interact with National Cancer Service API",
  Description = "Functions to access the National Cancer Service API.",
  License = "GPL-2",
  Encoding = "UTF-8",
  LazyData = "true"
))
```
或手動修改 `DESCRIPTION` 為：
```r
Package: MyPackage
Type: Package
Title: For teaching purpose
Version: 0.1.0
Authors@R: person("YHD", "Oxford", email = "yhdyhd@gmail.com", role = c("aut", "cre"))
Description: Functions to access the National Weather Service API.
License: GPL-2
Encoding: UTF-8
LazyData: true
Imports:
  httr,
  jsonlite
Suggests:
  rmarkdown,
  knitr,
  testthat (>= 3.0.0)
VignetteBuilder: knitr
```

---
## 使用 devtools 的完整 workflow
#### 加入一個函數
```r
usethis::use_r("my_function")
```
這會在`MyPackage`下`R`這個資料夾裡生成一個檔名為my_function的`.R`檔。就可以開始自定義函數。


#### 文件註解轉成說明檔
```r
devtools::document()
#Console出現: 
#ℹ Updating MyPackage documentation
#ℹ Loading MyPackage
#Writing NAMESPACE
#Writing get_cancer_data.Rd
```
此時會發現新增一個資料夾叫`man`，存放了一個檔案:`get_cancer_data.Rd` (用於 `?get_cancer_data`)。
而`NAMESPACE`這個檔案也被修正了:
```r
# Generated by roxygen2: do not edit by hand

export(get_cancer_data)
```

#### 載入開發中 package
模擬套件安裝後的使用情境，把你目前開發中的函數載入到 R 環境中，不需要重新安裝
- 時機: 開發過程中隨時都可以執行，用來測試函數是否可以正常呼叫
```r
devtools::load_all()
```

#### 檢查 package 是否正確
完整檢查整個 package 是否符合 R 語言套件的規範（語法錯誤、描述檔錯誤、測試錯誤）
- 時機: 發佈前、提交 CRAN 前、或每次重大改動後
```r
devtools::check()
```

#### 建立測試結構
```r
usethis::use_testthat()
```

#### 新增測試檔案
```r
usethis::use_test("get_cancer_data")
```

#### 建立範例教學文件
```r
usethis::use_vignette("intro")
```

#### 安裝本地套件
將開發中的 package 安裝到本地 R 環境中，供其他 project 使用
- 時機: 測試安裝是否正常、打包後安裝
```r
devtools::install()
```
---
## 加入測試
```r
# 建立測試檔 tests/testthat/test-get_cancer_data.R
test_that("get_cancer_data returns a list", {
  result <- get_geo_data(42.440, -76.497)
  expect_type(result, "list")
})
```

## 建立長篇教學 Vignette
編譯 `vignettes/` 內的 .Rmd 教學文檔為 `HTML`，並自動加入到 help 系統中
```r
usethis::use_vignette("MyPackage-intro")
# 然後在 vignettes/MyPackage-intro.Rmd 撰寫教學
```

## 最後：打包與分享你的套件！
```r
devtools::check()
devtools::build()
```
這會產生 `.tar.gz 檔案`，可給他人安裝使用：
```r
install.packages("MyPackage_0.1.0.tar.gz", repos = NULL, type = "source")
```
---
## 推薦使用順序
```r
# Step 1: 編寫函數 + 加上 roxygen2 註解
# Step 2: 轉換成說明文件
devtools::document()

# Step 3: 載入函數到目前 R session（模擬安裝後效果）
devtools::load_all()

# Step 4: 測試函數能否使用
get_cancer_data("123", "lung")

# Step 5: 撰寫或更新測試檔案，並跑測試
# testthat::test_dir("tests/testthat")

# Step 6: 檢查整體 package
devtools::check()

# Step 7: 若測試都通過，可安裝套件
devtools::install()

# Step 8: 若要分享或提交給他人，打包套件
devtools::build()
```

---
## 課程小結
本課程帶你從零開始學會如何建立一個完整的 R 套件，涵蓋函數撰寫、說明文件自動化、測試設計、教學文件撰寫與打包發佈流程，讓你具備將自己的程式模組化、標準化並對外分享的能力，真正踏入專業 R 開發者的領域。
後續建議可進一步學習如何將套件上傳至 `GitHub`、使用 `pkgdown` 建立線上文件網站，或深入瞭解 CRAN 套件提交流程，讓你的作品被更多人使用與引用。