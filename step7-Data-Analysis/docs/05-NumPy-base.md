## 💬 NumPy 基础：数组与向量化计算

&emsp;&emsp;NumPy，是 Numerical Python 的简称，它是目前 Python 数值计算最为重要的基础包，大多数计算包都提供了基于 NumPy 的科学函数功能。NumPy 包含了以下内容：

+ ndarray，一种高效多维数组，提供了基于数组的便捷算术操作以及灵活的广播功能

+ 对所有数据进行快速的矩阵计算，而无须编写循环程序

+ 对硬盘中数组数据进行读写的工具，并对内存映射文件进行操作

+ 线性代数、随机数生成以及傅里叶变换功能

+ 用于连接 NumPy 到 C、C++ 和 FORTRAN 语言类库的 C 语言 API

### NumPy ndarray：多维数组对象

&emsp;&emsp;NumPy 的核心特征之一就是 N-维数组对象——ndarray。ndarray 是 Python 中一个快速、灵活的大型数据集容器，它包含的每一个元素均为相同类型。每一个 ndarray 数组都有一个 shape 属性，用来表征每一维度的数量；同时也有 dtype 属性，用来描述数组的数据类型：

```python
In [1]: import numpy as np

# 生成随机数组
In [2]: data = np.random.randn(2, 3)

In [3]: data
Out[3]: array([[-1.13038125, -0.36260883, -0.85512949],
               [ 0.8039776 , -1.26492419,  1.56225998]])

In [4]: data.shape
Out[4]: (2, 3)

In [5]: data.dtype
Out[5]: dtype('float64')
```

+ **生成 ndarray**

    生成数据最简单的方式是使用 NumPy 的 array 函数，例如：

    ```python
    In [1]: import numpy as np

    In [2]: data1 = [6, 7.5, 8, 0, 1]

    In [3]: arr1 = np.array(data1)

    In [4]: arr1
    Out[4]: array([6. , 7.5, 8. , 0. , 1. ])
    ```

    嵌套序列会自动转换为多维数组：

    ```python
    In [1]: import numpy as np

    In [2]: data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

    In [3]: arr2 = np.array(data2)

    In [4]: arr2
    Out[4]: array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

    # 可以使用 ndim（查看维度） 和 shape 方法来验证
    In [5]: arr2.ndim
    Out[5]: 2

    In [6]: arr2.shape
    Out[6]: (2, 4)
    ```

    除了 np.array，还有很多其他函数可以创建新数组：

    + np.zeros：一次性创造全 0 数组

    + np.ones：一次性创造全 1 数组

    + np.empty：一次性创造一个没有初始化数值的数组

    > 如果想要创建高维数组，则需要为 shape 传递一个元组。没有特殊指明，默认数据类型为 float64 浮点型。

    ```python
    In [1]: np.zeros(10)
    Out[1]: 
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

    In [2]: np.zeros((3, 3))
    Out[2]: array([[0., 0., 0.],
                [0., 0., 0.],
                [0., 0., 0.]])

    In [3]: np.ones((2, 2), dtype=int)
    Out[3]: array([[1, 1],
                [1, 1]])

    In [4]: np.empty((2, 3, 2))
    Out[4]: array([[[0., 0.],
                    [0., 0.],
                    [0., 0.]],

                [[0., 0.],
                    [0., 0.],
                    [0., 0.]]])
    ```

    也可使用 arange（Python 内建函数 range 的数组版）等函数：

    ```python
    In [1]: np.arange(5)
    Out[1]: array([0, 1, 2, 3, 4])

    In [2]: np.arange(2, 9)
    Out[2]: array([2, 3, 4, 5, 6, 7, 8])

    In [3]: np.arange(2, 9, 2)
    Out[3]: array([2, 4, 6, 8])
    ```

    ***数组生成函数***

    |函数名|描述（使用 对象内省 查看）|
    |:-----|:---|
    |array|将输入数据（可以是列表、元组、数组以及其他序列）转换为 ndarray，如不显式指明数据类型，将自动推断；默认复制所有的输入数据|
    |asarray|将输入转换为 ndarray，但如果输入已经是 ndarray 则不再复制|
    |arange|Python 内建函数 range 的数组版，返回一个数组|
    |ones|根据给定形状和数据类型生成全 1 数组|
    |ones_like|根据所给的数组生成一个形状一样的全 1 数组|
    |zeros|根据给定形状和数据类型生成全 0 数组|
    |zeros_like|根据所给的数组生成一个形状一样的全 0 数组|
    |empty|根据给定形状生成一个没有初始化数值的空数组|
    |empty_like|根据所给数组生成一个形状一样但没有初始化数值的空数组|
    |full|根据给定的形状和数据类型生成指定数值的数组|
    |full_like|根据所给的数组生成一个形状一样但内容是指定数值的数组|
    |eye, identity|生成一个 N×N 特征矩阵（对角线位置都是 1，其余位置是 0）|

+ **ndarray 的数据类型**

    数据类型，即 dtype，是一个特殊的对象，它包含了 ndarray 需要为某一种类型数据所申明的内存块信息：

    ```python
    In [1]: import numpy as np

    In [2]: arr1 = np.array([1, 2, 3], dtype=np.float64)

    In [3]: arr2 = np.array([1, 2, 3], dtype=np.int32)

    In [4]: arr1.dtype
    Out[4]: dtype('float64')

    In [5]: arr2.dtype
    Out[5]: dtype('int32')
    ```

    ***NumPy 数据类型***

    |类型|类型代码|描述|
    |:--|:-------|:---|
    |int8, uint8|i1, u1|有符号和无符号的 8 数位整数|
    |int16, uint16|i2, u2|有符号和无符号的 16 数位整数|
    |int32, uint32|i4, u4|有符号和无符号的 32 数位整数|
    |int64, uint64|i8, u8|有符号和无符号的 64 数位整数|
    |float16|f2|半精度浮点数|
    |float32|f4 或 f|标准单精度浮点数；兼容 C 语言 float|
    |float64|f8 或 d|标准双精度浮点数；兼容 C 语言 double 和 Python float|
    |float128|f16 或 g|扩展精度浮点数|
    |complex64,<br>complex128,<br>complex256|c8, c16, c32|分别基于 32 位、64 位、128位浮点数的复数|
    |bool|?|布尔值，存储 True 或 False|
    |object|O|Python object 类型|
    |string_|S|修正的 ASCII 字符串类型；例如生成一个长度为 10 的字符串类型，使用 'S10'|
    |unicode_|U|修正的 Unicode 类型；例如生成一个长度为 10 的 Unicode 类型，使用 'U10'|

    可以使用类型代码生成类型，也可以使用 astype 方法显式地转换数组地数据类型：

    ```python
    In [1]: import numpy as np

    In [2]: empty_uint32 = np.empty(8, dtype='u4')

    In [3]: arr = np.array(['1.25', '-9.6', '42'], dtype=np.string)

    In [4]: new_arr.astype(float)
    Out[4]: array([1.25, -9.6, 42.])
    ```

