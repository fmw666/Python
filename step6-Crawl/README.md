# 💬Python3 网络爬虫 
&emsp;&emsp;"得数据者得天下"。在大数据盛行的今天，你或许很容易能在网上看到什么"年度总结"，这些东西就是一系列的数据。网上还有很流行的词云，也是通过爬虫爬取下来的数据整理的。总之，会爬虫者得数据，得数据者得天下。

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/bluecutegirl1.gif" width="300">
</div>


## *📑 章节目录：*
#### [0. 正则表达式](#)

#### [1. 开发环境配置](#1-开发环境配置-1)

#### [2. 爬虫基础](#2)

#### [3. 基本库的使用](#3)

#### [4. 解析库的使用](#4)

#### [5. 数据存储](#5)

#### [6. Ajax 数据爬取](#6)

#### [7. 动态渲染页面爬取](#7)

#### [8. 验证码的识别](#8)

#### [9. 代理的使用](#9)

#### [10. 模拟登录](#10)

#### [11. App 的爬取](#11)

#### [12. pyspider 框架的使用](#12)

#### [13. Scrapy 框架的使用](#13)

#### [14. 分布式爬虫](#14)

#### [15. 分布式爬虫的部署](#15)

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/bluegirl1.jpg" width="150">
</div>

## 1. 开发环境配置
&emsp;&emsp;⚙ 安装库的方法有很多种，但我们选用最简单的第三方包管理工具 **[pip](#no-jump)** 来安装。使用的方法很简单，只需要打开命令行，输入：

```python
    pip install ***
```

<div align="right"><a href="#-章节目录">返回目录⬆</a></div>

### *📜 目录：*
&emsp;&emsp;**[1.1. 请求库的安装](#11-请求库的安装)**

&emsp;&emsp;&emsp;&emsp;[- requests 的安装](#1.1.1)

&emsp;&emsp;&emsp;&emsp;[- Selenium 的安装](#1.1.2)

&emsp;&emsp;**[1.2. 解析库的安装](#12-解析库的安装)**

&emsp;&emsp;**[1.3. 数据库的安装](#1.3)**

&emsp;&emsp;**[1.4. 存储库的安装](#1.4)**

---

### 1.1. 请求库的安装

<div align="center">
  <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/bluegirl2.jpg" width="100">
</div>

&emsp;&emsp;***📚 [requests 的安装](#1.1.1)*** <a name="1.1.1"></a>
 
  ```cmd
    pip install requests
  ```
    
&emsp;&emsp;***📚 [Selenium 的安装](#1.1.2)*** <a name="1.1.2"></a>
  
&emsp;&emsp;&emsp;&emsp;[Selenium](#no-jump) 是一个自动化测试工具，利用它我们可以驱动浏览器执行特定的动作，如[点击、下拉](#no-jump)等等操作，对于一些 [JavaScript](#no-jump) 渲染的页面来说，此种抓取方式非常有效。
    
  ```pip
      pip install selenium
  ```
    
&emsp;&emsp;***📚 [ChromeDriver 的安装](#1.1.3)*** 

&emsp;&emsp;&emsp;&emsp;暂时未更~
    
<div align="right"><a href="#-章节目录">返回目录⬆</a></div>
    
### 1.2. 解析库的安装

<div align="center">
  <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/bluegirl3.jpg" width="100">
</div>

&emsp;&emsp;***📚 [lxml 的安装](#1.2.1)*** <a name="1.2.1"></a>

&emsp;&emsp;&emsp;&emsp;[lxml](#no-jump) 是Python的一个解析库，支持 [HTML 和 XML 的解析](#no-jump)，支持 [XPtah](#no-jump) 解析方式，而且解析效率非常高。 

  ```cmd
      pip install lxml
  ```

---

[返回目录⬆](#-章节目录)


<br>


---

<br><br><br>
<div align="right">
    <a href="../step6-xxxx">Python科学计算——数据可视化➡</a>
</div>
