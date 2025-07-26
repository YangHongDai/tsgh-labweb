---
title: 迷你課程:Python-9~其他好用函式
date: 2025-07-26
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
本課程將深入探討 Python 的進階特性，包括集合操作、函數式編程工具和生成器等強大功能，幫助你寫出更簡潔高效的程式碼。

## 集合(Set)操作
```python
students = [
    {"name":"YHD", "house":"Summertown"},
    {"name":"Mark", "house":"Headington"}
]

# 傳統使用 list 的方法（需手動檢查重複）
houses = []
for student in students:
    if student["house"] not in houses:  # 每次都要檢查是否已存在
        houses.append(student["house"])

# 使用 set 更簡潔（自動處理重複）
houses = set()  # 創建空集合
for student in students:
    houses.add(student["house"])  # 注意：使用 add 而非 append

# 錯誤示範：如果用 append 會報 AttributeError
# houses.append(student["house"])  # 集合沒有 append 方法

for house in sorted(houses):
    print(house)
```
- 集合`自動去重`，無需手動檢查 if student["house"] not in houses
- 查找效率 O(1) 比列表 O(n) 更快
- 語意更明確：當我們需要「不重複集合」時就該用 set

---
## 全局變量與作用域
```python
balance = 0  # 全局變量

def main():
    print('Balance:', balance)
    deposit(100)
    withdraw(50)
    print('Balance:', balance)

def deposit(n):
    global balance  # 必須聲明！
    balance += n  # 沒有 global 會報 UnboundLocalError

def withdraw(n):
    global balance
    balance -= n

main()

```
錯誤解釋：
如果忘記加 `global`：
```python
def deposit(n):
    balance += n  # UnboundLocalError: local variable 'balance' referenced before assignment
```
Python 會認為你想修改局部變量，但發現`還沒定義就使用`。

其實這樣太麻煩，還要定義global，所以其實可以使用class：

```python
class Account:
def __init__(self):
    self._balance = 0 

@property
def balance(self):
    return self._balance
def deposit(self,n):
    return self._balance +=n    
def withdraw(self,n):
    return self._balance -=n  

```
這樣`self._balance`在類別裡面大家都可以取用，透過`self`串接起來。
---

## 類型提示與靜態檢查
```python
def meow(n: int) -> str:
    """產生 n 次喵喵叫
    
    :param n: 喵喵叫次數
    :type n: int
    :raise TypeError: 如果 n 不是整數
    :return: 包含 n 次喵喵叫的字串
    :rtype: str
    """
    return 'meow\n' * n

number: int = int(input('Number: '))
meows: str = meow(number)
print(meows, end='')
```
- 函數參數類型提示 `n: int`: 表示參數 n 應該是一個整數。這只是`提示`，`Python 運行時不會強制檢查`，而使用 `mypy` 等工具可以進行靜態類型檢查
- 返回值類型提示 `-> str`: 表示函數將返回一個`字串`。幫助開發者理解函數的輸出類型
- 變量類型提示 `number: int` 和 `meows: str`: 明確變量應該存儲的數據類型，提高代碼可讀性和可維護性

#### Docstring
`docstring（文件字串`）是 Python 中用來為模組（module）、函數（function）、類別（class）或方法（method）撰寫說明文件的工具。它通常放在定義下方的三引號` """ """ `中。
1. 讓程式碼更易讀、更好維護: 清楚描述函數/模組的目的、參數、回傳值與副作用。對團隊合作與長期專案特別有幫助
2. 開發階段可直接使用 `help()` 查看說明: 使用者或開發者不需要打開原始碼，也能快速了解用途
3. 支援自動化工具生成文件: 如：`Sphinx`、`pdoc`、`mkdocstrings` 可自動抓取 docstring 建立 HTML 或 PDF 文件。提高 API 文件一致性與可維護性

#### 靜態檢查
```python
mypy script.py  # 會檢查類型是否匹配
#如果傳入錯誤類型
meow("3")  # mypy 會警告但程式仍能運行
```
---
## 命令行參數解析
#### 使用sys.argv
```python
import sys

if len(sys.argv)==1:
    print('meow')
elif len(sys.argv)==3 and sys.argv[1]=='-n':
    n = int(sys.argv[2])
    for _ in range(n):
        print('meow')
else:
    print('usage: meows.py')

```

#### 使用argparse
```python
import argparse

# 錯誤處理版本
parser = argparse.ArgumentParser(description='Meow like a cat')
parser.add_argument('-n', default=1, type=int, help='number of times to meow')
args = parser.parse_args()

for _ in range(args.n):
    print('meow')
```
當你從命令列執行 Python 程式時（例如：python script.py -n 3），你可以透過 sys.argv 或 argparse 模組來讀取命令列參數。但它們的設計目標和優勢大不相同。
- sys.argv 是一個 list，包含從命令列輸入的所有字串參數。
- sys.argv[0] 是腳本名稱，其餘是傳入的參數（全部都是字串）。

#### 使用sys.argv缺點
1. `解析複雜`: 你必須手動處理參數的解析與順序，例如 if sys.argv[1] == '-n'
2. `型別轉換需自己處理`: int(sys.argv[2])，若不是數字會拋出錯誤
3. `缺少錯誤訊息說明`: 使用錯誤時只好手動印出 `usage`
4. `無法支援預設值、自動幫助訊息等`

#### 使用 argparse 的優點
1. `自動產生 --help`: 自動顯示參數用法與說明文字
2. `內建型別轉換`: type=int 會自動檢查與轉換型別
3. `自動錯誤處理`: 若參數缺失或格式錯誤，自動印出錯誤訊息與退出
4. `支援預設值`: `default=1` 讓參數可選填
5. `支援多種參數格式`: 支援位置參數、可選參數（-n）、旗標（--verbose）等
6. `文件化與維護性高`: 參數都集中在一個地方，容易擴充與閱讀

