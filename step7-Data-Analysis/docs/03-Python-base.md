## 💬 Python 语言基础

### 语言语义

+ Tab（或空格） 缩进

    ```python
    for x in array:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)
    ```

+ 一切皆对象

    每一个数值、字符串、数据结构、函数、类、模块以及所有存在于 Python 解释器中的事物，都是 Python 对象。

+ 注释

    当行注释

    ```python
    # 此行被注释

    print("Hello World")  # 当然也可以注释在语句后
    ```

    多行注释

    ```python
    '''
    多行注释，使用三个单引号 '
    '''

    """
    多行注释，也可使用三个双引号 "
    """

    """
    当然，单引号和双引号不能混用！
    '''
    ```

+ 函数和对象方法的调用

    调用函数，向函数括号里传递 0 或多个参数，通常会把返回值赋值给一个变量：

    ```python
    result = f(x, y, z)
    g()
    ```

    调用对象内部方法，使用点：

    ```python
    obj.some_method(x, y, z)

    # 函数传参既可以是位置参数也可以是关键字参数：
    result = f(a, b, c, d=5, e='foo')
    ```

+ 变量和参数传递

    Python 中，对变量赋值时，你就创建了一个指向等号右边对象的引用，例如：

    ```python
    # 变量 a，赋值一个列表 list
    a = [1, 2, 3]

    # 现将 a 赋值给新变量 b
    b = a

    '''
    某些语言中，这种赋值是值拷贝过程，即上述中是列表 [1,2,3] 赋值给了 b
    而在 Python 中，是 a、b 指向了相同的对象 list[1,2,3]
    可以验证如下：
    '''
    b.append(4)

    print(a)
    # 输出 [1, 2, 3, 4]
    ```

    Python 中有 *可更改（mutable）对象* 与 *不可更改（immutable）对象*。可更改类型有：list、dict；不可更改类型有：string、tuple、number

    在函数参数传递中，对于可更改对象，类似于 C++ 引用传递，对于不可更改类型，类似于 C++ 值传递：

    ```python
    # 不可更改对象作为函数参数
    def f1(value):
        value += 1
    
    a = 10
    f1(a)
    print(a)    # 输出 10


    # 可更改对象作为函数参数
    def f2(some_list, element):
        some_list.append(element)
    
    data = [1, 2, 3]
    f2(data, 4)
    print(data)    # 输出 [1, 2, 3, 4]
    ```

+ 动态引用、强类型

    Python 中的对象引用并不涉及类型，这称为 *动态类型*：

    ```python
    a = 5
    pring(type(a))  # int

    a = 'foo'
    print(type(a))  # str
    ```

    Python 是 *强类型语言*，这意味着所有的对象都拥有一个指定的类型（或类），隐式转换只在某些特定、明显的情况下发生：

    ```python
    print('5' + 5)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-16-4dd8efb5fac1> in <module>
    ----> 1 '5' + 5

    TypeError: can only concatenate str (not "int") to str
    ```

    ```python
    a = 4.5
    b = 2

    print('a is {0}, b is {1}'.format(type(a), type(b)))
    # 输出 a is <class 'float'>, b is <class 'int'>
    print(a / b)
    # 输出 2.25
    print(type(a / b))
    # 输出 <class 'float'>
    ```

    *isinstance* 函数可以检查一个对象是否是特定类型的实例：

    ```python
    a = 5
    print(isinstance(a, int))
    # 输出 True

    # 也可以接收一个元组，判断 对象 是否是其中类型之一
    b = 4.5
    print(isinstance(a, (int, float)))
    # 输出 True
    print(isinstance(b, (int, float)))
    # 输出 True
    ```

+ 属性和方法

    Python 中对象通常都会有属性和方法，属性和方法都可以通过 `obj.attribute_name` 调用：

    ```python
    In [1]: a = 'foo'

    In [2]: a.<Tab>
    a.capitalize  a.format  ...
    ```

    属性和方法也可通过 *getattr* 函数获得，这种通过变量名访问对象通常被称为“反射”：

    ```python
    getattr(a, 'split')
    # <function str.split>

    # 同类型还有 hasattr 和 setattr
    ```

+ 鸭子类型

    通常情况下，你并不关心某个对象的具体类型，而关心它是否拥有某个特殊的方法或行为。

    > “鸭子类型” 说法源于 “一个东西走起来像鸭子叫起来像鸭子，那它就是鸭子”。例如，你可以验证一个对象如果实现了迭代器协议，那么它一定是可迭代的（包含 \_\_iter\_\_ 魔术方法）

    ```python
    def isiterable(obj):
        try:
            iter(obj)
            return True
        except TypeError:
            return False

    # 对于绝大部分 Python 容器类型的对象，iter 函数都会返回 True
    isiterable('a string')
    # True
    isiterable([1, 2, 3])
    # True
    isiterable(5)
    # False

    # 常见的案例是先检查对象是否是一个列表（或一个 NumPy 数组）
    # 如果不是则转换为一个列表
    if not isinstance(x, list) and isiterable(x):
        x = list(x)
    ```

+ 导入模块

    Python 模块就是以 *.py* 为后缀并包含 Python 代码的文件。假设有以下模块：

    ```python
    # some_module.py
    PI = 3.14159

    def f(x):
        return x + 2

    def g(a, b):
        return a + b
    ```

    要导入模块中定义的变量和函数：

    ```python
    import some_module
    
    result = some_module.f(5)
    pi = some_module.PI
    ```

    或者：

    ```python
    from some_module import f, g, PI
    
    result = g(5, PI)
    ```

    也可用关键字 as，对导入内容更名：

    ```python
    import some_module as sm
    from some_module import PI as pi, g as gf

    r1 = sm.f(pi)
    r2 = gf(6, pi)
    ```

<br>
上述为 Python 中的一些基本特性，语法中的其他内容后续补充。