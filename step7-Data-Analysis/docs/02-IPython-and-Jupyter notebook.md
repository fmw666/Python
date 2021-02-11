## 💬 IPython 及 Jupyter notebook

### 安装

+ IPython 的安装

    ```python
    pip install ipython
    ```

+ Jupyter 的安装

    ```python
    pip install jupyter
    ```

### 基本使用

+ IPython 的基本使用——启动

    ```bash
    # 终端中
    $ ipython
    d:\python3.9.0\lib\site-packages\IPython\core\interactiveshell.py:936: UserWarning: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
    warn("Attempting to work in a virtualenv. If you encounter problems, please "
    Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: a = 10

    In [2]: a
    Out[2]: 10
    ```

+ IPython 的基本使用——退出

    ```bash
    # 终端中
    ...
    In [1]: exit
    ```

+ Jupyter 的基本使用——启动

    ```bash
    # 终端中
    $ jupyter notebook
    ...

    # 通过地址 http://localhost:8888/ 来访问
    # Jupyter notebook 可以使用 IPython 命令
    ```

+ Jupyter 的基本使用——安装第三方包

    ```python
    # ipython 命令行中
    In [1]: ! pip install xxx

    # 如：! pip install matplotlib
    ```

+ Jupyter 的基本使用——退出

    ```bash
    # 终端中

    快捷键 'ctrl + C' 退出
    ```

### IPython 基础

> 可单独作用于终端或 Jupyter notebook 中

+ Tab 补全

    *变量名*

    ```python
    In [1]: an_apple = 27

    In [2]: an_example = 42

    In [3]: an<Tab>
    an_apple an_example any
    ```

    *方法、属性*

    ```python
    In [1]: b = [1, 2, 3]

    In [2]: b.<Tab>
    b.append  b.count   b.insert  b.reverse
    b.clear   b.extend  b.pop     b.sort
    b.copy    b.index   b.remove
    ```

    *模块*

    ```python
    In [1]: import datetime

    In [2]: datatime.<Tab>
    datetime.date          datetime.MAXYEAR     datetime.timedelta
    datetime.datetime      datetime.MINYEAR     datetime.timezone
    datetime.datetime_CAPI datetime.time        datetime.tzinfo
    ```

    *路径*

    ```python
    In [1]: datasets/movielens/<Tab>
    datasets/movielens/movies,dat   datasets/movielens/README
    datasets/movielens/ratings.dat  datasets/movielens/users.dat

    In [2]: path = 'datasets/movielens/<Tab>
    datasets/movielens/movies,dat   datasets/movielens/README
    datasets/movielens/ratings.dat  datasets/movielens/users.dat
    ```

    *关键字参数*

    ```python
    In [1]: def func_with_keywords(abra=1, abbra=2, abbbra=3):
                return abra, abbra, abbbra
    
    In [2]: func_with_keywords(ab<Tab>)
    abbbra=  abbra=  abra=  abs
    ```

+ 内省

    在一个变量名的前后使用问号（?）可以显示一些关于该对象的概要信息，这就是对象内省：

    ```python
    In [1]: b = [1, 2, 3]

    In [2]: b?
    Type:        list
    String form: [1, 2, 3]
    Length:      3
    Docstring:  
    Built-in mutable sequence.

    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    ```

    如果对象是一个函数或实例方法，则文档字符串会显示出来：

    ```python
    In [1]: def add_numbers(a, b):
                """
                Add two numbers together
                
                Returns
                -------
                the_sum : type of arguments
                """
                return a + b
    
    # 使用 ？ 来显示文档字符串
    In [2]: add_numbers?
    Signature: add_numbers(a, b)
    Docstring:
    Add two numbers together

    Returns
    -------
    the_sum : type of arguments
    File:      f:\2a.python数据分析\code\<ipython-input-15-5b0474888b43>
    Type:      function

    # 使用 ?? 来显示函数的源代码
    In [3]: add_numbers??
    Signature: add_numbers(a, b)
    Source:   
    def add_numbers(a, b):
        """
        Add two numbers together

        Returns
        -------
        the_sum : type of arguments
        """
        return a + b
    File:      f:\2a.python数据分析\code\<ipython-input-18-0e543d60c645>
    Type:      function
    ```

    问号（？）可以结合星号（*）作为通配符匹配字符

    ```python
    In [1]: import datetime as dt

    In [2]: dt.*time*?
    dt.datetime
    dt.datetime_CAPI
    dt.time
    dt.timedelta
    dt.timezone
    ```