+ **NumPy 数组算术**

    NumPy 的数组算术允许你进行批量操作而无须任何 for 循环。NumPy 用户称这种特性为向量化。任何在两个等尺寸数组之间的算术操作都应用了逐元素操作的方式：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.array([[1., 2., 3.], [4., 5., 6.]])

    In [3]: arr
    Out[3]: array([[1., 2., 3.].
                [4., 5., 6.]])

    In [4]: arr * arr
    Out[4]: array([[1., 4., 9.],
                [16., 25., 36.]])

    In [5]: arr - arr
    Out[5]: array([[0., 0., 0.],
                [0., 0., 0.]])
    ```

    带有标量计算的算术操作，会把计算参数传递给数组的每一个元素：

    ```python
    In [6]: 1 / arr
    Out[6]: array([[1., 0.5, 0.3333],
                [0.25, 0.2, 0.1667]])

    In [7]: arr ** 0.5
    Out[7]: array([[1., 1.4142, 1.7321],
                [2., 2.2361, 2.4495]])
    ```

    同尺寸数组之间的比较，会产生一个布尔值数组：

    ```python
    In [8]: arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

    In [9]: arr2
    Out[9]: array([[0., 4., 1.],
                [7., 2., 12.]])

    In [10]: arr2 > arr
    Out[10]: array([[False, True, False],
                    [True, False, True]])
    ```

    不同尺寸的数组间的操作，将会用到广播特性，这里后续展开。

+ **基础索引与切片**

    索引和切片就是为了让你选中数据的子集或某个单元元素。一维数组比较简单，看起来和 Python 的列表类似：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.arange(10)

    In [3]: arr
    Out[3]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    In [4]: arr[5]
    Out[4]: 5

    In [5]: arr[5:8]
    Out[5]: array([5, 6, 7])

    In [6]: arr[5:8] = 12

    In [7]: arr
    Out[7]: array([0, 1, 2, 3, 4, 12, 12, 12, 8, 9])
    ```

    区别于 Python 的内建列表，数组的切片是原数组的 *视图*。这意味着数据并不是复制，任何对于视图的修改都会反映到原数组上：

    ```python
    In [8]: arr_slice = arr[5:8]

    In [9]: arr_slice
    Out[9]: array([12, 12, 12])

    # 改变 arr_slice 中的值
    In [10]: arr_slice[1] = 12345

    In [11]: arr
    Out[11]: array([0, 1, 2, 3, 4, 12, 12345, 12, 8, 9])

    # 不写切片值的 [:] 将会引用数组的所有值
    In [12]: arr_slice[:] = 64

    In [13]: arr
    Out[13]: array([0, 1, 2, 3, 4, 64, 64, 64, 8, 9])
    ```

    > tips：为什么不做复制？因为 NumPy 常处理非常大的数组，涉及频繁复制数据会引起内存问题。

    如果想要拷贝一份数组切片，则必须显式地复制这个数组，例如：`arr[5:8].copy()`

    对于高维数组，每个索引值对应的元素可能是一个数组，因此可以递归或通过传递一个索引的逗号分隔列表去得到单个元素：

    ```python
    In [1]: import numpy as np

    In [2]: arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    In [3]: arr2d[2]
    Out[3]: array([7, 8, 9])

    # 递归得到
    In [4]: arr2d[0][2]
    Out[4]: 3

    # 逗号分隔
    In [5]: arr2d[0, 2]
    Out[5]: 3
    ```

    对于高维数组的切片同理，稍加理解就能掌握，每一次切片都可以对原数组降维：

    ```python
    In [1]: import numpy as np

    In [2]: arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    In [3]: arr2d
    Out[3]: array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

    # 得到前两“行”
    In [4]: arr2d[:2]
    Out[4]: array([[1, 2, 3],
                [4, 5, 6]])

    # 得到前两“行”，每一行的后两“列”
    In [5]: arr2d[:2, 1:]
    Out[5]: array([[2, 3],
                [5, 6]])

    # 得到第 2 “行”，前两“列”
    In [6]: arr2d[1, :2]
    Out[6]: array([4, 5])

    # 得到前两“行”，第 3 “列”
    In [7]: arr2d[:2, 2]
    Out[7]: array([3, 6])

    # 得到每行的第一“列”
    In [8]: arr2d[:, :1]
    Out[8]: array([[1],
                [4],
                [7]])

    # 对切片表达式赋值时，同样为视图操作
    In [9]: arr2d[:2, 1:] = 0
    Out[9]: array([[1, 0, 0],
                [4, 0, 0],
                [7, 8, 9]])
    ```

