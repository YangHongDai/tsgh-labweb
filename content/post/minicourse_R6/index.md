---
title: 迷你課程:R語言-5~輸入與輸出
date: 2025-01-04
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
今天介紹R語言中讀取和寫入資料的工具，包括讀取不同格式的資料模式，並使用寫入輸出來儲存和顯示資料。這部分將輸出更多實用示例與深入解釋。

## Input 讀取資料
#### 主要讀取函數
R 提供了一系列讀取資料的方法：
1. read.table: 讀入行列形式的資料

2. read.csv: 用於 CSV 格式讀取資料，默認 header = TRUE

3. read_delim/read_csv: 定義於readr 套件中，可以在tidyverse 環境中建立tibble。

```r
#read.table
cancer_patients <- read.table("../datasets/cancer_patients.csv", sep=",", header=TRUE)
head(cancer_patients)

# read.csv 讀取 CSV 資料
lung_cancer <- read.csv("../datasets/lung_cancer.csv")
head(lung_cancer)

# readr包含的讀取方法
library(readr)
immunotherapy_tibble <- read_csv("../datasets/immunotherapy_tibble.csv")
print(immunotherapy_tibble)
```

---
## R專屬資料格式
與matlab或其他程式語言類似，R的生態也有自己的數據格式，如`.RData`與`.rds`，用來儲存壓縮後的R物件。
`.RData` 是一種可以存儲多個 R 物件的檔案格式:
- 多物件儲存：可以同時儲存多個物件，例如向量、數據框、列表、函數等。
- 無需指定變數名稱：使用 load() 函數加載 .RData 檔案時，檔案內的物件會直接被還原到工作環境中。
- 會覆蓋同名物件：如果工作空間中已有名稱相同的物件，load() 會覆蓋它們。
- 壓縮儲存：預設使用壓縮技術減少檔案大小。

#### .RData 讀取
```r
# 儲存多個物件到 .RData
x <- 1:10
y <- matrix(1:9, 3, 3)
save(x, y, file = "example.RData")

# 加載 .RData
load("example.RData")

# 確認工作空間物件
ls()
```
`.rds` 是一種用於儲存單一 R 物件的檔案格式:
- 僅支持單一物件：一次只能儲存一個物件，這使得它的用途更具針對性。
- 必須明確指定變數：使用 readRDS() 加載 .rds 檔案時，必須將物件指定給某個變數。
- 不覆蓋現有物件：因為需要明確分配變數名稱，因此避免了意外覆蓋現有物件的風險。
- 壓縮儲存：與 .RData 類似，使用壓縮技術減少檔案大小。

#### .rds 讀取
```r
# 儲存單一物件到 .rds
x <- 1:10
saveRDS(x, file = "example.rds")

# 加載 .rds
x_loaded <- readRDS("example.rds")

# 檢查內容
print(x_loaded)
```

---
## Output 輸出
最間單的輸出方式是使用print()，print() 是最基本的輸出方法，將物件顯示在控制台。在 loop 和 function 中，常需要呼叫 print 來將結果輸出。
```r
# 在 loop 中輸出
for(j in 1:3) { 
    print(my_list) 
}

# 在 function 中輸出
prints_something <- function() {
    print(my_list)
    return(NULL)
}
prints_something()
```
此外，print()也是一種通用函數 (generic function)，意思是它會根據物件的`類別 (class)`，調用對應的特定方法。例如，print.data.frame 是專門用於顯示資料框的 print 方法。
當呼叫 print(x) 時，R 會檢查物件 x 的類別，然後執行 print.<class> 方法。可以用以下方式來查看 print() 方法列表：
```r
# 查看 `print` 方法列表
methods(print)
```
```
#>
[1] "print,ANY-method"           
[2] "print,CFunc-method"         
[3] "print,CFuncList-method"     
[4] "print,diagonalMatrix-method"
[5] "print,sparseMatrix-method"  
[6] "print.aareg"   
```
#### 通用函數運作機制
R 會檢查物件的類別 (class)。根據類別選擇對應的 print.<class> 方法。若沒有定義專屬方法，則使用預設的 `print.default`。

