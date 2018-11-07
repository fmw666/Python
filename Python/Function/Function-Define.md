### 定义函数
在[Python]()中，定义一个函数要使用[def]()语句，依次写出函数名、括号、括号中的参数和冒号[:]()，然后，在缩进块中编写函数体，函数的返回值用[return]()语句返回,也可以没有返回，在函数最后自动[return None]()。
```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```
```python
>>> print(my_abs(-99))
99
```
如果你已经把my_abs()的函数定义保存为a.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用`from a import my_abs`来导入[my_abs()]()函数，注意a是文件名（不含.py扩展名）：
```python
>>> from a import my_abs 
>>> my_abs(-9)                                          │
9
```
---
### 空函数
如果想定义一个什么事也不做的空函数，可以用 [pass]() 语句：
```python
def nop():
    pass
```
[pass]() 语句什么都不做，相当于一个占位符。比如现在还没想好怎么写函数的代码，就可以先放一个 [pass]()，让代码能运行起来。
```python
if age >= 18:
    pass
```
缺少了 [pass]()，代码运行就会有语法错误。

---
### 返回多个值
函数可以返回多个值，比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
```
> `import math`语句表示导入[math]()包，并允许后续代码引用[math]()包里的[sin]()、[cos]()等函数。

然后，我们就可以同时获得返回值：
```python
>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x, y)
151.96152422706632 70.0
```
但其实这只是一种假象，[Python]()函数返回的仍然是单一值：
```python
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```
其实函数返回值是一个[tuple]()！但是，在语法上，返回一个[tuple]()可以省略括号，而多个变量可以同时接收一个[tuple]()，按位置赋给对应的值，所以，[Python]()的函数返回多值其实就是返回一个[tuple]()，但写起来更方便。