+ **布尔索引**

    数组的比较操作（比如 ==）是可以向量化的，数组与值的比较可以产生一个布尔值数组：

    ```python
    In [1]: import numpy as np

    In [2]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

    In [3]: names == 'Bob'
    Out[3]: array([True, False, False, True, False, False, False])
    ```

    同时，布尔值数组可以作为参数传入其他数组，布尔值数组的长度必须和数组轴索引长度一致：

    ```python
    In [4]: data = np.arange(7)

    In [5]: data
    Out[5]: array([0, 1, 2, 3, 4, 5, 6])

    In [6]: data[names == 'Bob']
    Out[6]: array([0, 3])
    ```

    可以使用 `!=` 或条件表达式前使用 `~` 对条件取反：

    ```python
    In [7]: names != 'Bob'
    Out[7]: array([False, True, True, False, True, True, True])

    In [8]: ~(names == 'Bob')
    Out[8]: array([False, True, True, False, True, True, True])
    ```

    Python 中关键字 `and` 和 `or` 对布尔值数组没有用，使用 `&`（and）和 `|`（or）代替：

    ```python
    In [9]: mask = (names == 'Bob') | (names == 'Will')

    In [10]: mask
    Out[10]: array([True, False, True, True, True, False, False])

    In [11]: mask = (names == 'Bob') & (False)

    In [12]: mask
    Out[12]: array([False, False, False, False, False, False, False])
    ```

+ **神奇索引**

    *神奇索引* 是 NumPy 中的术语，用于描述使用整数数组进行数据索引。

    假设我们有一个 8×4 的数组：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.empty((8, 4))

    In [3]: for i in range(8):
                arr[i] = i

    In [4]: arr
    Out[4]: array([[0., 0., 0., 0.],
                [1., 1., 1., 1.],
                [2., 2., 2., 2.],
                [3., 3., 3., 3.],
                [4., 4., 4., 4.],
                [5., 5., 5., 5.],
                [6., 6., 6., 6.],
                [7., 7., 7., 7.]])
    ```

    为了选出一个符合特定顺序的子集，可以通过传递一个包含指明所需顺序的列表或数组来完成：

    ```python
    # 这里传入的是列表，也可以传入数组 np.array([4, 3, 0, 6])
    In [5]: arr[[4, 3, 0, 6]]
    Out[5]: array([[4., 4., 4., 4.],
                [3., 3., 3., 3.],
                [0., 0., 0., 0.],
                [6., 6., 6., 6.]])
    ```

    如果使用负的索引，将从尾部进行选择：

    ```python
    In [6]: arr[[-3, -5, -7]]
    Out[6]: array([[5., 5., 5., 5.],
                [3., 3., 3., 3.],
                [1., 1., 1., 1.]])
    ```

    神奇索引得到的结果总是一维的，如果想要得到特定区域，可以考虑其他方法，如：

    ```python
    In [7]: arr = np.arange(32).reshape((8, 4))

    In [8]: arr
    Out[8]: array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15],
                [16, 17, 18, 19],
                [20, 21, 22, 23],
                [24, 25, 26, 27],
                [28, 29, 30, 31]])

    # 通过神奇索引得到结果总是一维的
    In [9]: arr[[1, 5, 7, 2], [0, 3, 1, 2]]
    Out[9]: array([4, 23, 29, 10])

    # 通过其他方式得到特定区域
    In [10]: arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
    Out[10]: array([[4, 7, 5, 6],
                    [20, 23, 21, 22],
                    [28, 31, 29, 30],
                    [8, 11, 9, 10]])
    ```

+ **数组转置和换轴**

    转置是一种特殊的数据重组方式，可以返回底层数据的视图。数组拥有 `transpose` 方法，也有特殊的 `T` 属性：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.arange(15).reshape((3, 5))

    In [3]: arr
    Out[3]: array([[ 0,  1,  2,  3,  4],
                   [ 5,  6,  7,  8,  9],
                   [10, 11, 12, 13, 14]])

    In [4]: arr.T
    Out[4]: array([[0, 5, 10],
                   [1, 6, 11],
                   [2, 7, 12],
                   [3, 8, 13],
                   [4, 9, 14]])

    In [5]: arr.transpose()
    Out[5]: array([[0, 5, 10],
                   [1, 6, 11],
                   [2, 7, 12],
                   [3, 8, 13],
                   [4, 9, 14]])
    ```

    当进行矩阵计算时，可能需要进行一些特定操作，如计算矩阵的内积会使用 `np.dot`：

    ```python
    In [6]: arr = np.random.randn(6, 3)

    In [7]: arr
    Out[7]: array([[ 0.07500987,  2.09890546,  2.62569602],
                   [ 0.14339131,  0.11738914, -0.09726827],
                   [ 1.73804972, -1.18171653, -2.07034798],
                   [-0.97491109,  0.95448881, -0.36978696],
                   [ 0.11512856,  1.6148048 , -0.96814446],
                   [-0.37423436, -0.98958066,  0.38662069]])

    In [8]: np.dot(arr.T, arr)
    Out[8]: array([[ 4.15076193, -2.25390736, -3.31100044],
                   [-2.25390736, 10.31355163,  5.64731974],
                   [-3.31100044,  5.64731974, 12.41360314]])
    ```

    对于更高维度的数组，`transpose` 方法可以接收包含轴编号的元组，用于置换轴：

    ```python
    In [9]: arr = np.arange(16).reshape((2, 2, 4))

    In [10]: arr
    Out[10]: array([[[ 0,  1,  2,  3],
                     [ 4,  5,  6,  7]],
                    [[ 8,  9, 10, 11],
                     [12, 13, 14, 15]]])

    # 把三维轴的 0轴 和 1轴 交换
    In [11]: arr.transpose((1, 0, 2))
    Out[11]: array([[[ 0,  1,  2,  3],
                     [ 8,  9, 10, 11]],
                    [[ 4,  5,  6,  7],
                     [12, 13, 14, 15]]])
    ```

    当然，也可以通过 `swapaxes` 方法置换相应的轴：

    ```python
    In [12]: arr = np.arange(16).reshape((2, 2, 4))

    In [13]: arr
    Out[13]: array([[[ 0,  1,  2,  3],
                     [ 4,  5,  6,  7]],
                    [[ 8,  9, 10, 11],
                     [12, 13, 14, 15]]])

    # 把三维轴的 1轴 和 2轴 交换
    In [11]: arr.swapaxes(1, 2)
    Out[11]: array([[[ 0,  4],
                     [ 1,  5],
                     [ 2,  6],
                     [ 3,  7]],
                    [[ 8, 12],
                     [ 9, 13],
                     [10, 14],
                     [11, 15]]])
    ```