#### S3系統
`S3` 是 R 的三種`物件導向系統`之一（其他為 `S4` 和 `R6`）。它使用非常簡單的方式為物件`指定類別並定義方法`。定義一個新的方法很簡單，只需`創建一個函數`，命名格式為 `generic.class`（例如 print.diagmat）。
一旦方法被定義，`對應類別`的物件會自動使用這個方法。接下來來為print定義新方法：
```r
print.diagmat <- function(d) {
  # 顯示一個對角矩陣，對角線元素由 `d` 決定
  print(diag(x = d))
}
```
然後再將物件轉換為自訂類別
```r
d <- 1:10
class(d) <- "diagmat"
```
原本 `d` 是一個普通的 `atomic vector`，透過 `class(d) <- "diagmat" `指定其類別為 "diagmat"。
此時，d 將使用 `print.diagmat 方法`。

```r
print(d)
```
R 檢查 d 的類別為 "diagmat"。呼叫對應的 print.diagmat 方法。生成並顯示對角矩陣：
```
#>
[,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9] [,10]
[1,]    1    0    0    0    0    0    0    0    0     0
[2,]    0    2    0    0    0    0    0    0    0     0
...
```
---
## 使用cat
print 與 cat 的差別：
1. `print` 是通用函數，適合顯示 R 的物件（如數據框、向量等），並`自動換行`。
2. `cat` 用於`直接將文字輸出到控制台`，且`不自動換行`，需要手動使用 `\n` 加入換行符號。

```r
print("Hello, darkness, my old friend")
cat("Hello, darkness, my old friend")
cat("Hello, darkness, my old friend\n")
cat("Hello, darkness, my old friend\nI've come to talk with you again\n")
cat("\nHello, darkness, my old friend\nI've come to talk with you again\n\n")
```
#### cat常與字串操作函數結合
```r
first <- "YangHong"
last <- "Dai"
paste(first, last)            # "YangHong Dai"
paste0(first, last)           # "YangHongDai"
paste0(first, " ", last)      # " YangHong Dai"
paste(last, first, sep = ", ") # "Dai, YangHong"
cat(paste(first, last, "\n\n")) # "YangHong, Dai"
```
---
## 使用 sprintf 進行格式化輸出
`sprintf` 函數提供了高度靈活的文字格式化功能，可用於生成具特定格式的字串。
```r
first <- "YangHong"
last <- "Dai"

sprintf("%s %s\n", first, last)          # "YangHong Dai"
sprintf("%s    %s\n", first, last)       # "YangHong    Dai"（多個空格）
sprintf("%10s %8s\n", first, last)       # 將名字與姓氏各自右對齊，固定寬度
sprintf("%10s %10s\n", first, last)      # 名字與姓氏各占 10 個字符寬度
```
- `%s`：表示插入字串。
- `%10s`：表示插入字串並右對齊，固定寬度為 10。
- `\n`：換行符號。

#### 處理向量和回收 (Recycling)
`sprintf` 支援向量運算，當第一個向量的長度大於第二個時，短的向量會自動重複。
```r
first <- c("YangHong", "James", "Curry")
last <- "Dai"

sprintf("%s %s\n", first, last)         # 依次組合向量的值
cat(sprintf("%s %s\n", first, last))    # 直接輸出結果到控制台
cat(sprintf("%10s %10s\n", first, last))# 固定寬度的格式化輸出
```
```
#>
[1] "YangHong Dai\n" "James Dai\n"   
[3] "Curry Dai\n"   

YangHong Dai
 James Dai
 Curry Dai

  YangHong        Dai
      James        Dai
      Curry        Dai
```
#### 複雜字符串組合
sprintf 可以處理多個不同類型的參數，像整數（%d）、浮點數（%f）等。
```r
first <- "YangHong"
last <- "Dai"
num <- 4
team <- "Los Angelos Lakers"

sprintf("%s %s won %d NBA championships with the %s.\n", first, last, num, team)
cat(sprintf("%s %s won %d NBA championships with the %s.\n", first, last, num, team))
```
```
#>
YangHong Dai won 4 NBA championships with the Los Angelos Lakers.
```
#### 格式化浮點數
```r
pct <- 62.7

cat(sprintf("%s %s compated %f%% of his passes.\n", first, last, pct))  # 六位小數
cat(sprintf("%s %s compated %4.1f%% of his passes.\n", first, last, pct))  # 固定 1 位小數
cat(sprintf("%s %s compated %8.1f%% of his passes.\n", first, last, pct))  # 寬度 8，1 位小數
cat(sprintf("%s %s compated %4.2f%% of his passes.\n", first, last, pct))  # 固定 2 位小數
```
- `%%`：表示插入百分號 %。

