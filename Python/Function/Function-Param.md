### 位置参数
计算 [x²]() 的函数：
```python
def power(x):
    return x * x
```
对于[power(x)]()函数，参数x就是一个位置参数。当我们调用[power]()函数时，必须传入有且仅有的一个参数 [x]()：
```python
>>> power(5)
25
>>> power(15)
225
```
计算 [x]() 的任意 [n]() 次方函数：
```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```
对于这个修改后的[power(x, n)]()函数，可以计算任意 [n]() 次方：
```python
>>> power(5, 2)
25
>>> power(5, 3)
125
```
修改后的[power(x, n)]()函数有两个参数： [x]() 和 [n]() ，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数 [x]() 和 [n]() 。

---
### 默认参数
新的[power(x, n)]()函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
```python
>>> power(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: power() missing 1 required positional argument: 'n'
```
这时候，用我们的默认参数。由于我们经常计算 [x²]() ，所以，完全可以把第二个参数 [n]() 的默认值设定为2：
```python
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```
这样，当我们调用[power(5)]()时，相当于调用[power(5, 2)]()：
```python
>>> power(5)
25
>>> power(5, 2)
25
```
定义默认参数要牢记一点：默认参数必须指向不变对象，如 [str]() 、[None]() 这样的不变对象。
