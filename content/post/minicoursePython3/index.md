---
title: 迷你課程:Python-3~例外與錯誤處理
date: 2025-01-14
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在 Python 中，處理`異常（Exception）`是一項必備技能，避免在執行時因非預期的錯誤而崩潰。這篇文章將介紹如何使用 try、except、else 和 finally 來有效處理例外情況。

---
## 什麼是異常？
異常是程式執行過程中出現的錯誤。例如，將一個字串轉換為整數時，可能會觸發 ValueError：
```python
x = int(input("What's x? "))
print(f"x is {x}")
# 若輸入非整數，會出現：
# ValueError: invalid literal for int() with base 10
```
為避免這類錯誤導致程式崩潰，我們可以使用 try 和 except 進行處理：
```python
try:
      x = int(input("What's x? "))
      print(f"x is {x}")
except ValueError:
      print("x is not an integer")

```
- try：放置可能出現錯誤的程式碼。
- except：當指定的錯誤發生時，執行這裡的處理邏輯。
所以，如果輸入整數，正常執行。如果輸入非整數，提示錯誤並防止程式崩潰。

---
## 例外處理的範圍與變數作用域
如果在 try 區塊內的變數未成功定義，會導致後續作用域出現錯誤：
```python
try:
      x = int(input("What's x? "))
      print(f"x is {x}")
except ValueError:
      print("x is not an integer")
print(f"x is {x}")
# 若發生 ValueError，則會拋出 NameError，因為 x 沒有被定義。
```
如果輸入不是整數，則x不會有值，下一行的print()就顯得多餘，這種狀況下，可以使用`else`區塊：
```python
try:
      x = int(input("What's x? "))
except ValueError:
      print("x is not an integer")
else:
      print(f"x is {x}")  # 只有 x 被成功賦值時才執行
```
這樣寫就簡潔多了，也沒有多餘的邏輯。

---
## 多次輸入與循環處理
當需要多次嘗試讓用戶提供有效輸入時，可結合 while 和異常處理：
### 使用 break 終止循環
```python
while True:
      try:
            x = int(input("What's x? "))
            break  # 成功輸入時結束循環
      except ValueError:
            print("x is not an integer")
print(f"x is {x}")
```

### 不使用 break 的設計
```python
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x  # return 本身結束函數，相當於 break
```
`return` 本身可以結束函數，相當於 break，所以在回傳值的同時結束回圈。但需要先定義一個`function()`。

---
## 擴展功能：finally 區塊
`finally` 區塊中的程式碼會無條件執行，即使 try 或 except 中發生了錯誤：
```python
try:
      x = int(input("What's x? "))
except ValueError:
      print("x is not an integer")
finally:
      print("This block always executes, no matter what!")

```
用途：釋放資源（如關閉文件或網路連線）。確保某些關鍵程式碼必定執行。

---
## 新增內容：多個異常處理
如果需要處理多種可能的錯誤，可以用多個 except 區塊，或使用`元組`進行匹配：
```python
try:
      x = int(input("What's x? "))
      y = 10 / x
except ValueError:
      print("x is not an integer")
except ZeroDivisionError:
      print("x cannot be zero")

```
而上面多個錯誤的處理可以搭配元組 (tuple)：
```python
try:
      x = int(input("What's x? "))
      y = 10 / x
except (ValueError, ZeroDivisionError) as e:
      print(f"An error occurred: {e}")
```

---
## 小結
異常處理是寫程式的基礎：
1. 使用 `try-except` 來捕捉常見錯誤。
2. 利用`else` 和 `finally` 增強邏輯清晰度和資源管理。
3. 結合循環，確保用戶輸入有效。
4. 多異常捕捉，並與tuple搭配。