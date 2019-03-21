> <h3><a href="#no-jump">本文是基于 Ubuntu 18.04.2 LTS 操作系统下 Django 的博客开发实战爬坑篇</a> </h3>

.<br>.<br>.<br>.<br>.<br>


### *前期安装及其配置：*
+ 下载django
    ```python
    pip3 install django
    ```
    ```python
    # 如果还没有安装pip3：
    sudo apt-get install python3-pip
    ```
+ 建立django项目
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
    sudo find -name django-admin
    ```