### 通用函数：快速的逐元素数组函数

通用函数，也可以称为 `ufunc`，是一种在 ndarray 数据中进行逐元素操作的函数，某些简单函数接收一个或多个标量数值，并产生一个或多个标量结果，而通用函数就是对这些简单函数的向量化封装。

> 标量：单整数（或浮点数）数据；向量化：利用数组表达式来替代显式循环的方法称为向量化

有很多 ufunc 是简单的逐元素转换，比如 `sqrt` 或 `exp` 一元通用函数：

```python
In [1]: import numpy as np

In [2]: arr = np.arange(10)

In [3]: arr
Out[3]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 求根号，隐式转换为浮点型
In [4]: np.sqrt(arr)
Out[4]: array([0., 1., 1.41421356, 1.73205081, 2., 2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.])

# 求 e 的 x 次方
In [5]: np.exp(arr)
Out[5]: array([1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01, 5.45981500e+01, 1.48413159e+02, 4.03428793e+02, 1.09663316e+03, 2.98095799e+03, 8.10308393e+03])
```

也有诸如 `add` 或 `maximum` 接收两个数组作为参数的二元通用函数：

```python
In [6]: x = np.random.randn(8)

In [7]: y = np.random.randn(8)

In [8]: x
Out[8]: array([0.04779461, -0.5693168, -1.51545964, 0.0613396, -0.55333612, 1.08644688, -0.32525729, -0.32005243])

In [9]: y
Out[9]: array([-0.38771763, -0.48837013, -1.6328695, -0.86527395, 0.83213777, 0.55542294, -0.44991655, -1.32199402])

# 求 x 和 y 每一列中的最大值
In [10]: np.maximum(x, y)
Out[10]: array([0.04779461, -0.48837013, -1.51545964, 0.0613396, 0.83213777, 1.08644688, -0.32525729, -0.32005243])
```

也有一些通用函数返回多个数组。比如 `modf`，是 Python 内建函数 `divmod` 的向量化版本。它返回了一个浮点值数组的小数部分和整数部分：

```python
In [11]: arr = np.random.randn(7) * 5

In [12]: arr
Out[12]: array([0.78717167, 4.1168182, -5.76949166, -1.10782293, 1.76970463, 0.14903839, -2.24270491])

In [13]: remainder, whole_part = np.modf(arr)

In [14]: remainder
Out[14]: array([0.78717167, 0.1168182, -0.76949166, -0.10782293, 0.76970463, 0.14903839, -0.24270491])

In [15]: whole_part
Out[15]: array([0., 4., -5., -1., 1., 0., -2.])
```

通用函数可以通过可选参数 `out` 来接收运算结果：

```python
In [16]: arr_out = np.empty(7)

In [17]: np.sqrt(arr, arr_out)
<ipython-input-165-85ebc3849b55>:1: RuntimeWarning: invalid value encountered in sqrt np.sqrt(arr, arr_out)
Out[17]: array([0.88722696, 2.02899438, nan, nan, 1.33030246, 0.38605491, nan])

In [18]: arr
Out[18]: array([0.78717167, 4.1168182, -5.76949166, -1.10782293, 1.76970463, 0.14903839, -2.24270491])

In [19]: arr_out
Out[19]: array([0.88722696, 2.02899438, nan, nan, 1.33030246, 0.38605491, nan])
```

***一元通用函数***

|函数名|描述|
|:-----|:---|
|abs、fabs|逐元素地计算整数、浮点数或复数的绝对值|
|sqrt|计算每个元素的平方根（与 arr ** 0.5 相等）|
|square|计算每个元素的平方（与 arr ** 2 相等）|
|exp|计算每个元素的自然指数值 e<sup>x</sup>|
|log、log10、log2、log1p|分别对应：自然对数（e 为底）、对数 10 为底、对数 2 为底、log(1+x)|
|sign|计算每个元素的符号值：1（正数）、0（0）、-1（负数）|
|ceil|计算每个元素的最高整数值（即大于等于给定数值的最小整数）|
|floor|计算每个元素的最小整数值（即小于等于给定元素的最大整数）|
|rint|将元素保留到整数位，并保持 dtype|
|modf|分别将数组的小数部分和整数部分按数组形式返回|
|isnan|返回数组中的元素是否是一个 NaN（不是一个数值），形式为布尔值数组|
|isfinite、isinf|分别返回数组中的元素是否有限（非 inf、非 NaN）、是否无限的，形式为布尔值数组|
|cos、cosh、sin、<br>sinh、tan、tanh|常规的双曲三角函数|
|arccos、arccosh、arcsin、<br>arcsinh、arctan、arctanh|反三角函数|
|logical_not|对数组的元素按位取反（与 ~arr 效果一致）|

***二元通用函数***

|函数名|描述|
|:----|:---|
|add|将数组的对应元素相加|
|subtract|在第二个数组中，将第一个数组中包含的元素去除|
|multiply|将数组的对应元素相乘|
|divide, floor_divide|除或整除（放弃余数）|
|power|将第二个数组的元素作为第一个数组对应元素的幂次方|
|maximum, fmax|逐个元素计算最大值，fmax 忽略 NaN|
|minimum, fmin|逐个元素计算最小值，fmin 忽略 NaN|
|mod|按元素的求模计算（即求除法的余数）|
|copysign|将第一个数组的符号值改为第二个数组的符号值|
|greater, greater_equal, less,<br>less_equal, equal, not_equal|进行逐个元素的比较，返回布尔值数组（与数学操作符 >、>=、<、<=、==、!= 效果一致）|
|logical_and, logical_or,<br>logical_xor|进行逐个元素的逻辑操作（与逻辑操作符 &、|、^ 效果一致）|

