---
title: 迷你課程:Python-11~用「命名空間」把程式變乾淨
date: 2025-09-15
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
- 什麼是命名空間（namespace），為什麼能避免 x 和別人的 x 打架
- Python 找變數的`LEGB `規則
- 模組、類別、物件與屬性都是各自的命名空間
- 避免命名衝突與寫出可維護程式的實務招

---
## 命名空間是什麼？
同名不同姓的概念：每個「作用域或物件」都有自家字典。
1. 模組有自己的名字→ a_module.x
2. 類別/實例有自己的屬性→ obj.x
3. 函式內部有自己的區域變數→ x
好處：你和別人都用 x 也沒關係，各在各家。

## 變數查找順序：LEGB
- L (Local): 函式目前區域
- E (Enclosing): 外層函式（閉包）
- G (Global): 模組層級
- B (Builtin): 內建（如 len, sum）
示例：
```python
x = 'G'                      # Global

def outer():
    x = 'E'                  # Enclosing
    def inner():
        x = 'L'              # Local
        return x
    return inner()

print(outer())               # 'L'
```
上面例子如果你依序移除 x = 'L' 與 x = 'E'，會發現印出來的會從`Enclosing`的`E`到`Global`的`G`。

## 模組與屬性：最常用的命名空間
#### a_module.py
```python
x = 10
def f(): return x

# main.py
import a_module
x = 'mine'
print(x)              # mine
print(a_module.x)     # 10   ← 各在各的命名空間
```
## 屬性（attributes） 就是物件的「自家字典」：
```python
class Book:
    def __init__(self, title): self.title = title

b1 = Book("Zen of Python")
b2 = Book("Fluent Python")
print(b1.title, b2.title)     # 各自獨立的屬性命名空間
```

## 容易誤踩的坑
- from x import *：把別人家的名字通通丟進你家，易撞名。
- 用 import x 或 from x import name1, name2 更安全。
- 覆蓋內建（Builtins）：`不要把變數叫 list, sum, id`。
- 誤用 global / nonlocal：`只在需要修改外層同名變數時才用`。
```python
count = 0
def tick():
    global count #需要改寫外層count的綁定才需要用
    count += 1
```
`包與模組名重疊`：你的檔名若叫 random.py 會遮到標準庫 random。

## 設計建議（把層次疊起來）
1. 模組 → `類別` → 物件：每一層都是命名空間，讓名稱意圖清晰。
2. 善用封裝：把相關函式與資料放進同一類別/模組。
3. `明確前綴`：config.DB_URL、metrics.accuracy 一看就懂來自哪裡。
4. 適度別名：import numpy as np，但避免過度縮寫造成可讀性差。

---
## 快速練習（10 分鐘）
## Q1. 改寫下列程式，避免命名污染與撞名：
```python
from utils import *
from math import *
print(sin(pi/2))
```

參考解答：
```python
import utils
import math
print(math.sin(math.pi/2))
```

## Q2. 讓 make_counter() 回傳能自增的函式，不使用全域變數：
```python
def make_counter():
    count = 0
    def inc():
        # 填寫
        return count
    return inc
```
參考解答：
```python
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

## Q3. 模組 cfg.py 內有 API_KEY，在 main.py 安全存取：
#### main.py
```python
import cfg
print(cfg.API_KEY)   # 用命名空間前綴，避免與本檔變數衝突
```
## 課程小結
1. Namespaces are one honking great idea — let’s do more of those!
2. 用更多、清晰、分層的命名空間（模組/類別/物件/函式）來管理名稱，
讓程式更安全、可讀、好維護。