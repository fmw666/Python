> <h3><a href="#no-jump">《本文是基于 Ubuntu 18.04.2 LTS 操作系统下 Django 开发的博客实战爬坑篇》</a></h3>

.<br>.<br>.<br>.<br>.<br>


> 参考书籍：《跟老齐学 Python：Django实战》
### *前期安装及其配置：*
+ **下载django**
    ```shell
    pip3 install django
    ```
    ```python
    # 如果还没有安装pip3：
    sudo apt-get install python3-pip
    ```
+ **建立django项目**
    ```python
    # 在项目文件夹下执行指令
    django-admin startproject mysite
    ```

    但是！执行后会出现下面报错：
    ```shell
    zsh: command not found: django-admin
    ```

    ※解决方案：
    1. 使用指令查找执行文件所在目录：
        ```shell
        cd ~
        sudo find -name django-admin
        ```
        得到位置：`./.local/bin/django-admin`

    1. 在项目文件夹下执行指令：
        ```shell
        python3  ~/.local/bin/django-admin.py startproject mysite
        ```

    1. ok，大功告成！
+ **运行django项目**
    ```shell
    cd mysite
    python3 manage.py runserver 127.0.0.1:8000
    ```
    成功跑起～
+ **创建应用**

    项目已经创建好，现在要创建实现网站具体功能的“应用”（application）

    在之前创建的项目目录中，即 manage.py 文件所在目录下：
    ```shell
    ~/mysite$ ls
    db.sqlite3 manage.py mysite
    ~/mysite$ python3 manage.py startapp blog
    ~/mysite$ ls
    blog db.sqlite3 manage.py mysite
    ```
+ **网站配置**

    前面只是创建了应用，但必须把应用注册到项目中才能访问。

    Django 项目中，主管信息注册的文件是 `./mysite/settings.py`

    在 [INSTALLED_APPS](#welcome) 中新增 `blog`：
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    ]
    ```

    在 [LANGUAGE_CODE](#welcome) 中设置项目语言为 `zh-hans`：
    ```python
    LANGUAGE_CODE = 'zh-hans'
    ```

    在 [TIME_ZONE](#welcome) 中设置时区为 `Asia/Shanghai`：
    ```python
    TIME_ZONE = 'Asia/Shanghai'
    ```
### *编写博客的数据模型类：*


