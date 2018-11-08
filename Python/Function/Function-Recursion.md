### 递归函数
在函数内部，可以调用其他函数。*如果一个函数在内部调用自身本身，这个函数就是递归函数。*

计算阶乘`n! = 1 x 2 x 3 x ... x n`，用函数[fact(n)]()表示:<br>
`fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n`
```python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```
```python
>>> fact(1)
1
>>> fact(5)
120
```
递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

> **注意：** 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（[stack]()）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
```python
>>> fact(1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in fact
  ...
  File "<stdin>", line 4, in fact
RuntimeError: maximum recursion depth exceeded in comparison
```
