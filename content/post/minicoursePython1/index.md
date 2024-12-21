---
title: 迷你課程:Python-1~字串操作與格式化
date: 2024-12-21
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在 Python 中，字串 (string) 是最常用的資料類型之一。掌握字串的基本操作和進階技巧，不僅能讓你的程式碼更簡潔，也能提升程式設計的靈活性。本文將基於範例程式碼進一步詳細講解，並延伸至更多實用的字串操作和格式化方法。

---
## 輸出
```python
print("Hello, World!")
```
這是 Python 中最基本的輸出語句，用於在terminal (終端) 顯示文字。

---
## 字串格式化
Python 3.6 版之後引入`f-string`的格式化方式，語法簡潔易懂。
```python
name = "Micha"
print(f"Hello, {name}!") 
```
---
## 格式化數字
可以針對一串數字中間加逗號，對一些需要這樣處理的數字很方便。
```python
z = 1234567
print(f"{z:,}")  # 輸出: 1,234,567
```

---
## 保留小數位數
```python
z = 1234.56789
print(f"{z:.2f}")  # 輸出: 1234.57
```

---
## 跳脫字符
```python
print("She said, \"Hello!\"")  # 使用 \\ 處理雙引號
```

```
#>>>
She said, "Hello!"
```

---
## 活用print()
要輸出的字可以在print()內用`+`號來結合：
```python
print('Hello'+'Micha') 
```
```
#>>>
HelloMicha
```
但我們發現到兩個字串連在一起，這是因為`+`會默認中間沒有空格，所以這樣的情況下應該要：
```python
print('Hello '+'Micha') 
```

如果不要用`+`，可以直接使用`,`，這樣就不會默認中間沒有空格：
```python
print('Hello','Micha') ##輸出Hello Micha
```

當然，我們可以在print()內修改參數，讓上面的輸出沒有空格：
```python
print('Hello','Micha', sep='') ##輸出HelloMicha
```
這是因為print() default中設定sep=' '，所以平時用逗號分割時中間會有空格。

---
## 換行
如果我們希望Micha出現在下一行該怎麼做？
第一種最簡單的做法：
```python
print('Hello')
print('Micha')
```
這是因為print() default 會有一個參數`end = '\n'`，所以只要每一行都輸入print()，輸出就會分行。但這樣會增加代碼的行數，如果我們想要縮成一行該怎麼做？可以在中間插入`\n`。
```python
print('Hello \nMicha') #輸出會跟上面一樣
```
---
## 使用者輸入
使用 `input()` 函數接受使用者輸入：
```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```
萬一使用者不小心輸入多餘的空格，我們可以用`strip()`來處理：
```python
name = name.strip()  # 去除前後空白
```

---
## 輸入字母大寫
可以針對輸入的字串做大寫轉換：
```python
name = "micha"
print(name.capitalize()) #輸出Micha
```
但如果想要輸入的多個字串都大小開頭，需要使用`title()`：
```python
name = "micha wu"
print(name.title()) #輸出Micha Wu
```

---
## 整合處理
```python
name = input("What's your name? ").strip().title()
print(f"Hello, {name}!")
```

---
## 自串分割
分割字串： 使用 `split()` 方法將字串分割為多個部分：
```python
full_name = "Micha Wu"
first, last = full_name.split(" ")
print(first)  # 輸出: Micha
print(last)   # 輸出: Wu
```
---

## 合併字串
使用 `join() `方法將列表中的元素合併為字串：
```python
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)  # 輸出: Hello World
```

## 替換字串
```python
text = "I love Micha!"
print(text.replace("Micha", "Red Bean"))  # 輸出: I love Red Bean!
```

---
## 搜尋字串
```python
text = "I love Micha!"
print(text.find("Micha"))  # 輸出: 7 (Micha 的起始位置)
```

## 其他搭配
字串的操作還可以搭配`isdigit()`、`isalpha()`、`isspace()`等，讓字串的操作更為靈活。

---
## 課程小結
| **功能**                 | **操作方法**                                        | **範例**                                                                                     | **輸出**                   |
|--------------------------|---------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------|
| **基本輸出**             | `print()`                                         | `print("Hello, World!")`                                                                   | `Hello, World!`            |
| **格式化字串**           | f-string                                          | `name = "Micha"`<br>`print(f"Hello, {name}!")`                                            | `Hello, Micha!`            |
| **數字加逗號**           | f-string 加千分位分隔符                             | `z = 1234567`<br>`print(f"{z:,}")`                                                        | `1,234,567`                |
| **保留小數位數**         | f-string 保留小數點後兩位                          | `z = 1234.56789`<br>`print(f"{z:.2f}")`                                                   | `1234.57`                  |
| **跳脫字符**             | 使用 `\` 處理特殊字符                               | `print("She said, \"Hello!\"")`                                                           | `She said, "Hello!"`       |
| **字串拼接**             | `+` 或 `,` 進行字串拼接                             | `print('Hello '+'Micha')`<br>`print('Hello', 'Micha')`                                    | `Hello Micha`              |
| **字串合併**             | `join()`                                          | `words = ["Hello", "World"]`<br>`sentence = " ".join(words)`<br>`print(sentence)`          | `Hello World`              |
| **換行輸出**             | `\n` 或多次 `print()`                              | `print('Hello \nMicha')`                                                                  | `Hello`<br>`Micha`         |
| **用戶輸入**             | `input()`                                         | `name = input("What's your name? ")`<br>`print(f"Hello, {name}!")`                        | 根據使用者輸入             |
| **去除空白**             | `strip()`                                         | `name = " Micha "`<br>`print(name.strip())`                                               | `Micha`                    |
| **首字母大寫**           | `capitalize()`                                    | `name = "micha"`<br>`print(name.capitalize())`                                            | `Micha`                    |
| **標題格式化**           | `title()`                                         | `name = "micha wu"`<br>`print(name.title())`                                              | `Micha Wu`                 |
| **分割字串**             | `split()`                                         | `full_name = "Micha Wu"`<br>`first, last = full_name.split(" ")`                           | `Micha` 和 `Wu`            |
| **替換字串**             | `replace()`                                       | `text = "I love Micha!"`<br>`print(text.replace("Micha", "Red Bean"))`                    | `I love Red Bean!`         |
| **搜尋字串**             | `find()`                                          | `text = "I love Micha!"`<br>`print(text.find("Micha"))`                                   | `7`                        |
| **檢查字串內容**         | `isdigit()`, `isalpha()`, `isspace()`              | `s = "12345"`<br>`print(s.isdigit())`                                                     | `True`                     |
| **整合處理**             | `strip() + title()`                               | `name = input("What's your name? ").strip().title()`<br>`print(f"Hello, {name}!")`        | 格式化的用戶輸入結果       |
