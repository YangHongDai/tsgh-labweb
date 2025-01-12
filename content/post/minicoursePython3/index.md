---
title: 迷你課程:Python-3~Exception
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

```python
x = int(input("What'sx? "))
print(f"x is {x}")
->invalid literal for int()

try:
      x=int(input("What'sx? "))
      print(f"x is {x}")
except ValueError:
      print("x is not an integer")

#ValueError
try:
      x=int(input("What'sx? "))
      print(f"x is {x}")
except ValueError:
      print("x is not an integer")
print(f"x is {x}")
#NameError: name 'x' is not defined 雖然有indent 但是try 裡面的還是在global env 是可以被外面調用的，只是valueError 先發生，所以不會有x 被定義

#else
try:
      x=int(input("What's x? "))
except ValueError:
      print("x is not an integer")
else:
      print(f"x is {x}") # 只有x有值時才會執行


#In a look, with break to deliberately stop
while True:
      try:
            x=int(input("What's x? "))
      except ValueEror:
            print("x is not an integer")
      else:
            break
print(f"x is {x}") 
      

while True:
      try:
            x=int(input("What's x? "))
      except ValueEror:
            print("x is not an integer")
      else:
            print(f"x is {x}") # 會一直問user 不會break

while True:
      try:
           x=int(input("What's x? "))
           break
      except ValueError:
             print("x is not an integer")

print(f"x is {x}")

#Either way is ok

def main():
      x = get_int()
      print(f"x is {x}")

def get_int():
    while True:
      try:
            x=int(input("What's x? "))
      except ValueEror:
            print("x is not an integer")
      else:
            break
      return x



#More tidy version
def get_int():
    while True:
      try:
            x=int(input("What's x? "))
      except ValueEror:
            print("x is not an integer")
      else:
            return x #return has the same function to break


def get_int():
    while True:
      try:
            x=int(input("What's x? "))
      except ValueEror:
            pass # still recognize the error but do nothing

def get_int(prompt):
    while True:
      try:
            return int(input(prompt))
      except ValueEror:
            pass # still recognize the error but do nothing

```