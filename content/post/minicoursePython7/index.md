---
title: 迷你課程:Python-7~Regular expression
date: 2025-04-15
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: false
---
<!--more-->
## Quick look
本課程將帶你從最基礎的 email 驗證出發，循序漸進學會 Python 中強大的正規表示式（Regular Expression, regex）工具。透過實作與範例，你將掌握字串判斷、樣式比對、資訊擷取與清洗技巧，並學會使用 re.findall()、re.split()、re.sub() 等核心函式，有效處理像是 email、網址、Twitter 帳號、姓名等實際應用場景。

---
## 什麼是正規表示式？
正規表示式是一種用來描述字串模式的語言，適用於資料驗證、搜尋與替換。

## Email 驗證與字串切割
```python
email = input("What's your email? ").strip()
if '@' in email:
    print("Valid")
else:
    print("Invalid")
```
- 判斷是否包含 @ 符號。
- 補充：這種方式很基本，但無法判斷完整格式是否正確，例如 a@b、@.、@... 仍會被視為合法。

## 切割字串
```python
user, domain = email.split("@")
if user and '.' in domain:
    print("Valid")
else:
    print("Invalid")
```
- split("@") 將 email 切割成使用者與網域。
- 判斷 domain 是否含有 .。
缺點：@.仍合法

---
## 進階驗證：使用正規表示式
```python
import re
```
Python 中專門處理正規表示式的標準函式庫。

- re.match()：從字串開頭開始比對。
- re.search()：整個字串中尋找符合的模式。

## regex pattern 的語法
- `.`: 任意一個字元（除換行）
- `*`: 0 或多次
- `+`: 1 或多次
- `?`: 0 或 1 次
- `{m,n}`: m 到 n 次
- `\w`: 任意英文字母、數字或底線
- `\d`: 數字
- `\s`: 空白
- `[^@]`: 非 @ 的任一字元
- `^`: 開頭
- `$`: 結尾
- `A|B`: A或B
- `(...)`: a group
- `(?:...)`: non-capturing version，在return 數值時不會回傳在此括號內的表達式。

---
## 檢查是否為 .edu 結尾的信箱
```python
if user and domain.endswith(".edu"):
    print("Valid")
```

## 使用 regex 驗證
```python
import re
if re.search(".*@.*", email):
    print("Valid")
```
上面表示@的左右兩邊出現任何字元0次或0次以上都可，因此abc@ 也是valid的。

```python
import re
if re.search(".+@.+", email):
    print("Valid")
```
這邊`.+`與`..*`實際上是同義，因為`.+`表示左邊必定只少有一字元，而`..*`多一個`.`可以確保在`.*`允許0個字元的情況下，至少有一個字元，因此同義。
如果想要確保要match到`.edu`，我們或許可以這樣做：
```python
if re.search(".+@.+.edu", email):
    print("Valid")
```
但這樣會使得@?edu也是可以接受的email，為什麼呢？因為`.`在這邊並不表示`.`，而需要改成`\.`。
```python
if re.search(r".+@.+\.edu$", email):
    print("Valid")
```
這邊前面的`r`表示raw string，意為原始字串，會告訴Python不要把""裡面的`\`當成是跳脫字元，
- $ 表示字串結尾，不希望.edu後面有任何字串。

---
## 允許特定的字元出現
`[]`在regular expression 具有特別意義，表示字元的集合，所以`[a-z]`表示英文小寫a-z的集合。
若要包括所有email允許的字元，可以這麼寫: `[a-zA-Z0-9_]`，注意中間都不用空格。
另外`[^]`表示除了...以外的集合，所以`[^@]`就表示任何字元但除了@以外。所以上面可以改成：
```python
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
```
或是
```python
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
```
但其實上面還是稍嫌複雜，我們其實可以簡化成：
```python
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
```
因為`\w`就表示word character，所以可以取代`[a-zA-Z0-9_]`。

---
## 大小寫判斷
如果要忽略使用者輸入的大小寫，要怎麼做呢？re提供了一個參數: `re.IGNORECASE`，讓re在做matching 時可以忽律大小寫:
```python
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
```

## 多個subdomains
我們在填寫email時，很多時候不像@gmail.com或@hotmail.com那麼簡單，而是有包含多個subdomains，例如@stx.ox.ac.uk，如果要允許@後面有多個`.`時該怎麼做呢？
不難發現一個subdomain包含`XXX.`，這種形式可以有多個，也可以完全沒有，只剩主domain，所以我們可以把他grouping起來，然後允許他可以`選擇性`的出現。所以我們可以用到`()`與`?`：
```python
if re.search(r"^\w+@(\w\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
```

---
## 姓名matching 
```python
import re
matches = re.search(r"^(.+), (.+)$", name)
```
記住有`()`的才會被捕捉。
```python
matches = re.search(r"^(.+), (.+)$", name)
last = matches.group(1)
first = matches.group(2)
name = last + ", " + first
```
---
## 捕捉twitter 帳號使用者名稱

```python
url = input("URL: ").strip()
match = re.search(r"^https?://(www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE)
if match:
    print("username:", match.group(2))

```
- https?：接受 http 或 https
- (www\.)?：www. 可有可無
- ([a-zA-Z0-9_]+)：Twitter 使用者名稱可包含字母、數字與底線

---
## 其他函式
#### re.findall(pattern, string)
從字串中「找出所有符合 pattern 的子字串」，並以 list 的形式回傳。
```python
import re

text = "My phone number is 0912-345-678, office is 02-1234-5678"
numbers = re.findall(r"\d{2,4}-\d{3,4}-\d{3,4}", text)
print(numbers)
```
```python
>>>
['0912-345-678', '02-1234-5678']
```
- \d{2,4}：代表 2 到 4 位數的數字
- 若 pattern 中有括號 ()，findall 只會回傳群組內容，不是整段。

```python
text = "My emails are alice@mail.com and bob@example.org"
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
print(emails)
# ➜ ['alice@mail.com', 'bob@example.org']
```
- \b 代表 單字邊界（word boundary)，確保 email 是一個獨立單位，不會卡在一個大字串裡面。也就是若出現`@XXX.com123`則會返回`@XXX.com`。


#### re.split(pattern, string)
以符合 pattern 的地方切割字串，回傳一個 list。
```python
text = "apple, orange; banana,pear"
fruits = re.split(r"[,;]\s*", text)
print(fruits)
```
```python
>>>
['apple', 'orange', 'banana', 'pear']
```
- [,;]：逗號或分號都可以作為切割點
- \s*：允許切割點後方有 0 或多個空白

#### re.sub(pattern, repl, string)
將字串中符合 pattern 的部分取代成 repl 的內容，回傳新的字串。
```python
text = "Visit my website at http://example.com or https://example.org"
new_text = re.sub(r"https?://[^\s]+", "[LINK]", text)
print(new_text)
```
- https?://：比對 http 或 https
- [^\s]+：非空白字元 1 次以上（即網址本體）

---
## 課程小結
本課程帶你從字串邏輯判斷到正規表示式應用，逐步掌握：
- Email格式驗證技巧：從簡單的 @ 判斷，到使用 regex 精準比對 .edu 結尾及子網域。
- Regex語法掌握：學會 \w, \d, ^, $, [abc], [^abc] 等關鍵語法，能快速針對輸入進行格式驗證。
- 群組擷取與非擷取群組：學會使用 group() 擷取需要的內容，以及如何使用 (?:...) 建立非擷取群組。
這些技巧廣泛應用於 資料前處理（Preprocessing）、網頁爬蟲（Web scraping）、表單驗證（Form validation） 等領域。
