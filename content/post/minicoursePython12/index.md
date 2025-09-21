---
title: 迷你課程:Python-12~Magic methods 與 Dunder
date: 2025-09-21
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
什麼是 `Dunder` 和 `Magic methods`?
在 Python 裡，許多內建行為（像是物件建立、相加、字串顯示、長度計算等），其實都是靠一組特殊命名的方法完成的。
這些方法的名字 前後都有兩個底線 `(double underscore, "dunder")`，因此常被稱為 dunder methods 或 magic methods。
舉例：
1. __init__：物件初始化（建構子）
2. __del__：物件刪除（解構子）
3. __add__：定義 + 的行為
4. __len__：定義 len(obj) 的行為
5. __call__：讓物件能像函數一樣被呼叫
這些方法不是你平常直接呼叫的，而是當你執行某些語法時，Python 會自動觸發。

## 建構與解構: __init__ 與 __del__
```python
class Person:
    def __init__(self, name, age):   # 建構子，建立物件時自動呼叫
        self.name = name
        self.age = age
        print(f"{self.name} 被建立了")

    def __del__(self):               # 解構子，物件被刪除時呼叫
        print(f"{self.name} 被刪除了")

p = Person("YHD", 25)   # 自動觸發 __init__
del p                   # 觸發 __del__
```
輸出：
```python
#>>YHD 被建立了
#>>YHD 被刪除了
```
重點：
- __init__ 負責初始化屬性。
- __del__ 通常不常用，但在釋放資源（像是檔案或網路連線）時有用。


## 運算子多載: __add__
我們可以自訂物件在使用 + 時的行為。
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # 定義 v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):         # 定義 print() 時顯示的格式
        return f"X:{self.x}; Y:{self.y}"

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2   # 自動呼叫 __add__
print(v3)      # 自動呼叫 __repr__
```
輸出：
```python
#>> X:60; Y:80
```
重點：
__add__ 讓我們能控制 + 的行為。
__repr__ 決定物件被 print 或在 REPL 顯示時的字串格式。

## 內建函數連動: __len__
讓物件支援 len()：
```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):     # 定義 len(obj) 的行為
        return len(self.items)

nums = MyList([1, 2, 3, 4, 5])
print(len(nums))   # 呼叫 __len__
```
輸出：
```python
#>>5
```
## 可呼叫物件: __call__
讓物件能像函數一樣使用：
```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):   # 讓物件可以直接被呼叫
        print(f"Hello, {self.name}!")

g = Greeter("YHD")
g()   # 呼叫 __call__
```
輸出：
```python
#>>Hello, YHD!
```
應用情境：
模擬函數的物件（例如機器學習模型 model(x) 就是靠 __call__）。

在 PyTorch 裡，nn.Module 已經幫你定義好了 __call__。
它的工作流程大概是這樣：
```python
class Module:
    def __call__(self, *args, **kwargs):
        # 一些前處理（像是 hooks、模式檢查…）
        return self.forward(*args, **kwargs)
```
所以當你寫：
```python
y = model(x)
```
背後實際上就是：
```python
y = model.__call__(x)   # 呼叫 __call__
y = model.forward(x)    # __call__ 內部再去呼叫 forward
```
所以平常只要寫 model(x) 就好，不需要手動調 forward()。

## 常見的 Magic methods
方法	說明
__init__	初始化物件
__del__	銷毀物件
__repr__	print() 或 REPL 顯示
__str__	str(obj) 的輸出（和 __repr__ 不同）
__len__	len(obj)
__getitem__	obj[i] 索引取值
__setitem__	obj[i] = x
__iter__	迭代器支援 (for loop)
__call__	物件可被呼叫
__add__, __sub__, __mul__	運算子多載

---
## 課程小結
Dunder methods (magic methods) 是 Python 的「隱藏 API」，用來定義物件的內建行為。
Python 看到某些語法時（例如 +, len(), print()），會自動去呼叫對應的 dunder 方法。
這讓 Python 非常靈活，我們可以讓自訂的 class 行為和內建型態一樣直觀。
