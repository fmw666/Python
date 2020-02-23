##  numpy 模块

&emsp;&emsp;Numpy（Numerical Python）是 Python 中做科学计算的基础库。重在数值运算，也是大部分 Python 科学计算库的基础，多用于在大型、多维数组上执行的数值运算。

+ 安装：

    ```python
    pip install numpy
    ```

### numpy 的创建

+ 使用 `np.array()` 创建：

    ```python
    import numpy as np
    
    # 创建一维数组
    arr1 = np.array([1, 2, 3, 4, 5])
    # 创建二维数组
    arr2 = np.array([1, 2, 3], [4, 5, 6])
    ```

    + 数组和列表区别：数组中存储的数据元素类型必须一致

+ 使用 `plt` 创建：

    ```python
    import matplotlib.pyplot as plt

    # 图片数据的读取(三维数组)
    img_arr = plt.imread('./demo.jpg')

    # 将一个三维的 numpy 数组显示成一张图片
    plt.imshow(img_arr)
    ```