### 使用数组进行面向数组编程

NumPy 中用数组表达式完成多种数据操作任务，而无须使用显式循环方法（向量化操作）。

作为一个基础示例，假设需要一些网格数据来计算函数 `sqrt(x^2 + y^2)` 的值。使用 `np.meshgrid` 函数来接收两个一维数组，返回其 x 轴以及 y 轴数组：

```python
In [1]: import numpy as np

# 以 -5->5 为 length ，0.01 为 step 的 1000 个点数据 
In [2]: points = np.arange(-5, 5, 0.01)

In [3]: points
Out[3]: array([-5.00, -4.99, -4.98, ..., 4.98, 4.99])

'''
<简要解析 np.meshgrid 函数>

假设 一维数组 a=np.array([1,2,3])、b=np.array([7,8])
网格中的点坐标有 6 个：
(1,7) (2,7) (3,7)
(1,8) (2,8) (3,8)

那么返回值为：[array([[1,2,3],[1,2,3]]), array([[7,7,7],[8,8,8]])]
'''
# 得到网格数据的 x 轴数组和 y 轴数组
In [4]: xs, ys = np.meshgrid(points, points)

# xs、ys.shape = (1000, 1000)
In [5]: ys
Out[5]: array([[-5.00, -5.00, ..., -5.00, -5.00],
               [-4.99, -4.99, ..., -4.99, -4.99],
               ...,
               [ 4.98,  4.98, ...,  4.98,  4.98],
               [ 4.99,  4.99, ...,  4.99,  4.99]])

# 得到两个 1000×1000 数组后再求对应位置平方和开根号
In [6]: z = np.sqrt(x ** 2 + ys ** 2)

In [7]: z
Out[7]: array([[7.0711,  7.064, ..., 7.0569,  7.064],
               [ 7.064, 7.0569, ..., 7.0499, 7.0569],
               ...,
               [7.0569, 7.0499, ..., 7.0428, 7.0499],
               [ 7.064, 7.0569, ..., 7.0499, 7.0569]])
```

我们预先用后面 matplotlib 知识生成这个二维数组在网格数据上的可视化图像：

```python
In [8]: import matplotlib.pyplot as plt

In [9]: plt.imshow(z, cmap=plt.cm.gray); plt.colorbar(); plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
Out[9]: Text(0.5, 1.0, 'Image plot of $\\sqrt{x^2 + y^2}$ for a grid of values')
# 生成的图像这儿就不展示了
```

+ **将条件逻辑作为数组操作**

    `np.where` 函数是三元表达式 `x if condition else y` 的向量化版本，考虑到我们的基本 Python 代码执行：

    ```python
    In [1]: import numpy as np

    In [2]: xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])

    In [3]: yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

    In [4]: cond = np.array([True, False, True, True, False])

    # 逻辑需求为：
    # cond 元素为 True 时，取对应位置 x 的值，否则取 y 值
    In [5]: result = [(x if c else y)
                     for x, y, c in zip(xarr, yarr, cond)]]

    In [6]: result
    Out[6]: [1.1, 2.2, 1.3, 1.4, 2.5]
    ```

    上述的执行，在数组量稍微庞大的基础上耗时会非常严重，其次，当数组是多维时，也无法执行。这个时候就要使用我们的 `np.where` 函数：

    ```python
    # xarr 和 yarr 必须是同等数组
    In [7]: result = np.where(cond, xarr, yarr)

    In [8]: result
    Out[8]: array([1.1, 2.2, 1.3, 1.4, 2.5])
    ```

    `np.where` 的第二个和第三个参数并不需要是数组，也可以是标量。如果要把一个数组负值全部替换为 -2，正值全部替换为 2，那么就很容易实现：

    ```python
    In [9]: arr = np.random.randn(4, 4)

    In [10]: arr
    Out[10]: array([[ 0.27545814,  0.98973623,  1.14738762, -0.13025497],
                    [ 0.2765394 ,  1.11453503,  0.67416583, -0.12339932],
                    [ 0.04718984, -1.2194738 , -1.20030532,  0.44182545],
                    [-0.67123175,  0.08731678,  0.34563459, -0.25369254]])

    In [11]: arr > 0
    Out[11]: array([[ True,  True,  True, False],
                    [ True,  True,  True, False],
                    [ True, False, False,  True],
                    [False,  True,  True, False]])

    In [12]: np.where(arr > 0, 2, -2)
    Out[12]: array([[ 2,  2,  2, -2],
                    [ 2,  2,  2, -2],
                    [ 2, -2, -2,  2],
                    [-2,  2,  2, -2]])
    ```

    `np.where` 也可以将标量和数组联合使用，比如只替代上述 arr 的正值：

    ```python
    In [13]: np.where(arr > 0, 2, arr)
    Out[13]: array([[ 2.        ,  2.        ,  2.        , -0.13025497],
                    [ 2.        ,  2.        ,  2.        , -0.12339932],
                    [ 2.        , -1.2194738 , -1.20030532,  2.        ],
                    [-0.67123175,  2.        ,  2.        , -0.25369254]])
    ```