```python
parser.add_argument('-n', default=1, help='number of times to meow', type=int)
args = parser.parse_args()
```
這一行的意思是：
- `-n` 是一個選擇性參數（optional argument）
- type=int 代表這個參數需要接一個整數值
- 所以當你輸入 -n 時，argparse 就會`自動期待一個整數跟在後面`


---
## Unpackaging
```python
def total(galleons, sickles, knuts):
    return (galleons*18 + sickles)*30 + knuts

# 列表解包
coins = [100, 25, 50]
print(total(*coins))  # 等同 total(coins[0], coins[1], coins[2])

# 字典解包
coins_dict = {'galleons': 100, 'sickles': 25, 'knuts': 50}
print(total(**coins_dict))  # 鍵名必須匹配參數名

# 常見錯誤：
# print(total(**{'a':100,'b':25,'c':50}))  # TypeError: 參數名不匹配
```

---
## *args, **kwargs
#### *args：可變位置參數
用來接收任意數量的`「位置參數」`（positional arguments），會以 `tuple `形式傳入函數。

#### **kwargs：可變關鍵字參數
用來接收任意數量的`「關鍵字參數」`（keyword arguments），會以 `dict` 形式傳入函數。
```python
def f(*args, **kwargs):
    print('Positional:' args)

f(100,50,25,5)
```
接收幾個input arguments 都可以

```python
def f(*args, **kwargs):
    print('Keyword:' kwargs)

f(galleons=100,sickles=50,knuts=25)
#Keyword: {'galleons': 100, 'sickles': 50, 'knuts': 25}
```
#### 注意事項
- *args 一定要放在普通參數之後
- **kwargs 一定要放在 *args 之後
- 傳入參數時位置不能亂：普通參數 → *args → **kwargs
```python
def good(a, *args, **kwargs):
    pass

def bad(*args, a, **kwargs):  # ❌ 錯誤：位置參數不能在 *args 後面
    pass
```

---
## 函數式編程工具
#### map 與 filter
#### map(function, iterable)
對 iterable 中的每一個元素，套用 function，然後回傳一個新的迭代器。
這個迭代器包含了每次執行 function(元素) 的結果。
#### 範例一
```python
students = [
    {"name":"Ron", "house": "Gryffindor"},
    {"name":"Draco", "house": "Slytherin"}
]

names = map(lambda s: s["name"].upper(), students)
print(*names)  # 輸出: RON DRACO
```
#### 範例二
```python
def main():
    yell('This', 'is', 'CS50')

def yell(*words):
    uppercased = map(str.upper, words) #調用str.upper 不要用()因為目前沒有要直接呼叫
    print(*uppercased)
```

#### filter(function, iterable)
對 iterable 中的每一個元素，執行 function。
如果 function(元素) 回傳 `True`，就保留這個元素，否則丟掉。
回傳一個新的迭代器，`只包含被保留的元素`。
```python
# filter 範例
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
print(list(gryffindors))  # 轉為列表顯示
```
這樣得到的 names 或 gryffindors 其實是個 `lazy iterator（惰性迭代器）`，這有幾個特性:
1. `不會立刻執行`: map / filter 不會立即處理資料，而是等你真正「取用」的時候才一個一個執行
2. `一次性`: 你只能「走訪」一次，走過的元素就消失了（記憶體優化的結果）
3. `要轉為 list 或使用迴圈`: 否則你看不到裡面的結果

```python
names = map(lambda s: s["name"], students)
print(list(names))  # ['Ron', 'Draco']
print(list(names))  # [] -> 第二次就沒東西了！
```

---
## List comprehension and dict comprehension
```python
# 列表推導式（等價於 map）
uppercased = [s["name"].upper() for s in students]

# 字典推導式
house_dict = {s["name"]: s["house"] for s in students}

# 帶條件的推導式（等價於 filter + map）
gryffindor_names = [s["name"] for s in students if s["house"] == "Gryffindor"]
```
---
## 生成器(Generator)
生成器是一種特殊的函數，使用 `yield` 逐步產生值，每次呼叫都會記住當前狀態，不會一次性全部執行完畢。
```python
def star_generator(n):
    """生成星號金字塔"""
    for i in range(n):
        yield '*' * i  # 每次產生一個值

# 使用方式
for line in star_generator(5):
    print(line)
```
優點：
1. 記憶體效能高（惰性求值 lazy evaluation）
2. 適合處理大量資料或無限序列

#### 對比
使用 return：一次回傳全部 → 會佔用大量記憶體
```python
def main():
    n = 10
    for i in star(n):
        print(i)

def star(n):
    total = []
    for i in range(n):
        total.append('*' * i)
    return total  # 一次回傳所有值

main()
```
改用 yield：逐個產生 → 節省資源、可控性強
```python
def main():
    n = 10
    for i in star(n):
        print(i)

def star(n):
    for i in range(n):
        yield '*' * i  # 一次回傳一個

main()
```

#### 常見錯誤：將 yield 寫成 return
```python
def star(n):
    for i in range(n):
        return '*' * i  # ❌ 錯誤：只會執行一次，i=0 就直接 return

main()
```
---
## 課程小結
本課程涵蓋了 Python 的多個進階特性：
1. 集合操作：使用 set 處理不重複元素
2. 作用域管理：理解 global 關鍵字和更好的封裝方式
3. 類型提示：提升程式碼可讀性和可維護性
4. 命令行參數：使用 argparse 創建專業 CLI 工具
5. unpacking操作：靈活處理序列和字典
6. 函數式編程：map, filter 和推導式
7. 生成器：高效處理大型數據集