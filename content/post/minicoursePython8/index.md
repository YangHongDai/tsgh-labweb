---
title: 迷你課程:Python-8~Object-oriented programming
date: 2025-06-20
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
在本週課程中，我們將重心從程序式編程轉向物件導向程式設計`（Object-Oriented Programming, OOP）`。透過一連串實例，我們學會如何定義`類別（Class）`、建立`物件（Object）`、使用建構子 __init__ 初始化屬性，以及如何透過 @property、@classmethod、@staticmethod 等語法增強類別的彈性與安全性。我們也學習如何利用繼承（Inheritance）來延伸既有類別功能，以及使用`運算子多載（Operator Overloading）`讓自訂物件支援直覺的運算邏輯如 + 或 ==。

## 程序式 vs. 物件導向
在前幾週，我們以程序式的方式撰寫程式碼，逐步執行每個指令。​例如：​
```python
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
```
我們可以透過定義函式來抽象化部分程式碼：​

```python
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()
```
進一步地，我們可以使用 tuple、list 或 dict 來結構化資料：​

```python
def get_student():
    return {"name": input("Name: "), "house": input("House: ")}
```
然而，這些方法在資料的封裝和操作上仍有侷限。​

---

#### 缺乏結構：資料與行為是分離的
當我們用 dict、tuple、list 來表示一個「學生」的資料時：
```python
student = {"name": "Harry", "house": "Gryffindor"}
```
這只是單純的資料，它本身沒有任何行為。所有操作都要另外寫函式，例如：
```python
def print_student(student):
    print(f"{student['name']} from {student['house']}")
```
缺點：
- 程式碼分散、不直觀。
- 缺乏`「資料 + 邏輯」`的組合。
- 資料錯誤容易發生（例如拼錯 key 名稱）。

#### 難以控制資料的正確性與一致性
使用 dict 時，`沒有強制機制要求一定要有 name 和 house`，也無法`限制它們的類型`：
```python
student = {"name": 123, "house": None}  # 不合理但不會報錯 因為不會先對輸入做評估
```
缺點：
- 無法驗證資料格式。
- 錯誤往往在執行中才發現，難以除錯。

#### 程式可讀性與可維護性差
當程式邏輯變複雜，你會發現所有資料與操作都分散在全域變數與函式裡，變得難以追蹤與維護。

#### 缺乏擴充性與重用性
如果我們想表示不只是學生，還有教授、助教等，不使用類別的話，每種資料型態都要用不同格式管理，非常麻煩。而透過類別與繼承，我們可以統一處理並擴充。

因此，我們引入了物件導向（Object-oriented programming）的概念。​

## 定義類別與建立物件
我們可以定義一個 Student 類別，並建立其物件：​

```python
class Student:
   ...

   def main():
         student = get_student()
         print(f"{student.name} from {student.house}")

   def get_student():
         student = Student() #初始化Student object 的實例 （instance）
         student.name = input("Name: ")
         student.house = input("House: ")
         return student

   if __name__ == "__main__":
         main()
```
在這裡，Student 是一個`類別（Class）`，而 student 是其物件（Object）。​我們使用`點記法（dot notation）來存取物件的屬性`。​

實務上，我們可以用一個constructor來初始化物件的所有特性

## 建構子（Constructor）
我們可以使用 __init__ 方法來初始化物件的屬性：​

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```
這樣，在建立物件時就可以直接指定屬性：​
```python
student = Student("Harry", "Gryffindor")
```
因為考慮到屬性name與house要存放在哪，因此設計了`self`來當做存放的位點。
- `__new__()`:會在class建立實例時呼叫，創造一個空間for存放記憶體，而__init__()會在instance創建後才會呼叫。


## Error 處理
針對屬性的輸入，class也可以在__init__()內做處理。例如：
```python
class Student:
    def __init__(self, name, house):
        if not name:
              raise ValueError('Missing name')
        self.name = name
        self.house = house
