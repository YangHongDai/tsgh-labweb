---
title: 迷你課程:Python-2~函數邏輯與迴圈
date: 2024-12-30
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在這篇教學中，我們將深入探討 Python 中函數的邏輯與迴圈的應用，幫助學習者掌握基本程式設計技巧。課程內容涵蓋條件判斷、函數設計、迴圈使用、資料結構操作等關鍵概念。

---
## 函數的定義與應用
函數是一段可以重複使用的程式碼邏輯，以下是函數的基本用法：
```python
# 主函數範例
def main():
    x = int(input())
    print('The number is', square(x))

def square(n):
    return n * n
```
上述範例中，我們定義了一個 `square` 函數用來計算平方數，並透過 `main` 函數接收輸入。

---
## 條件判斷
條件判斷讓程式能根據不同情況執行對應邏輯。基本條件判斷:
```python
if x < y:
      print('x is smaller than y')
if x > y:
      print('x is larger than y')
if x == y:
      print('x is equal to y')
```
但上面的寫法會讓程式評估`3次 if`，如果是小程式倒還好，但如果是複雜的程式就會影響效能，有沒有更好的方法呢？其實我們可以使用`elif`，這樣只有當if的結果是False時，程式才會往`elif`去運算，因此從上面的3次運算，減少到目前的2-3次。

```python
if x < y:
      print('x is less than y')
elif x > y:
      print('x is larger than y')
elif x == y:
      print('x is equal to y')
```
但似乎還可以再更精簡，因為x如果不是小於y或大於y，那一定是等於y，所以第三個程式邏輯基本上不用運算，在這種狀況下，可以使用`else`：

```python
if x < y:
      print('x is less than y')
elif x > y:
      print('x is larger than y')
else: # 假設x==y 無需再詢問
      print('x is equal to y')
```
接下來再看另外一個例子：
```python
if x<y or x > y:
      print('x is not equal to y')
else:
      print('x is equal to y')

```
上面的語法基本上都沒有錯，但不夠Python，以下是更簡潔的方式：
```python
if x!=y:
      print('x is not equal to y')
else:
      print('x is equal to y')
```
或是：
```python
if x==y:
      print('x  is equal to y')
else:
      print('x is not equal to y') 

```

---
## 範圍判斷
對於成績分級的應用，如果90-100分為Grade A，80-90分為Grade B，70-80分為Grade C，60-70分為Grade D，而小於60分為Grade F，今天希望使用者在輸入一個分數，可以輸出他的成績分級，初步可以寫成：
```python
score = int(input('Score: '))
if score >= 90 and score <=100:
      print('Grade: A')
elif score >= 80 and score <90:
      print('Grade: B')
elif score >=70 and score <80:
      print('Grade: C')
elif score >=60 and score <70:
      print('Grade: D')   
else:
      print('Grade: F')

```
上面的程式利用了`and`來連接兩個邏輯運算式，雖然合理，但這個程式看起來不夠簡潔，接下來該怎麼做呢？Python可以允許範圍的界定如：
```python
if 90<=score<=100:
      print('Grade A')
elif 80<=score<=90:
      print('Grade B')
elif 70<=score<=80:
      print('Grade C')
elif 76<=score<=70:
      print('Grade D')
else:
      print('Grade F')
```
這樣看起來似乎好一點了，但我們不難發現，`elif`只有在`if`運算結果為False時才會開始運算，所以如果輸入的成績如果若在某個數值以上，就必然不會落入較低的分級，因此我們可以簡化成：
```python
if score >=90:
      print('Grade A')
elif score >=80:
      print('Grade B')
elif score >=70:
      print('Grade C')
elif score >=60:
      print('Grade D')
else:
      print('Grade F')
```

---
## 奇偶數判斷函數
定義函數檢查數字是否為偶數，我們可以試著先這樣寫：
```python
def main():
      x = int(input("What's x? "))
      if is_even(x):
            print('Even')
      else:
            print('Odd')

def is_even(n):
      if n % 2 == 0:
            return True
      else:
            return False
```
上面的主程式包含了一個寫好的函式`is_even`，讓主程式更為易讀及簡潔。但`is_even`內部用了一個`if`和兩個`return`，我們是否可以用更簡潔的方式來寫這個副程式？ 其實可以只用一個`return`來返回邏輯值：
```python
def is_even():
      return True if n % 2 == 0 else False
```
但Python是很優雅的語言，我們甚至可以簡單的這麼做：

```python
def is_even():
      return (n % 2 == 0)
```
如此一來，如果 `(n % 2 == 0)` 為True就會直接返回`True`，否則為`False`。

---
## match and case
如果我們的程式需要符合多項條件，可以使用`match`與`case`，例如我們想要區分NBA球員的所屬隊伍：
```python
name = input("Give me the player's name: ")
if name =='Lebron James' or name == 'Bronny James' or name == 'Anthony Davis':
      print('Lakers')
elif name == 'Stephen Curry':
      print('Warriors')
else:
      print('Who?')
```

我們也可以用`match`與`case`：
```python
match name:
      case 'Lebron James'|'Bronny James'|'Anthony Davis':
            print('Lakers')
      case 'Stephen Curry':
            print('Warriors')
      case _:
            print('Who?')
```

