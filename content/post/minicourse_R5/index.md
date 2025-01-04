---
title: 迷你課程:R語言-5~R的字串操作
date: 2024-12-15
authors: ["戴揚紘", ""]
commentable: true
categories: [R語言迷你課程]
tags: [R, coding]
isCJKLanguage: true
draft: false
---
<!--more-->

## Quick look
本次課程將介紹 R 語言中與**字串**相關的各種操作方法，包括字串的建立、分割、拼接、取子字串、查找與替換，以及字串的轉換與處理。

R 中的字串屬於 `character` 類型，是一種重要的資料結構，特別是在文字處理、資料清理與分析中經常使用。

---
## 字串的建立

在 R 中，字串用雙引號 `""` 或單引號 `''` 建立：

```r
# 建立字串
str1 <- "Hello, World!"
str2 <- 'R is powerful!'

# 查看字串類型
class(str1)  # 輸出: "character"
```

若需包含雙引號或單引號，可以用反斜槓 `\` 進行跳脫：
```r
str3 <- "He said, \"R is amazing!\""
print(str3)
# 輸出: He said, "R is amazing!"
```

---
## 字串的基本操作

### 1. **拼接字串**
使用 `paste()` 和 `paste0()` 函數來拼接字串：
- `paste()`: 會自動加入分隔符（預設為空格）
- `paste0()`: 不加入任何分隔符

```r
# 拼接字串
first_name <- "James"
last_name <- "Dai"

full_name <- paste(first_name, last_name)
print(full_name)  # 輸出: "James Dai"

# 無分隔符拼接
full_name_no_space <- paste0(first_name, last_name)
print(full_name_no_space)  # 輸出: "JamesDai"
```

### 2. **字串長度**
使用 `nchar()` 函數計算字串的長度：
```r
nchar(full_name)  # 輸出: 9
```

### 3. **取子字串**
使用 `substr()` 和 `substring()` 提取字串的特定部分：

```r
# 提取子字串
substr(full_name, 1, 5)  # 從第1個字元到第5個字元
# 輸出: "James"

# substring 的用法
substring(full_name, 7)  # 從第7個字元開始到結尾
# 輸出: "Dai"
```

---
## 字串的分割
使用 `strsplit()` 函數根據指定分隔符分割字串：

```r
# 分割字串
sentence <- "apple,banana,cherry"
words <- strsplit(sentence, ",")
print(words[[1]])
# 輸出: "apple" "banana" "cherry"
```

> 注意：`strsplit()` 返回的是一個列表，因此要用 `[[1]]` 提取結果。

### 使用 `tidyverse` 的 `separate()` 分割資料框中的字串
如果有多筆名字資料，`tidyverse` 提供了一個方便的函數 `separate()` 來分割字串，並將其拆分成多個欄位：

```r
library(tidyverse)

# 建立資料框
name_data <- tibble(full_name = c("James Dai", "Anna Smith", "John Doe"))

# 使用 separate 分割 full_name 欄位
name_data <- name_data %>% 
  separate(full_name, into = c("first_name", "last_name"), sep = " ")

# 查看結果
print(name_data)
```

**輸出結果**：
```
# A tibble: 3 x 2
  first_name last_name
  <chr>      <chr>    
1 James      Dai      
2 Anna       Smith    
3 John       Doe      
```

---
## 字串的查找與替換

### 1. **查找特定字串**
使用 `grep()` 或 `grepl()` 來查找字串：
- `grep()`: 返回匹配的索引位置
- `grepl()`: 返回布林值向量

```r
# 查找字串
fruits <- c("apple", "banana", "cherry")
index <- grep("apple", fruits)
print(index)  # 輸出: 1

contains_apple <- grepl("apple", fruits)
print(contains_apple)  # 輸出: TRUE FALSE FALSE
```

### 2. **替換字串**
使用 `gsub()` 和 `sub()` 進行字串替換：
- `gsub()`: 替換所有匹配的字串
- `sub()`: 只替換第一個匹配的字串

```r
# 替換字串
text <- "I love R. R is amazing!"

new_text <- gsub("R", "Python", text)
print(new_text)  # 輸出: "I love Python. Python is amazing!"
```

---
## 字串的類型轉換 (Coercion)

在 R 中，當不同類型的資料組合時，R 會自動進行 `coercion`（類型強制轉換）。字串會被視為**最高類型**，並將其他資料類型轉換成 `character`。

```r
# 自動轉換
mixed_vec <- c("R", 1, TRUE)
print(mixed_vec)
# 輸出: "R" "1" "TRUE"

# 手動轉換
num_to_char <- as.character(123)
print(num_to_char)  # 輸出: "123"

char_to_num <- as.numeric("123")
print(char_to_num)  # 輸出: 123
```

---
## 字串與 S4 物件的轉換
對於複雜結構的物件，可以使用 `as()` 進行轉換：

```r
# 使用 as 進行轉換
s4_object <- as(c("x", "y", "z"), "character")
print(s4_object)
# 輸出: "x" "y" "z"
```

---
## 課程小結

| 操作類型           | 函數名稱                | 範例                                   |
|--------------------|-------------------------|----------------------------------------|
| 字串拼接           | `paste()`, `paste0()`  | `paste("James", "Dai")`               |
| 取字串長度         | `nchar()`              | `nchar("James")`                      |
| 提取子字串         | `substr()`, `substring()` | `substr("James", 1, 3)`               |
| 分割字串           | `strsplit()`, `separate()` | `strsplit("a,b,c", ",")`             |
| 查找字串           | `grep()`, `grepl()`    | `grep("apple", fruits)`               |
| 替換字串           | `gsub()`, `sub()`      | `gsub("R", "Python", text)`          |
| 類型轉換           | `as.character()`, `as.numeric()` | `as.character(123)`           |

掌握這些字串操作技巧，將能有效地處理各種文字資料，並在資料分析、清洗與視覺化過程中發揮重要作用！
