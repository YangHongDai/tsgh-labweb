---
title: 迷你課程:Python-5~Unit tests
date: 2025-02-16
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
## Quick look
本課程將帶你學習 Python 中的單元測試基礎，包括使用標準庫中的 assert 語句、處理異常、以及使用 pytest 框架來進行更進階的測試。

---
## assert, try-except 與 raise 差別
在 Python 程式設計課程中，assert、try-except 和 raise 是用於錯誤處理和程式調試的三種重要工具，它們的作用和使用情境如下：

#### assert
`assert` 用於`設定條件`，確保程式在特定條件下才會繼續執行。`如果條件不成立`，會自動引發 `AssertionError`。常用於測試和確保程式內部狀態`符合預期`。
```python
assert condition, "Error message if condition is not met"
```
#### try-except
`try-except` 用於捕捉和處理異常。程式碼塊放在 `try `裡運行，如果發生異常，則執行 `except` 裡的代碼塊。這對於處理`不可預測的錯誤`（如文件讀取錯誤、數據庫查詢失敗等）非常有用。
```python
try:
    # code that might throw an exception
except SomeException as e:
    # code that runs if an exception occurs
```

#### raise
`raise` 用於主動引發異常，可以在檢測到特定問題時，使程序`主動報錯並中斷`。這是撰寫可靠和可維護程式碼時一種常用技術。
```python
if not type(x) is int:
    raise TypeError("Only integers are allowed")
```
---

## 基本單元測試
功能定義：首先定義一個簡單的功能，比如 square 函數，用於計算數字的平方。
```python
def square(n):
    return n * n
```
使用 `assert` 進行測試：使用 Python 的 assert 關鍵字來確保函數行為正確。
```python
def test_square():
    assert square(2) == 4
    assert square(3) == 9
```

## 錯誤處理
異常捕獲：用 try-except 結構來捕獲並處理測試中可能出現的錯誤。
```python
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
```
## 使用 pytest 框架
- 安裝 pytest：通過命令 pip install pytest 安裝 pytest。
- 編寫測試用例：將測試函數放在獨立的文件中，例如 test_calculator.py。
```python
from calculator import square #首先要先創立一個calculator.py 裡面定義square() 函數
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
```
運行 pytest：在`終端`中運行 `pytest` 命令來執行所有的測試。

## 特別提醒
在自行撰寫module檔案時，如這邊的`calculator`，記得在最底下使用:
```python
if __name__ == '__main__': 
      main()
```      
這是為了確保當檔案被直接執行時，該檔案內的代碼塊才會運行。這個條件判斷的目的是防止該檔案被導入到其他 Python 檔案作為模塊時，裡面的代碼塊被執行。換句話說，這個語句後面的代碼只有在該檔案作為主程序運行時才會執行，因為 `__name__ `在`直接運行文件時`會被設置為 `'__main__'`。而當檔案被其他文件導入時，這部分代碼則不會被執行。這是一個常用的 Python 語法，用來區分檔案直接運行和被導入時的行為。


---
## 課程小結
在這個單元中，你學會了如何使用 Python 進行基本的單元測試，包括如何處理異常並使用 pytest 框架來進行自動化測試。這些技能將幫助你在開發過程中提早發現問題，保證程式碼質量。