+ %run 命令

    如果已有脚本文件 *ipython_script_test.py*：

    ```python
    def f(x, y, z):
        return (x + y) / z

    a = 5
    b = 6
    c = 7.5


    result = f(a, b, c)
    ```

    则可以使用 %run 命令来运行，且运行后文件中定义的所有变量、函数均可任意使用：

    > 如果想使用 IPython 命名空间中已有的变量，则使用 **%run -i** 命令

    ```python
    In [1]: %run ipython_script_test.py

    In [2]: c
    Out[2]: 7.5

    In [3]: result
    Out[3]: 1.4666666666666666
    
    In [4]: f(1, 1, 2)
    Out[4]: 1.0
    ```

    如果想把脚本导入一个代码单元，使用 %load 命令：

    ```python
    In [1]: %load ipython_script_test.py
    # %load ipython_script_test.py
    def f(x, y, z):
        return (x + y) / z

    a = 5
    b = 6
    c = 7.5


    result = f(a, b, c)
    ```

+ 魔术命令

    IPython 的特殊命令（没有内建到 Python 自身中去）被称为“魔术”命令，这些命令被设计来简化常见任务。魔术命令呃前缀符号是百分号 %，如查看当前路径：

    ```python
    In [1]: %pwd
    Out[1]: 'F:\\2a.Python数据分析\\code'
    ```

    一些魔术命令可以赋值给 Python 变量：

    ```python
    In [1]: a = %pwd

    In [2]: a
    Out[2]: 'F:\\2a.Python数据分析\\code'
    ```

    如果魔术命令与当前命名空间变量不冲突，则可不加 %，这种特性被称为 *自动魔术*，可使用 `%automagic` 进行启用或禁用：

    ```python
    In [1]: pwd
    Out[1]: 'F:\\2a.Python数据分析\\code'

    In [2]: %automagic
    Automagic is OFF, % prefix IS needed for line magics.

    In [3]: pwd
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    F:\2a.Python数据分析\code\ipython_script_test.py in <module>
    ----> 1 pwd

    NameError: name 'pwd' is not defined
    ```

    IPython 常用魔术命令：

    |命令|描述|
    |:--|:---|
    |%quickref|显示 IPython 快速参考卡|
    |%magic|显示所有可用魔术命令的详细文档|
    |%debug|从最后发生报错的底部进入交互式调试器|
    |%hist|打印命令输入（也可以打印输出）历史|
    |%pdb|出现任意报错后自动进入调试器|
    |%pwd|显示当前路径|
    |%reset|删除交互式命名空间中所有的变量/名称|
    |%page OBJECT|通过分页器更美观地打印显示一个对象|
    |%run script.py|在 IPython 中运行一个 Python 脚本|
    |%prun statement|使用 CProfile 执行语句，并报告输出|
    |%time statement|报告单个语句的执行时间|
    |%timeit statement|多次运行单个语句计算平均执行时间；在估算代码最短执行时间时有用|
    |%who, %who_ls, %whos|根据不同级别的信息/详细程度，展示交互命名空间中定义的变量|
    |%xdel variable|在 IPython 内部删除一个变量，消除相关的引用|

+ matplotlib 集成

    IPython 能在分析计算领域流行的原因之一，就是它和数据可视化、用户界面库（如 matplotlib）的良好集成。

    注意，使用 matplotlib，要更换 numpy 版本：

    ```bash
    # 终端中
    pip install numpy==1.19.3
    ```

    要在 Jupyter 网页外显示图（后台），使用魔术命令 %matplotlib：

    ```python
    In [1]: %matplotlib
    Using matplotlib backend: TkAgg

    In [2]: import matplotlib.pyplot as plt

    In [3]: import numpy as np

    In [4]: plt.plot(np.random.randn(50).cumsum())
    [<matplotlib.lines.Line2D at 0x219ce8ab700>]
    ```

    要在 Jupyter 网页内显示图，使用魔术命令 %matplotlib inline：

    ```python
    In [1]: %matplotlib inline

    In [2]: import matplotlib.pyplot as plt

    In [3]: import numpy as np

    In [4]: plt.plot(np.random.randn(50).cumsum())
    [<matplotlib.lines.Line2D at 0x219ce615550>]
    ```
