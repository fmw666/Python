## Python 输入和输出
### Python 中文编码
如果在运行[Python]()程序中，出现以下错误提示：
```python
SyntaxError: Non-ASCII character '\xe4' in file test.py on line 2, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
```
则未指定编码，需要在文件开头添加`#coding=utf-8`

> 对于[VS code]()，在界面右下角中选择编码[UTF-8]()
---
### Python 输出
```python
>>>print('hello,world')
```
[print()]()函数可以接受多个字符串（字符串用一对`''`或者`""`表示），用逗号`,`或者加号`+`隔开，不过逗号在输出中相当于空格，加号则直接连接：
```python
>>>print('hello','world')
hello world
>>>print('hello'+'world')
helloworld
```
[print()]()函数可以用于打印常数，或作计算
```python
>>>print(100)
100
>>>print(1 + 1.1)
2.1
```
---
### Python 输入
```python
>>>name = input()
fmw
```
当出现[input()]()函数以后，命令行会等待用户输入一串字符，此时用户输入的字符串将保留在[name]()变量中。
```python
>>>name
'fmw'
>>>print(name)
fmw
```
当然，为了增加用户交互体验，我们可以
```python
>>>name = input('Please input your name:')
Please input your name:fmw
>>>print('hello',name)
hello fmw
```
