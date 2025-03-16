---
title: 迷你課程:Python-6~I/O
date: 2025-02-16
authors: ["戴揚紘", ""]
commentable: true
categories: [Python迷你課程]
tags: [Python,coding]
isCJKLanguage: true
draft: true
---
<!--more-->
## Quick look

```python
names = []
for _ in range(3):
      name = input('What is your name?')
      names.append(name)

for _ in range(3):
      names.append(input('Waht is your name?'))

for name in sorted(names):
      print(f'hello, {name}')

# how do we save the names persistently instead of typing repeatedly?

#open: name of the file and how do we want to open

#similar to double click on files, write something and save files
file = open("names.txt", "w")
file.write(name)
file.close()

# if we run the above program three times, the name will ne overwritten 
file = open("names.txt", "a")
file.write(name)
file.close()

#but this will be NameANameB, whic is we don't want it to be. 






```