+ **数学和统计方法**

    许多关于计算整个数组统计值或关于轴向数据的数学函数，可以作为数组类型的方法被调用。你可以使用聚合函数（通常也叫 *缩减函数*），比如 `sum`（求和）、`mean`（求平均值）和 `std`（求标准差），也可以直接调用数组实例方法，还可以使用顶层的 NumPy 函数：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.random.randn(5, 4)

    In [3]: arr
    Out[3]: array([[-0.07848023,  0.24265379, -0.62649164, -1.05933403],
                   [ 1.20580448, -0.55743715,  1.1006682 ,  0.56874852],
                   [ 0.43813554, -2.43298919,  0.13962061,  0.32243348],
                   [ 0.85542175, -0.69790371,  0.43495032,  0.08688685],
                   [-0.17309622, -0.62837755, -0.35972471,  0.49852859]])
    
    # 求平均值，使用数组的实例方法
    In [4]: arr.mean()
    Out[4]: -0.03599911623663495

    # 求平均值，使用顶层 NumPy 函数
    In [5]: np.mean(arr)
    Out[5]: -0.03599911623663495

    # 求和，使用数组的实例方法
    In [6]: arr.sum()
    Out[6]: -0.7199823247326991
    ```

    像 `mean`、`sum` 等函数可以接收一个可选参数 `axis`，这个参数可以用于计算给定轴向上的统计值，形成一个下降一维度的数组：

    ```python
    '''
    虽然前面也有涉及，但是后面会涉及地更广，举例说明轴向
  
      → 0 轴
    ↓ [[0, 1, 2, 3, 4],
    1  [5, 6, 7, 8, 9],
    轴 [4, 3, 2, 1, 0],
       [9, 8, 7, 6, 5]]

    参数 axis=0，则对每列 1 轴数据做计算。类似同理。
    如果是更高维数组，则依次增添 2 轴、3 轴...
    '''
    In [7]: arr.mean(axis=1)
    Out[7]: array([-0.38041303, 0.57944601, -0.38319989, 0.1698388 , -0.16566747])

    In [8]: arr.sum(axis=0)
    Out[8]: array([2.24778532, -4.07405382, 0.68902278, 0.4172634 ])
    ```

    其他方法，例如 `cumsum`（从 0 累和） 和 `cumprod`（从 1 累积） 并不会聚合，它们会产生一个中间结果：

    ```python
    In [9]: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])

    In [10]: arr.cumsum()
    Out[10]: array([0, 1, 3, 6, 10, 15, 21, 28])
    ```

    在多维数组中，像 `cumsum` 这样的累计函数返回相同长度的数组，但是可以在指定轴向上根据较低纬度的切片进行部分聚合：

    ```python
    In [11]: arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    In [12]: arr
    Out[12]: array([[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])

    In [13]: arr.cumsum(axis=0)
    Out[13]: array([[0,  1,  2],
                    [3,  5,  7],
                    [9, 12, 15]])

    In [14]: np.cumprod(arr, axis=1)
    Out[14]: array([[0,  0,   0],
                    [3, 12,  60],
                    [6, 42, 336]])
    ```

    ***基础数组统计方法***

    |方法|描述|
    |:--|:----|
    |sum|沿着轴向计算所有元素的累和，0 长度的数组，累和为 0|
    |mean|数学平均，0 长度的数组平均值 NaN|
    |std, var|标准差和方差，可以选择自由度调整（默认分母是 n）|
    |min, max|最小值和最大值|
    |argmin, argmax|最小值和最大值的位置|
    |cumsum|从 0 开始元素累积和|
    |cumprod|从 1 开始元素累积积|

+ **布尔值数组的方法**

    `sum` 函数可以统计布尔值数组中的 True 个数：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.random.randn(100)

    # 正值的个数
    In [3]: (arr > 0).sum()
    Out[3]: 42
    ```

    对于布尔值数组，有两个非常有用的方法 `any` 和 `all`。`any` 检查数组中是否至少有一个 True，而 `all` 检查是否每个值都是 True：

    ```python
    In [4]: bools = np.array([False, False, True, False])

    In [5]: bools.any()
    Out[5]: True

    In [6]: bools.all()
    Out[6]: False
    ```

    > 这些方法也可适用于非布尔值数组，所有非 0 元素都会按 True 处理。

+ **排序**

    和 Python 内建函数类似，NumPy 数组可以使用 `sort` 方法按位置排序：

    ```python
    In [1]: import numpy as np

    In [2]: arr = np.random.randn(6)

    In [3]: arr
    Out[3]: array([-0.27361387, 0.36865567, -0.59286943, 0.36054245, 0.09468716, -1.19164215])

    In [4]: arr.sort()

    In [5]: arr
    Out[5]: array([-1.19164215, -0.59286943, -0.27361387, 0.09468716, 0.36054245, 0.36865567])
    ```

    你可以在多维数组中根据传递的 `axis` 值，沿着轴向对每一个一维数据段进行排序：

    ```python
    In [6]: arr = np.random.randn(5, 3)

    In [7]: arr
    Out[7]: array([[ 0.97884294, -0.84468111,  1.03389029],
                   [ 1.0516682 ,  0.08438978, -0.85197342],
                   [-0.65317884, -0.88428797,  0.13411752],
                   [-1.56032192,  0.95649752, -0.582282  ],
                   [ 0.23671691, -1.27874667,  2.95889557]])

    # arr.sort(1) 等价于 arr.sort(axis=1)
    In [8]: arr.sort(1)

    In [9]: arr
    Out[9]: array([[-0.84468111,  0.97884294,  1.03389029],
                   [-0.85197342,  0.08438978,  1.0516682 ],
                   [-0.88428797, -0.65317884,  0.13411752],
                   [-1.56032192, -0.582282  ,  0.95649752],
                   [-1.27874667,  0.23671691,  2.95889557]])
    ```

    > 顶层的 `np.sort` 方法返回的是已经排序好的数组拷贝，而不是对原数组按位置排序。

    下面例子计算的是一个数组的分位数，并选出分位数所对应的值，这是一种应急的方法：

    ```python
    In [10]: large_arr = np.random.randn(1000)

    In [11]: large_arr.sort()

    # 5% quantile —— 以 0.05 为分位数
    In [12]: large_arr[int(0.05 * len(large_arr))]
    Out[12]: -1.6090637874718658
    ```

    对于更多 NumPy 排序方法的细节，以及像间接排序这类更高级技术，后续再补充。一些与排序相关的其他种类的数据操作，Pandas 中也会出现。

+ **唯一值与其他集合逻辑**

    NumPy 包含一些针对 **一维 ndarray** 的基础集合操作。常用的一个方法是 `np.unique`，返回的是数组中唯一值排序后形成的数组（类似于 Python 列表转集合再转列表）：

    ```python
    In [1]: import numpy as np

    In [2]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

    # 纯 Python 方法，返回一个列表
    In [3]: sorted(set(names))
    Out[3]: ['Bob', 'Joe', 'Will']

    # NumPy 方法，返回一个数组
    # 注意：ndarray 数组实例并没有这个方法，原因在于这个方法只针对一维数组
    In [4]: np.unique(names)
    Out[4]: array(['Bob', 'Joe', 'Will'], dtype='<U4')

    In [5]: ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

    In [6]: np.unique(ints)
    Out[6]: array([1, 2, 3, 4])
    ```

    另一个函数，`np.in1d` 可以检查一个数组中的值是否在另外一个数组中，并返回一个布尔值数组：

    ```python
    In [7]: values = np.array([6, 0, 0, 3, 2, 5, 6])

    In [8]: np.in1d(values, [2, 3, 6])
    Out[8]: array([True, False, False, True, True, False, True])
    ```

    ***数组的集合操作***

    |方法|描述|
    |:---|:---|
    |unique(x)|计算 x 的唯一值，并排序|
    |intersect1d(x, y)|计算 x 和 y 的交集，并排序|
    |union1d(x, y)|计算 x 和 y 的并集，并排序|
    |in1d(x, y)|计算 x 中的元素是否包含在 y 中，返回一个布尔值数组|
    |setdiff1d(x, y)|差集，在 x 中但不在 y 中的 x 的元素|
    |setxor1d(x, y)|异或集，在 x 或 y 中，但不属于 x、y 交集的元素|

### 使用数组进行文件输入和输出

NumPy 可以在硬盘中将数据以文本或二进制文件的形式进行存入硬盘或由硬盘载入。在这里，我们只讨论 NumPy 的内建二进制格式，因为大部分用户更倾向于使用 pandas 或其他工具来载入文本或表格数据。

`np.save` 和 `np.load` 是高效存取硬盘数据的两大工具函数。数组在默认情况下是以未压缩的格式进行存储的，后缀名是 `.npy`：

```python
In [1]: import numpy as np

In [2]: arr = np.arange(10)

In [3]: np.save('some_array', arr)
```

如果文件存放路径没写 `.npy`，后缀名会自动加上。硬盘上的数据可以使用 `np.load` 进行载入：

```python
In [4]: np.load('some_array')
Out[4]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

可以使用 `np.savez` 并将数组作为参数，用于在未压缩文件中保存多个数组：

```python
# 注意，这儿后缀名不是 npy，而是 npz
In [5]: np.savez('array_archive.npz', a=arr, b=arr)
```

当载入一个 `npz` 文件，会获得一个字典型对象：

```python
In [6]: arch = np.load('array_archive.npz')

In [7]: arch['b']
Out[7]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

如果数据已经压缩好了，可以使用 `np.savez_compressed` 将数据存入已经压缩的文件（相比于 `np.savez` 得到的文件更小）：

```python
In [8]: np.savez_compressed('array_compressed.npz', a=arr, b=arr)
```

### 线性代数

线性代数，比如矩阵乘法、分解、行列式等方针数学，是所有数组类库的重要组成部分。NumPy 的数组方法和 numpy 命名空间中都有一个函数 `dot`（点乘），用于矩阵的操作：

```python
In [1]: import numpy as np

# shape(2, 3)
In [2]: x = np.array([[1., 2., 3.], [4., 5., 6.]])

# shape(3, 2)
In [3]: y = np.array([[6., 23.], [-1, 7], [8, 9]])

# x * y = shape(2, 2)
In [4]: x.dot(y)
Out[4]: array([[ 28.,  64.],
               [ 67., 181.]])

# 与上述等价
In [5]: np.dot(x, y)
Out[5]: array([[ 28.,  64.],
               [ 67., 181.]])

# (2, 3) * (3, 1) = (2, 1)
In [6]: np.dot(x, np.ones(3))
Out[6]: array([ 6., 15.])

# 特殊符号 @ 也作为中缀操作符，用于点乘矩阵操作：
In [7]: x @ np.ones(3)
Out[7]: array([ 6., 15.])
```

`numpy.linalg` 拥有一个矩阵分解的标准函数表，以及其他常用函数，例如求逆矩阵和行列式求解：

> 这些函数都是通过在 MATLAB 和 R 等其他语言使用的相同的行业标准线性代数库来实现的，例如 BLAS、LAPACK 或英特尔专有的 MKL（数学核心库）（是否使用 MKL 取决于使用 NumPy 的版本）

```python
In [1]: import numpy as np

In [2]: from numpy.linalg import inv, qr

In [3]: X = np.arange(4).reshape((2, 2))

In [4]: X
Out[4]: array([[0, 1],
               [2, 3]])

# X.T.dot(X) 是 X 的转置 X.T 与它自身的点乘积
In [5]: mat = X.T.dot(X)

In [6]: mat
Out[6]: array([[ 4,  6],
               [ 6, 10]])

# 求方阵的逆矩阵
In [7]: inv(mat)
Out[7]: array([[ 2.5, -1.5],
               [-1.5,  1. ]])

# 方阵乘以它的逆矩阵等于同阶单位矩阵
In [8]: mat.dot(inv(mat))
Out[8]: array([[1., 0.],
               [0., 1.]])

# 计算 QR 分解
In [9]: q, r = qr(mat)

# r 为上三角矩阵
In [10]: r
Out[10]: array([[ -7.21110255, -11.64870412],
                [  0.        ,   0.5547002 ]])
```

***常用的 numpy.linalg 函数***

|函数|描述|
|:---|:---|
|np.diag|将一个方阵的对角（或非对角）元素作为一维数组返回，或者将一维数组转换成一个方阵，并且在非对角线上有零点|
|dot|矩阵点乘|
|trace|计算对角元素和|
|det|计算矩阵的行列式|
|eig|计算方阵的特征值和特征向量|
|inv|计算方阵的逆矩阵|
|pinv|计算矩阵的 Moore-Penrose 伪逆|
|qr|计算 QR 分解|
|svd|计算奇异值分解（SVD）|
|solve|求解 x 的线性系统 Ax = b，其中 A 是方阵|
|lstsq|计算 Ax = b 的最小二乘解|

### 伪随机数生成

`np.random` 模块填补了 Python 内建的 `random` 模块的不足，可以高效地生成多种概率分布下的完整样本值数组。例如，可以使用 `normal` 来获得一个 4×4 的正态分布样本数组：

```python
In [1]: import numpy as np

In [2]: samples = np.random.normal(size=(4, 4))

In [3]: samples
Out[3]: array([[ 0.5547801 ,  0.12259633, -1.32820028, -1.12457278],
               [-1.81902093, -0.00925318, -0.06991161, -0.87687667],
               [ 0.18013267, -1.97683063,  1.24371569,  0.52512112],
               [-2.13189018,  0.38879294,  0.88144575, -0.43554783]])
```

Python 内建的 `random` 模块一次只能生成一个值，`np.random` 在生产大型样本时比纯 Python 的方式快了一个数量级：

```python
In [4]: from random import normalvariate

In [5]: N = 1000000

In [6]: %timeit samples = [normalvariate(0, 1) for _ in range(N)]
721 ms ± 16.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [7]: %timeit np.random.normal(size=N)
28.9 ms ± 1.17 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

以上都是 *伪随机数*，都是由确定性行为的算法根据随机数生成器中的随机数种子生成的。可以通过 `np.random.seed` 更改 NumPy 的随机数种子：

```python
In [8]: np.random.seed(1234)
```

可以使用 `np.random.RandomState` 创建一个随机数生成器，使数据独立于其他的随机数状态：

```python
In [9]: rng = np.random.RandomState(1234)

In [10]: rng.randn(10)
Out[10]: array([ 0.47143516, -1.19097569,  1.43270697, -0.3126519 , -0.72058873,  0.88716294,  0.85958841, -0.6365235 ,  0.01569637, -2.24268495])
```

***np.random 中的部分函数列表***

> 后面内容会用到下面函数来一次性生成大型样本数组

|函数|描述|
|:---|:---|
|seed|向随机数生成器传递随机状态种子|
|permutation|返回一个序列的随机排列，或者返回一个乱序的整数范围序列|
|shuffle|随机排列一个序列|
|rand|从均匀分布中抽取样本|
|randint|根据给定的由低到高的范围抽取随机整数|
|randn|从均值 0 方差 1 的正态分布中抽取样本（MATLAB 型接口）|
|binomial|从二项分布中抽取样本|
|normal|从正态（高斯）分布中抽取样本|
|beta|从 beta 分布中抽取样本|
|chisquare|从卡方分布中抽取样本|
|gamma|从伽马分布中抽取样本|
|uniform|从均匀 [0,1) 分布中抽取样本|

### 示例：随机漫步

*随机漫步* 的模拟提供了一个使用数组操作的说明性应用。现在来考虑一个简单的随机漫步，从 0 开始，步进为 1 和 -1，且两种步进发生的概率相等。

下列是使用内建 random 模块利用纯 Python 实现的一个 1000 步的随机漫步：

```python
In [1]: import random

In [2]: position = 0

In [3]: walk = [position]

In [4]: steps = 1000

In [5]: for i in range(steps):
            step = 1 if random.randint(0, 1) else -1
            position += step
            walk.append(position)
```

对随机漫步的前 100 步可视化：

```python
In [6]: import matplotlib.pyplot as plt

In [7]: plt.plot(walk[:100])
[<matplotlib.lines.Line2D at 0x1b5ee089bb0>]
# 图省略
```

在 NumPy 中使用 `np.random` 模块一次性抽取 1000 次结果，然后计算累计值：

```python
In [8]: import numpy as np

In [9]: nsteps = 1000

In [10]: draws = np.random.randint(0, 2, size=nsteps)

In [11]: steps = np.where(draws > 0, 1, -1)

In [12]: walk = steps.cumsum()
```

我们从漫步轨道上提取一些统计数据，比如最大值、最小值等：

```python
In [13]: walk.min()
Out[13]: -9

In [14]: walk.max()
Out[14]: 60
```

更复杂的统计是第一次穿越时间，即随机漫步的某一步达到了某个特定值。这里假设我们要求漫步中是何时连续朝某个方向连续走了 10 步。`np.abs(walk) >= 10` 给我们一个布尔值数组，用于表明漫步是否连续在同一方向走了十步，但是我们想要的是第一次走了 10 步或 -10 步的位置。我们可以使用 `argmax` 来计算，该函数可以返回布尔值数组中最大值的第一个位置（True 就是最大值）：

```python
In [15]: (np.abs(walk) >= 10).argmax()
Out[15]: 297
```

> 请注意：这里使用 argmax 效率并不高，因为它总是完整地扫描了整个数组。

如果想要一次性模拟多次随机漫步，`np.random` 可以生成一个二维的抽取数组，并且一次性地跨行计算：

```python
In [16]: nwalks = 5000

In [17]: nsteps = 1000

In [18]: draws = np.random.randint(0, 2, size=(nwalks, nsteps))

In [19]: steps = np.where(draws > 0, 1, -1)

In [20]: walks = steps.cumsum(1)

In [21]: walks
Out[21]: array([[  1,   2,   3, ...,  46,  47,  46],
                [  1,   0,   1, ...,  40,  41,  42],
                [  1,   2,   3, ..., -26, -27, -28],
                ...,
                [  1,   0,   1, ...,  64,  65,  66],
                [  1,   2,   1, ...,   2,   1,   0],
                [ -1,  -2,  -3, ...,  32,  33,  34]], dtype=int32)
```

利用其他分布而不是等概率的上述掷硬币实验来验证随机漫步也是很容易的。只需要使用一个不同的随机数生成函数，比如 `normal`，再根据特定的均值和标准差即可生成正态分布下的随机步：

```python
In [22]: steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
```
