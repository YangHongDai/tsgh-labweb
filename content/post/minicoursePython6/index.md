---
title: 迷你課程:Python-6~I/O
date: 2025-03-30
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在本次課程中，我們將學習如何使用 Python 處理輸入與輸出（Input/Output, 簡稱 I/O），特別是與文字檔（txt）和 CSV 檔的互動。我們將從基本的文字儲存開始，逐步介紹更靈活的檔案讀寫與資料結構應用，並導入 csv 標準函式庫的操作。

## 使用 input() 收集使用者輸入並儲存
```python
names = []
for _ in range(3):
    name = input("What is your name?")
    names.append(name)

for _ in range(3):
    names.append(input("What is your name?"))

for name in sorted(names):
    print(f"Hello, {name}")
```
上述程式碼示範了如何收集使用者輸入三個名字，將其儲存在列表中，並排序後輸出問候語。
- 問題：每次執行都得重新輸入資料，有沒有辦法「永久儲存」呢？

---
## 基礎文字檔寫入
```python
file = open("names.txt", "w")
file.write(name)
file.close()
```
上述程式碼會建立 names.txt 並寫入「最後輸入的名字」，但注意：

`w` 模式會覆蓋原有檔案內容
若多次執行，只保留最後一次寫入的內容
若希望「追加寫入」而非覆蓋，可以使用 `a` 模式：
```python
file = open("names.txt", "a")
file.write(f"{name}\n")  # 每次新增一行
file.close()
```
---
## 更好的寫法：使用 with 自動關閉檔案
```python
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
```
`with` 區塊會自動在區塊結束時關閉檔案，避免忘記 `file.close()` 而導致檔案損毀或記憶體問題，是良好習慣。

## 讀取檔案內容
```python
with open("names.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("Hello,", line)
```
這段會印出每一行的使用者名字。但因為檔案中每行本身已有 \n，print() 又自帶 \n，因此會產生多餘的空行。
- 解法：使用 `.rstrip()` 移除行尾空白與換行符號
```python
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
```
補充說明：
for line in file: 是逐行讀取檔案內容的 Pythonic 寫法，`等同於 file.readlines()` 的效果，但記憶體效率更好，尤其在處理大型檔案時。

## 排序名稱清單
```python
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
```
這是很常見的模式：

1. 建立清單
2. 將檔案資料逐行加入
3. 移除換行後再排序並輸出

#### 更簡潔的寫法（延伸解釋）
```python
with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")
```
這裡 `sorted(file)` 直接對檔案物件做排序，會在讀取每一行時就進行排序（基於字母順序）。但這種寫法僅適用於`單純排序輸出`，不適合後續操作，因為`沒有保留在變數中`。

---
## CSV 檔案讀取介紹
`CSV（Comma-Separated Values）`是常見的表格式資料儲存方式，適合儲存表格、成績、學生資料等。
```python
with open("name.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```
- .split(",") 會將一行文字依逗號分割成清單
- 可使用`「解包」`技巧直接指派給多個變數

## 使用字典存資料（更具彈性）
```python
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]): #匿名函式更為簡潔，同時告訴sorted()要以哪個參數當作排序標準。
    print(f"{student['name']} is in {student['house']}")
```
為什麼使用字典好？

1. 更清楚每個欄位的意義（比位置索引直觀）
2. 可以根據欄位排序或篩選
3. 欄位順序調整不會影響程式邏輯

---
## 使用 csv 標準函式庫（推薦做法）
```python
import csv

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)  # 自動以第一行為欄位名 所以要先創造:name,home
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
```
優點：

1. 不怕欄位順序調動
2. 更安全地解析有逗號的欄位（如地址）

## 寫入 CSV 檔案
```python
import csv

name = input("What's your name? ")
home = input("Where do you live? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
```
注意：若輸入欄位中有逗號，csv 模組會自動加上雙引號來保護欄位完整性。
#### 使用 csv.DictWriter
```python
import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```
好處：

1. 保證欄位對應正確
2. 即使順序調整，也不會影響資料結構

---
## 課程小結
| 主題           | 重點內容                                                                 |
|----------------|--------------------------------------------------------------------------|
| 📥 使用者輸入   | 使用 `input()` 收集資料並存入 list                                       |
| 📁 檔案寫入     | 使用 `open()` 搭配 `"w"`（覆寫）或 `"a"`（追加）模式將資料寫入文字檔案      |
| 📖 檔案讀取     | 使用 `readlines()` 或 `for line in file` 逐行讀取，搭配 `.rstrip()` 去除換行 |
| 🔠 資料排序     | 使用 `sorted()` 進行排序，搭配 `key`（如 `lambda`）對字典列表排序           |
| 📑 處理 CSV     | 使用 `.split(",")` 或 `csv.reader` / `csv.DictReader` 處理表格資料         |
| 🧱 資料結構應用 | 用 dictionary 儲存每筆資料，增加彈性與可讀性，方便後續排序與分析           |
| ✍️ 寫入 CSV     | 使用 `csv.writer`（列表方式）或 `csv.DictWriter`（字典方式）輸出資料        |