#### 合併多行輸出為單一字串
```r
sprintf("%s %s\n", first, last)                             # 每行單獨輸出
cat(sprintf("%s %s\n", first, last))                        # 直接顯示輸出
paste(sprintf("%s %s", first, last), collapse = " || ")   # 合併成單一字串
```
```
#>
"YangHong Dai || James Dai || Curry Dai"
```
---

## 課程小結
| **功能**            | **函數/方法**             | **特性**                                                                                  | **範例**                                              |
|---------------------|---------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------|
| **資料讀取**        | `read.table`             | 讀入行列形式的資料，需指定分隔符號與表頭                                                 | `read.table("file.csv", sep=",", header=TRUE)`       |
|                     | `read.csv`               | 預設分隔符為逗號，表頭默認為 `TRUE`                                                     | `read.csv("file.csv")`                               |
|                     | `read_delim`/`read_csv`  | 使用於 `tidyverse`，輸出為 `tibble` 格式                                                 | `read_csv("file.csv")`                               |
| **專屬格式讀取**    | `.RData`                 | 支援多物件存取，使用 `save` 儲存，`load` 加載                                            | `save(x, y, file="data.RData"); load("data.RData")`  |
|                     | `.rds`                   | 單物件存取，需指定變數，使用 `saveRDS` 和 `readRDS`                                      | `saveRDS(x, file="data.rds"); readRDS("data.rds")`   |
| **資料輸出**        | `write.csv`              | 將數據框保存為 CSV 格式，選擇是否包含行名                                                | `write.csv(data, file="output.csv", row.names=FALSE)` |
|                     | `save`                   | 儲存多個物件為 `.RData` 格式                                                            | `save(x, y, file="data.RData")`                     |
|                     | `saveRDS`                | 儲存單一物件為 `.rds` 格式                                                              | `saveRDS(x, file="data.rds")`                       |
| **文字輸出**        | `print`                  | 通用函數，適合顯示物件，自動換行                                                        | `print(object)`                                      |
|                     | `cat`                    | 將文字輸出至控制台，無自動換行，需手動指定 `\n`                                          | `cat("Hello\n")`                                     |
|                     | `paste`/`paste0`         | 合併字串，`paste` 默認空格分隔，`paste0` 不使用分隔符                                    | `paste("A", "B", sep=", ")`                         |
|                     | `sprintf`                | 格式化輸出，支援字串（%s）、整數（%d）、浮點數（%f）                                     | `sprintf("%s %d", "Value:", 10)`                    |
| **向量與回收機制**  | `sprintf`                | 支援向量操作，當向量長度不一致時自動回收                                                | `sprintf("%s %d", c("A", "B"), 10)`                 |
|                     | `paste`/`collapse`       | 合併多行輸出為單一字串，指定分隔符號                                                    | `paste(values, collapse=" || ")`                    |
| **S3 方法與類別**   | 自定義方法               | 使用 `generic.class` 命名格式，為物件定義專屬方法                                        | `print.diagmat <- function(x){...}`                 |
|                     | `class`                  | 指定物件類別以啟用專屬方法                                                              | `class(x) <- "diagmat"`                              |
|                     | `methods`                | 查看通用函數的所有專屬方法                                                              | `methods(print)`                                     |
| **進階格式化輸出**  | `sprintf`                | 支援格式化字串，右對齊（%10s）、小數位數（%.2f）、百分號（%%）                           | `sprintf("%10s %.2f%%", "Value", 12.34)`            |