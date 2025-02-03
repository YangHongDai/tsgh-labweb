---
title: 迷你課程:Python-4~模組匯入與 sys 模組基礎教學
date: 2025-02-03
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
Python 有很豐富的資料庫可以匯入函式，幫助處理各種問題，而在寫完Python script 後，我們可以在command line 做測試接收參數，而這個功能仰賴`sys`模組的匯入，今天我們就來簡單講一下模組的匯入與sys模組的使用。

---
## 如何匯入模組
Python 擁有強大的標準函式庫，讓你可以輕鬆解決各種任務。匯入模組的方法主要有兩種：
1. 直接匯入整個模組
```python
import random
# 隨機選擇 'heads' 或 'tails'
coin = random.choice(['heads', 'tails'])
print(coin)
```
- 優點：程式碼可讀性高，明確知道 choice 來自 random 模組。
- 使用場景：當你需要`多個` random 模組的功能時。

2. 匯入特定函式
```python
from random import choice
# 直接使用 choice，而不需加上模組名稱
coin = choice(['heads', 'tails'])
print(coin)
```
- 優點：程式碼更簡潔。
- 注意：當不同模組有相同名稱的函式時，可能會造成命名衝突。


#### 隨機模組運用範例
```python
import random

cards = ['jack', 'queen', 'king']
random.shuffle(cards)  # 隨機打亂牌組
print(cards)

for card in cards:
    print(card)
```

---
## sys 模組：與命令列互動
`sys` 模組讓你可以從`命令列`傳遞`參數`到 Python 程式中。例如:
```python
import sys
print("Hello, my name is", sys.argv[1])
```
請注意:
`sys.argv` 是一個`列表`：
- sys.argv[0]：程式本身的檔案名稱。
- sys.argv[1]：第一個輸入參數。

#### 範例
```python
python script.py Alice
```
```
#>
Hello, my name is Alice
```
---
## 加入錯誤處理
錯誤處理：避免 `IndexError`
```python
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```
此時如果沒輸入參數，會顯示錯誤訊息而程式並不會因此而崩潰。

## 增強版：輸入參數的檢查
```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])
```
`sys.exit()`：當輸入不正確時，直接結束程式，並輸出錯誤訊息。

##  處理多個參數
```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
```
#### 範例
```python
python script.py Alice Bob Charlie
# 輸出：
# Hello, my name is Alice
# Hello, my name is Bob
# Hello, my name is Charlie
```
---

## 導入路徑管理
```python
import sys

# 查看模組搜索路徑
print("當前搜索路徑：", sys.path)

# 添加自定義路徑
sys.path.append("/my/custom/path")
```

## 系統參數訪問
```python
# 關鍵系統參數
print("Python版本：", sys.version)       # 3.10.6 (main...)  
print("作業系統：", sys.platform)       # win32/linux/darwin  
print("預設編碼：", sys.getdefaultencoding())  # utf-8
```

## 進階參數驗證
```python
def parse_args():
    if len(sys.argv) != 4:
        sys.exit("用法: python script.py <模式> <輸入路徑> <輸出路徑>")
    
    valid_modes = {'encode', 'decode'}
    mode = sys.argv[1]
    
    if mode not in valid_modes:
        sys.exit(f"無效模式！可用模式: {', '.join(valid_modes)}")
    
    return {
        'mode': mode,
        'input': sys.argv[2],
        'output': sys.argv[3]
    }

config = parse_args()
print(f"執行模式：{config['mode']}")
```
上面的parse_args()做了幾件事：
1. 先用if條件式確認參數輸入是否有為三個參數，因為第0個參數是檔名本身，因此長度會需要加上1。如果不是，則跳出並印出用法提醒。
2. 如果通過if條件式，接者看輸入的模式是否有效，若不存在則跳出並印出模式無效之提醒。
3. 若通過上述條件式，則返回有效的參數資料以供後續初始化。


## 課程小結
1. 模組匯入：使用 import 或 from ... import ...。
2. sys.argv：處理命令列輸入參數。
3. sys.exit()：在遇到錯誤時結束程式，避免程式繼續執行。