## 迴圈的應用
條件式裡面很重要的部分是`迴圈`，了解如何運用迴圈可以增加程式的效率。
## while 迴圈
當迴圈的條件是動態變化或為真與否(True or False)的時候，可以使用while：
```python
i = 1
while i <= 3:
    print('I love Micha!') #我家養的陸龜名字
    i += 1
```
我們可以針對i的值去做運算，來限制`while`的條件，所以上面的程式也可以改成：
```python
while i < 3:
      print('I love Micha!')
      i += 1
```

---
## for 迴圈
當需要遍歷一個序列，如列表、字典、集合、字串等，並且已知迭代次數，可以使用`for 迴圈`：
```python
for i in [0,1,2]:
      print('I love Micha!')
```
但這樣是非常不優雅的做法，在Python裡面，我們可以使用`range()`來幫助迭代：
```python
for i in range(3):
      print('I love Micha!')
```
這邊的`i`其實不重要，針對不重要的參數我們可以用`_`來表示：
```python
for _ in range(3):
      print('I love Micha!')
```

---
## 無限迴圈與中斷條件
```python
while True:
    n = int(input("What's n? "))
    if n < 0:
          continue
    if n > 0:
          break
```
上面為典型的`while`迴圈和`input()`的搭配，用來判斷何時該中斷使用者持續的輸入並做接下來的運算。因為判斷式為`True`，所以正常情況下會是`無限迴圈`，持續詢問`n`的數值，如果不中斷，程式則會持續詢問使用者而不會進行迴圈外的運算，因此需要設定一個條件來`中斷`此`while loop`。而上面的程式可以直接簡化為：
```python
while True:
      n = int(input("what's n? "))
      if n > 0:
            break
```

---
## 迴圈的高效寫法
雖然迴圈看起還比較正式，但如果我們只是想要`重複`某種任務，例如輸出三次字串，其實在Python並不需要用到迴圈，我們可以直接用`*`將我們的目標輸出`乘以`某個數字。
```python
print('Lebron is great!\n' * 3, end="")
```

---
## 資料結構操作
#### 列表 (List)
上面講過，可以搭配`for loop`來遍歷一個列表：
```python
students = ['A', 'B', 'C']
for student in students:
    print(student)
```
```
#>
A
B
C
```
我們也可以搭配`range`於for迴圈中一起使用，但是range需要數字當參數，單純的列表並沒有這種資訊，此時我們可以使用`len()`來將列表裡面元素的數量提取出來：
```python
for i in range(len(students)):
      print(i+1, students[i]) #i+1是為了讓輸出從數字1開始。
```
```
#>
1 A
2 B
3 C
```

#### 字典 (Dictionary)
Python `dictionary` 是一種內建的資料結構，使用`鍵值對（key-value pairs）`的方式來儲存和搜尋資料，字典可以用大括號 `{}` 或 `dict()` 函數來定義。
```python
players = {
    'Lebron James': 'Lakers',
    'Anthony Davis': 'Lakers',
    'Stephen Curry': 'Warriors'
}
print(players['Lebron James']) #字典的值用鍵來取
```
```
#>
Lakers
```
而字典同樣也可以用在for迴圈中：
```python
for player in players:
      print(player) #只有輸出鍵

for player in players:
      print(player, players[player], sep=', ') #輸出鍵與值
```

#### 字典列表
實際狀況下球員的資料很多，上面只能針對鍵去取得一個值，如果我們想要取得球員的其他資料，需要比較結構化的數據結構，如字典列表：
```python
players = [
    {"name": "Lebron James", "team": "Lakers", "height": "206 cm"},
    {"name": "Stephen Curry", "team": "Warriors", "height": "188 cm"}
]
for player in players:
    print(player["name"], player["team"], player["height"], sep=", ")
```
```
#>
Lebron James, Lakers, 206 cm
Stephen Curry, Warriors, 188 cm
```
---
## 繪製方形
#### 使用函數分解邏輯以繪製方形：
我們先來看第一種方式：
```python
def print_square(size):
      for i in range(size):
            for j in range(size):
                  print('#', end="")
            print()
print_square(3)
```
```
#>
###
###
###
```
這種方式需要因為在內部的迴圈中需要修改print()中的`end`參數來讓`#`可以順利依據size來印出來，同時不換行，但是會導致在迴圈外還需要一個print()來做換行的動作，這樣寫起來會比較複雜，閱讀性也較差。我們接著看第二種方式：
```python
def print_square(size):
    for i in range(size):
        print('#' * size)
# 主程式
print_square(3)
```
不要忘了Python允許在print內部對目標任務做相乘，這種寫法更為簡潔易懂。

---
## 課程小結
1. 函數的定義與使用：學習如何透過函數重複利用程式碼，提升程式的可讀性與模組化。
2. 條件判斷的優化：探討 if-elif-else 的邏輯運作，並學習如何簡化條件式判斷。使用範圍運算（<= 和 >=）與邏輯運算符（如 and）提高條件式的精簡性與效能。
3. 迴圈的應用：瞭解 while 與 for 迴圈的差異，並學會選擇適合的迴圈工具。學習如何使用 range() 簡化迴圈以及如何避免不必要的變數。
4. 資料結構操作：探討 列表 和 字典 的基礎操作，包括遍歷與元素操作。認識字典列表的使用，並以結構化數據進行更高效的管理與處理。
5. Python 的優雅性：探討簡潔而 Pythonic 的語法，如列表推導式、條件判斷的簡化、以及使用 match 與 case 替代多重 if 條件。
