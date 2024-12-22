---
title: 迷你課程:Python-2~
date: 2024-12-21
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: true
---
<!--more-->

```python

def main():
      x = input()
      print('The number is', square(x))
def square(n):
      return n*n

## Conditionals
if x < y:
      print('x is less than y')
if x > y:
      print()
if x == y:
      print()

to avoid repetetion
use elif
if x < y:
      print('x is less than y')
elif x > y:
      print()
elif x == y:
      print()
#what is the difference? ask less questions, more faster, and more efficient

#Use else
if x < y:
      print('x is less than y')
elif x > y:
      print()
else: # just assume x == y, no need to ask the PC
      print()

# but lengthy
if x<y or x > y:
      print('x is not equal to y')
else:
      print('x is equal to y')
#better one
if x!=y:
      print('x is not equal to y')
else:
      print('x is equal to y')

#or
if x==y:
      print('x  is equal to y')
else:
      print('x is not equal to y')     


#And
score = int(input('Score: '))
if score >= 90 and score <=100:
      print('Grade: A')
elif score >= 80 and score <90:
      print('Grade: B')
elif score >=70 and score <80:
      print('Grade: C')
else:
      print('Grade: F')


if 90<=score<=100:
      print('Grade A')
elif 80<=score<=90:
      print('Grade B')
elif 70<=score<=80:
      print('Grade C')
else:
      print('Grade F')

if score >=90:
      print('Grade A')
elif score >=80:
      print('Grade B')
elif score >=70:
      print('Grade C')
else:
      print('Grade F')

```