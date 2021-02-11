## 💬 重要的 Python 库

> 库/包的安装基于 **免费的 Anaconda 发布版** 来管理。

### NumPy

&emsp;&emsp;NumPy（<http://numpy.org>）是 *Numerical Python* 的简写，是 Python 数值计算的基石。

### Pandas

&emsp;&emsp;Pandas 的名字来源是 *panel data*，这是计量经济学中针对多维结构化数据集的术语。Pandas 也是 *Python data analysis*（Python 数据分析）自身的简写短语。

&emsp;&emsp;Pandas（<http://pandas.pyda.ta.org>）提供了高级数据结构和函数，这些数据结构和函数的设计使得利用结构化、表格化数据的工作快速、简单、有表现力。

### IPython 与 Jupyter

&emsp;&emsp;IPython 项目（<http://ipython.org>）开始于 2001 年，由 Fernando 发起，旨在开发一个更具交互性的 Python 解释器。

&emsp;&emsp;2014 年，Fernando 与 IPython 团队发布了 Jupyter 项目（<http://jupyter.org>），此项目旨在设计一个适用于更多语言的交互式计算工具。

&emsp;&emsp;IPython 系统目前可以作为一个内核用于在 Jupyter 中使用 Python。

### SciPy

&emsp;&emsp;SciPy（<http://scipy.org>）是科学计算领域针对不同标准问题域的包集合。以下是 SciPy 中包含的一些包：

+ scipy.integrate

    数值积分例程和微分方程求解器

+ scipy.linalg

    线性代数例程和基于 numpy.linalg 的矩阵分解

+ scipy.optimize

    函数优化器（最小化器）和求根算法

+ scipy.signal

    信号处理工具

+ scipy.sparse

    稀疏矩阵与稀疏线性系统求解器

+ scipy.special

    SPECFUN 的包装器。SPECFUN 是 Fortran 语言下实现的通用数据函数的包，例如 gamma 函数

+ scipy.stats

    标准的连续和离散概率分布（密度函数、采样器、连续分布函数）、各类统计测试、各类描述性统计

&emsp;&emsp;SciPy 和 NumPy 一起为很多传统科学计算应用提供了一个合理、完整、成熟的计算基础。

### scikit-learn

&emsp;&emsp;scikit-learn 项目（<http://scikit-learn.org>）诞生于 2010 年，目前已成为 Python 编程者首选的机器学习工具包。scikit-learn 包含以下子模块：

+ 分类：SVM、最近邻、随机森林、逻辑回归等

+ 回归：Lasso、岭回归等

+ 聚类：k-means、谱聚类等

+ 降维：PCA、特征选择、矩阵分解等

+ 模型选择：网格搜索、交叉验证、指标矩阵

+ 预处理：特征提取、正态化

### statsmodels

&emsp;&emsp;statsmodels（<http://statsmodels.org>）是一个统计分析包，与 scikit-learn 相比，statsmodels 包含经典的（高频词汇）统计学、经济学算法。它包含的模型如下：

+ 回归模型：线性回归、通用线性模型、鲁棒线性模型、线性混合效应模型等

+ 方差分析（ANOVA）

+ 时间序列分析：AR、ARMA、ARIMA、VAR 等模型

+ 非参数方法：核密度估计、核回归

+ 统计模型结果可视化