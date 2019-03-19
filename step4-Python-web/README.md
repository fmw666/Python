# 💬Python Web
&emsp;&emsp;目前，Python的网络编程框架已经多达几十个，逐个学习它们并不现实。但这些框架在系统架构和运行环境中有很多共通之处，所以这一节我们会先介绍Web编程的网络基础，以及Python网络框架开发的常用知识，然后会学习四种主流的 Python web 框架。[支持快速建站的框架——Flask](#7-支持快速建站的框架flask)、[企业级开发框架——Django](#5-企业级开发框架django)、[高并发处理框架——Tornado](#6-高并发处理框架tornado)、[底层自定义协议网络框架——Twisted](#8-底层自定义协议网络框架twisted)

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute51.gif" width="150">
</div>

---

### *📑快捷目录：* 
[1. 网页编程语言——前端](#1-网页编程语言前端)

[2. 计算机网络](#2-计算机网络)

[3. 数据库及 ORM](#3-数据库及-ORM)

[4. Python网络框架](#4-Python网络框架)

[5. 企业级开发框架——Django](#5-企业级开发框架django)

[6. 高并发处理框架——Tornado](#6-高并发处理框架tornado)

[7. 支持快速建站的框架——Flask](#7-支持快速建站的框架flask)

[8. 底层自定义协议网络框架——Twisted](#8-底层自定义协议网络框架twisted)

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute1.jpeg" width="150">
</div>

---

## 1. 网页编程语言——前端
前端即网站前台部分，运行在PC端，移动端等浏览器上展现给用户浏览的网页。

如果你在之前还没系统的了解过前端，可以在我的另一个库中学习了解。[点我跳转](https://github.com/fmw666/Front-end/)

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute2.jpeg" width="150">
</div>

---

[返回目录⬆](#快捷目录)

## 2. 计算机网络
计算机网络是指将地理位置不同的具有独立功能的多台计算机及其外部设备，通过通信线路连接起来，在网络操作系统，网络管理软件及网络通信协议的管理和协调下，实现资源共享和信息传递的计算机系统。

如果你在之前还没系统的了解过网络相关知识，可以在我的另一个库中学习了解。[点我跳转](https://github.com/fmw666/Linux/Network/)

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute3.jpeg" width="150">
</div>

---

[返回目录⬆](#快捷目录)

## 3. 数据库及 ORM
### 数据库
为了方便管理和存储数据，对数据进行增删查改，我们往往要用到数据库，而且是基本是必学和必用的。

如果你在之前还没系统的了解过数据库相关知识，可以在我的另一个库中学习了解。[点我跳转](https://github.com/fmw666/Database-System)

### ORM（Object-Relational Mapping，对象关系映射）
ORM的作用是在关系型数据库和业务实体对象之间做一个映射，这样开发者在操作数据库的数据时，就不需要再去和复杂的 SQL 语句打交道，只需简单地操作对象地属性和方法。所有的 ORM 必须具备3方面地基本能力：映射技术、CRUD操作（Create增加、Retrieve读取、Update更新、Delete删除）和缓存优化。

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute4.jpeg" width="150">
</div>

---

[返回目录⬆](#快捷目录)

## 4. Python网络框架

---

[返回目录⬆](#快捷目录)

## 5. 企业级开发框架——Django
Django 是 Python 世界中应用最广泛、发展最成熟的 Web 框架。因为 Django 足够完整，所以使用 Django 本身就可以开发出非常完整的 Web 应用，而无须借助诸如 SQLAlchemy 等其他数据访问组件。

### 5.1 Django 综述
+ Django 于 2003 年诞生于美国堪萨斯（Kansas）州，最初是劳伦斯出版集团为了用来制作在线新闻 Web 站点而开发的。Django 于 2005 年加入了 BSD 许可证家族，成为开源网络框架。Django 根据比利时的爵士音乐家 [Django Reinhardt](https://en.wikipedia.org/wiki/Django_Reinhardt) 命名，*作者这样命名 Django 意味着 Django 能优雅地演奏（开发）功能丰富的乐曲（Web 应用）*。

<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute5.jpeg" width="100">
</div>

+ Django 相比于 Python 的其他 Web 框架，其功能是最完整的，Django 定义了服务发布、路由映射、模板编程、数据处理的一整套功能。这也意味着 Django 的模块之间紧密耦合，开发者需要学习 Django 自己定义的这一整套技术。Django 的主要特点如下。

    - **完整的文档：** 经过 10 多年的发展和完善，Django 有广泛的应用和完善的在线文档。
    - **集成数据访问组件：** Django 的 Model 层自带数据库 ORM 组件。
    - **强大的 URL 映射技术：** Django 使用正则表达式管理 URL 映射。
    - **后台管理系统自动生成：** 只需要几行简单的配置和代码就可以实现完整的后台数据管理 Web 控制台。
    - **错误信息非常完整。**
    
<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute6.jpeg" width="100">
</div>
    
+ Django 是遵循 MVC 架构的 Web 开发框架，其主要由以下几部分组成。

    - **管理工具（Management）：** 一套内置的创建站点、迁移数据、维护静态文件的命令工具。
    - **模型（Model）：** 提供数据访问接口和模块，包括数据字段、元数据、数据关系等的定义及操作。
    - **视图（View）：** Django 的视图层封装了 HTTP Request 和 Response 的一系列操作和数据流，其主要功能包括 URL 映射机制、绑定模板等。
    - **模板（Template）：** 是一套 Django 自己的页面渲染模板语言，用若干内置的 tags 和 filters 定义页面的生产方式。
    - **表单（Form）：** 通过内置的数据类型和控件生产 HTML 表单。
    - **管理站（Admin）：** 通过声明需要管理的 Model，快速生成后台数据管理网站。
    
<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute7.jpeg" width="100">
</div>

+ Django 的安装及测试
    
    ```python
    pip install django
    ```
    
    ```python
    #python
    >>>import django
    >>>print(django.VERSION)
    (2, 1, 7, 'final', 0)
    ```
    
<div align="center">
    <img src="https://github.com/fmw666/my-image-file/blob/master/images/anime/cute8.jpeg" width="100">
</div>

### 5.2 开发 Django 站点
+ 建立项目。在进行 Django 开发之前需要先用 django-admin 建立 Django 项目，语法如下：

    ```python
    django-admin startproject 站点名称
    ```

---

[返回目录⬆](#快捷目录)

## 6. 高并发处理框架——Tornado

---

[返回目录⬆](#快捷目录)

## 7. 支持快速建站的框架——Flask

---

[返回目录⬆](#快捷目录)

## 8. 底层自定义协议网络框架——Twisted

---

[返回目录⬆](#快捷目录)

---

<br><br><br>
<div align="right">
    <a href="../step5-Crawl">Python3 网络爬虫➡</a>
</div>
