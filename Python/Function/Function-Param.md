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
定义默认参数要牢记一点：默认参数必须指向不变对象，如 [str]() 、[None]() 这样的不变对象。**我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。**

---
### 可变参数
可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

给定一组数字a，b，c……，计算a2 + b2 + c2 + ……

由于参数个数不确定，我们首先想到可以把a，b，c……作为一个[list]()或[tuple]()传进来:
```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
但是调用的时候，需要先组装出一个[list]()或[tuple]()：
```python
>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
```
如果利用可变参数，调用函数的方式可以简化成这样：
```python
>>> calc(1, 2, 3)
14
>>> calc(1, 3, 5, 7)
84
```
所以，我们把函数的参数改为可变参数：
```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
定义可变参数和定义一个[list]()或[tuple]()参数相比，仅仅在参数前面加了一个 [\*]() 号。在函数内部，参数numbers接收到的是一个[tuple]()，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
```python
>>> calc(1, 2)
5
>>> calc()
0
```
如果已经有一个[list]()或者[tuple]()，要调用一个可变参数怎么办？可以这样做：
```python
>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
```
这种写法当然是可行的，问题是太繁琐，所以[Python]()允许你在[list]()或[tuple]()前面加一个 [\*]() 号，把[list]()或[tuple]()的元素变成可变参数传进去：
```python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```
> `\*nums`表示把`nums`这个[list]()的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
---
### 关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个[tuple]()。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个[dict]()
```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```
函数[person]()除了必选参数[name]()和[age]()外，还接受关键字参数[kw]()。在调用该函数时，可以只传入必选参数：
```python
>>> person('Michael', 30)
name: Michael age: 30 other: {}
```
也可以传入任意个数的关键字参数：
```python
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```
关键字参数可以扩展函数的功能。如果要做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

和可变参数类似，也可以先组装出一个[dict]()，然后，把该[dict]()转换为关键字参数传进去：
```python
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
当然，上面复杂的调用可以用简化的写法：
```python
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
`\*\*extra`表示把`extra`这个[dict]()的所有key-value用关键字参数传入到函数的`\*\*kw`参数，`kw`将获得一个[dict]()，注意`kw`获得的[dict]()是`extra`的一份拷贝，对`kw`的改动不会影响到函数外的`extra`。

---
### 命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过 [kw]() 检查。

仍以[person()]()函数为例，我们希望检查是否有 [city]() 和 [job]() 参数：
```python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```
但是调用者仍可以传入不受限制的关键字参数：
```python
>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收 [city]() 和 [job]() 作为关键字参数。这种方式定义的函数如下：
```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```
和关键字参数 [\*\*kw]() 不同，命名关键字参数需要一个特殊分隔符 [\*]()，[\*]() 后面的参数被视为命名关键字参数：
```python
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
```
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 [\*]() 了：
```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
```python
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```
命名关键字参数可以有缺省值，从而简化调用：
```python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```
由于命名关键字参数[city]()具有默认值，调用时，可不传入[city]()参数：
```python
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer
```
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个 [\*]() 作为特殊分隔符。如果缺少 [\*]()，[Python]()解释器将无法识别位置参数和命名关键字参数：
```python
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
```
---
### 参数组合
在[Python]()中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。<br>但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```
在函数调用的时候，[Python]()解释器自动按照参数位置和参数名把对应的参数传进去。
```python
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```
最神奇的是通过一个[tuple]()和[dict]()，你也可以调用上述函数：
```python
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```
所以，对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的。

> 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