```
雖然我們與可以在`def get_student()` 內用try/except來捕捉錯誤，但無法確切知道問題錯在哪。
所以這邊建議使用`raise`：
- `raise`: 主動檢查丟出錯誤，適合在初始化或定義method中驗證輸入並終止程式，強迫使用者修正。
- `try-except`: 被動捕捉錯誤，適合處理可能出錯但不一定是預期錯誤的情況，也就是會讓錯誤靜靜發生，實際錯誤會被掩蓋。

## __str__意義
如果在class內定義一個__str__()，可以在類別物件實例化時被print()呼叫。
```python
class Student:
    def __init__(self, name, house):
        if not name:
              raise ValueError('Missing name')
        self.name = name
        self.house = house
    def __str__(self):
          return 'Hello'
```
當我們執行`print(instance_obj)`時，就會呼叫`instance_obj.__str__()`，印出`Hello`。
如果沒有定義__str__()，會使用__repr__()來替代，如果也沒有定義，才會印出物件所在記憶體位置。

---

## Properties
```python
class Student:
    def __init__(self, name, house):
        if not name:
              raise ValueError('Missing name')
        self.name = name
        self.house = house
    #Getter
    def house(self):
          return self.house
    #Setter
    def house(self, house):
          self.house = house      

```
如果我們想要在設定屬性後，評估屬性是否符合規定或是重新設定時，該如何做呢？我們可以初步寫成上面的樣子。
這個寫法看起來像是定義 getter 與 setter，也就是利用getter取得類別資訊，使用setter來設定資訊，但實際上會有幾個非常嚴重的錯誤問題！

#### 問題一：方法名稱和屬性名稱「重名」會造成遞迴錯誤
若定義了這樣的 setter：
```python
def house(self, house):
    self.house = house  # ⚠️ 這行會造成無限遞迴
```
當你執行 `self.house = house` 時，Python 其實會嘗試呼叫 `self.house()` 方法本身，因為 house 這個名字既是方法又是屬性，結果會導致 遞迴呼叫 house() → house() → 無限遞迴 → 崩潰


#### 這樣寫其實根本不是「正確的 getter/setter 寫法」

想定義 getter/setter，應該用 Python 提供的 `@property` 語法，否則根本沒有效果。

應該這樣寫：
```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self._house = house  # 用底線開頭表示「私有屬性」

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
```
如果這邊不用私有屬性，就會觸發@property機制，導致無限遞迴，所以還是建議使用前綴。


```python
s = Student("Harry", "Gryffindor")
print(s.house)      # ✅ 呼叫 getter，自動執行 house()
s.house = "Hufflepuff"  # ✅ 呼叫 setter，自動執行 house(house)
```
---
## 類別方法與靜態方法
有時，我們希望將某些功能與類別本身相關，而非特定物件。​這時可以使用 `@classmethod` 和 `@staticmethod` 裝飾器：​
```python
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        import random
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")
```
- `@classmethod` 是 Python 中的一種`方法裝飾器`。 被 @classmethod 裝飾的方法 不是操作某個特定實例（instance），而是`操作整個類別（class）本身`。也就是不用每次都實例化一個Hat，只為了操作Hat.sort()。
- 它的第一個參數 不是 self，而是 cls，代表 class 本身，因為不用實例化，所以要和self區分。

`Hat.sort("Harry")`這個方法`不需要建立 Hat 物件，就可以直接使用`，它從類別屬性 houses 中隨機選一個學院，把傳入的 name 分類到該學院。透過 cls.houses，可以取用 class 層級的資料，而非特定某個帽子物件的資料。另外`houses`需要從self.houses獨立出來，這樣才會有已知的變數可以取用，而不需要依賴實例化。

再看一下以下例子：
```python
class Student:
   ...


   @classmethod
   def get(cls):
       name = input("Name: ")
       house = input("House: ")
       return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
        main()

