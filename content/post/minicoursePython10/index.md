---
title: 迷你課程:Python-10~Python 迭代器 (Iterator) 與生成器 (Generator)
date: 2025-09-14
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在處理大量資料或需要串流運算時，如果你單純使用 list 或一次性讀入資料，往往會遇到 記憶體不足 (memory bloat) 或 運算效率低 的問題。
Python 提供的 Iterator (迭代器) 與 Generator (生成器)，能讓你在程式設計中「邊計算、邊取資料」，大幅減少資源消耗。

## 為什麼需要 Iterator？
傳統 list 操作一次載入所有元素，對小資料沒問題，但對大規模資料會浪費記憶體。
Iterator 則允許 一次只取一個元素。
```python
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
```
與一次讀完所有元素相比，Iterator 只在需要時才抓下一個。

## 自訂 Iterator — __iter__ 與 __next__
你可以透過 __iter__ 與 __next__ 自訂迭代器：
```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for num in Countdown(5):
    print(num)  # 5,4,3,2,1
```
StopIteration 代表迭代結束。

## Generator 與 yield
寫完整的 Iterator class 很麻煩。
Generator 則只需用 函式 + yield：
```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown(5):
    print(num)
```
簡潔、易懂，而且自動處理狀態保存。
## 實戰案例 — 串流讀取檔案
```python
def stream_logs(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for log in stream_logs("server.log"):
    print(log)
```
好處：不用一次載入幾 GB 的 log，只需逐行處理。
## Generator 組合成 Pipeline
像 Unix 管線一樣，把生成器串接起來：
```python
def read_numbers():
    for i in range(1, 10):
        yield i

def square(numbers):
    for n in numbers:
        yield n * n

def even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

nums = even(square(read_numbers()))
print(list(nums))  # [4, 16, 36, 64]
```
資料流式處理，不需建大清單。

## 無窮序列 (Infinite Streams)
生成器可用於模擬無窮資料流，例如 IoT 感測器：
```python
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

for i in infinite_counter():
    if i > 5:
        break
    print(i)
```
## Generator 表達式
快速生成大量資料流，不耗記憶體：
```python
squares = (x * x for x in range(1000000))
print(next(squares))  # 0
print(next(squares))  # 1
第八章：itertools 標準庫
Python 內建的 itertools 模組提供了許多強大的工具：
from itertools import islice, groupby

nums = range(10)
print(list(islice(nums, 5)))  # [0, 1, 2, 3, 4]

data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))  # 分組
```
---
## 實戰守則
- 大資料集 → 用 Generator
- 需要即時計算 → 用 Iterator
- 需要模組化數據處理 → 用 Generator pipeline
- 需要進階技巧 → 用 itertools

---
## 課程總結
Iterator 與 Generator 是 Python 高效能資料處理的基礎。
透過 yield 與 itertools，可以打造強大的資料流處理 pipeline。
學會這些技巧，你的程式能更 省記憶體、更模組化、更優雅。