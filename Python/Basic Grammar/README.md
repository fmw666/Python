# ⚡Python基础
*这是一个快捷目录栏*
+ [数据类型和变量](#Python 数据类型)

+ [使用list和tuple](#)

+ [条件判断](#)

+ [循环](#)

+ [使用dict和set](#)

---

# Python 数据类型
+ 整数
+ 浮点数
+ 字符串

  [字符串]()是以单引号`'`或双引号`"`括起来的任意文本，比如`'abc'`，`"xyz"`等等。
  ```python
  >>>print('abc')
  abc
  >>>print("xyz")
  xyz
  ```
  转义字符 [\\]() 可以转义很多字符，比如 [\n]() 表示换行， [\t]() 表示制表符，字符 [\\]() 本身也要转义，所以 [\\\\]() 表示的字符就是 [\\]()
  ```python
  >>>print('\\')
  \
  >>>print('\\\\')
  \\
  ```
  如果字符串里面有很多字符都需要转义，就需要加很多 [\\]() ，为了简化，[Python]()还允许用 [r' ']() 表示 [' ']() 内部的字符串默认不转义:
  ```python
  >>>print('\\\t\\')
  \       \
  >>>print(r'\\\t\\')
  \\\t\\
  ```
  如果字符串内部有很多换行，用 [\n]() 写在一行里不好阅读，为了简化，[Python]()允许用 ['''...''']() 的格式表示多行内容:
  ```python
  >>>print('''line1
  line2
  line3''')
  line1
  line2
  line3
  ```
+ 布尔值

  一个布尔值只有[True]()、[False]()两种值，要么是[True]()，要么是[False]()，在[Python]()中，可以直接用[True]()、[False]()表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
  ```python
  >>>True
  True
  >>>False
  False
  >>>print(True)
  True
  >>>3 > 2
  True
  >>>print(3 > 5)
  False
  ```
  布尔值可以用[and与]()、[or或]()和[not非]()运算。
  ```python
  >>>True and True
  True
  >>>True and False
  False
  >>>False and False
  False
  >>>2 > 1 and 3 > 1
  True
  >>> True or True
  True
  >>> True or False
  True
  >>> False or False
  False
  >>> 5 > 3 or 1 > 3
  True
  >>> not True
  False
  >>> not False
  True
  >>> not 1 > 2
  True
  ```
+ 空值

  空值是[Python]()里一个特殊的值，用[None]()表示。[None]()不能理解为[0]()，因为[0]()是有意义的，而[None]()是一个特殊的空值。
---
## 变量
变量可以是任意数据类型，在程序中，变量用其变量名表示。变量名必须是大小写英文、数字和`_`的组合，且不能用数字开头，比如：
```python
>>>a = 1  #变量a是一个整数
>>>name_1 = 'fmw'  #变量name_1是一个字符串
>>>Flag = True  #变量Flag是一个布尔值True
```
等号 [=]() 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：
```python
>>>a = 123  #变量a是一个整数
>>>a = 'abc'  #变量a变为字符串
```
---
## 常量
通常用全部大写的变量名表示
```python
>>>PI = 3.14
```
除法 [/]() :
```python
>>>10 / 3
3.3333333333333335
```
 [/]() 除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
```python
>>>9 / 3
3.0
``` 
除法 [//]() ,计算结果为整数部分:
```python
>>>9 // 3
3
>>>10 // 3
3
```
求余 [%]() :
```python
>>>9 % 3
0
>>>10 % 3
1
```
<br>

[返回目录>>](#Python基础)

---
<br>