```
原本我們將get_student()寫在class外面，並沒有錯，但是這個跟student有關的操作如果包裹在`Student`這個類別裡會更好閱讀。
裡面的`cls(name, house)`等同於`Student(name, house)`，這表示你打算呼叫類別來建立一個新物件（也就是「實例化」）。

因此，這表示你的 Student 類別應該有一個 `__init__` 方法，像這樣：
```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```
當你呼叫 cls(name, house)，其實就等於呼叫 Student(name, house) 來建立一個新學生物件。

#### 使用 @classmethod 的主要目的與情境
1. `操作 class 屬性`: 當你要使用或修改「類別變數」（非實例變數）時
2. `工廠方法（factory method)`: 建立特定規則的實例（如：from_config 等）
3. `不依賴實例`: 方法跟某個物件狀態無關，只依賴類別資訊
4. `建立可擴充設計`: 子類別可以覆寫 cls 行為，保有彈性

```python
 @staticmethod
    def static_method():           # 靜態方法
        return "Hi!"      
```
`@staticmethod`不操作 self / cls，純功能方法。

---
## 繼承（Inheritance）
繼承允許我們建立一個類別，並繼承另一個類別的屬性和方法，這樣就可以避免重複冗長但相同的程式。
```python
class Wizard: #因為都是巫師，所以這個類別可以被繼承。
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
```
在這裡，Student 和 Professor 類別繼承自 Wizard 類別，並擴展了各自特有的屬性。​


## 運算子多載（Operator Overloading）
假設我們在設計一個哈利波特世界的金庫系統，每個金庫可以存放：

- Galleons（金加隆）
- Sickles（銀西可）
- Knuts（銅納特）
我們可以定義Vault class：​
```python
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
```

`Vault` 類別封裝了這三個屬性。當你想把兩個金庫的錢加起來時，很自然地想寫：

```python
potter = Vault(100,50,20)
weasley = Value(25,40,25)
total = potter + weasley
```
如果沒定義 __add__，你會得到這樣的錯誤：
```python
TypeError: unsupported operand type(s) for +: 'Vault' and 'Vault'

```
#### 加入 __add__ 後的行為
你就讓 + 對 Vault 類別變得有意義了。這樣就可以進行：
```python
def __add__(self, other):
    return Vault(
        self.galleons + other.galleons,
        self.sickles + other.sickles,
        self.knuts + other.knuts
    )
potter = Vault(10, 20, 30)
weasley = Vault(5, 10, 15)
total = potter + weasley
print(total.galleons, total.sickles, total.knuts)  # 15 30 45
```
當你寫 potter + weasley 時，Python 會自動嘗試呼叫 potter.__add__(weasley)。這種機制稱為`運算子多載（Operator Overloading）`，可以讓你`自訂類別在使用像 +、-、* 等運算子時的行為`。


#### 額外建議：加上 __repr__ 方法，方便印出
```python
def __repr__(self):
    return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

print(total)  # 15 Galleons, 30 Sickles, 45 Knuts
```
運算子可以是任何物件，只要定義好即可。其他可以當作operator overload 的運算子包括：__sub__、__mul__、__eq__
、__lt__、__str__、__repr__。


---
## OOP 解決了什麼？
1. 封裝（Encapsulation）： 把資料與操作打包在一起，用方法控制資料操作。
2. 驗證與限制： 透過建構子或 @property 保證資料有效。
3. 重用（Reuse）： 使用繼承機制擴充原有邏輯。
4. 模組化與維護性高： 每個類別功能明確，容易擴充、修改、除錯。

---
## 課程小結
透過這次的物件導向課程，我們體會到使用類別的好處不僅在於程式碼的組織結構更清晰，更重要的是它讓資料與行為可以緊密結合，強化了資料的一致性與邏輯的封裝性。我們從基本的類別設計開始，逐步導入建構子與錯誤處理，再學會如何控制屬性的存取與驗證，進而理解類別方法與靜態方法的應用場景。透過繼承，我們能輕鬆擴展既有邏輯，而運算子多載則讓我們能為類別打造自然直觀的使用體驗。整體而言，OOP 讓我們能設計出更具彈性、可讀性高且容易維護的程式，這將成為日後進行大型專案或跨模組合作時不可或缺的技能。