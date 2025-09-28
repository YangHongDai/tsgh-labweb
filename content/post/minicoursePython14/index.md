---
title: 迷你課程:Python-14~Decorators
date: 2025-09-21
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
def mydecorator(function):

      def wrapper():
            print('I am a decorator')
            function()

      return wrapper
def hello_world():
      print('Hello world')

mydecorator(hello_world)()

 
def mydecorator(function):

      def wrapper():
            print('I am a decorator')
            #function()

      return wrapper
def hello_world():
      print('Hello world')

mydecorator(hello_world)()
##> only print 'I am a decorator'
```
因為mydecorator()是回傳wrapper 而沒有call 因此要再加()

```python
def mydecorator(function):

      def wrapper():
            print('I am a decorator')
            function()

      return wrapper

@mydecorator
def hello_world():
      print('Hello world')

hello_word()
```
會得到一樣結果

```python
def mydecorator(function):

      def wrapper():
            print('I am a decorator')
            function()

      return wrapper

@mydecorator
def hello_world(person):
      print(f'Hello {person}')

hello_word()

```
這樣會出錯，因為wrapper 並不允許輸入，但hello_world可以，可以這樣做

```python
def mydecorator(function):

      def wrapper(*args, **kargs):
            print('I am a decorator')
            function(*args, **kargs)

      return wrapper

@mydecorator
def hello_world(person):
      print(f'Hello {person}')

hello_word('YHD')

```


## 實際範例


