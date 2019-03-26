> <h3><a href="#no-jump">《本文是基于 Ubuntu 18.04.2 LTS 操作系统下 Django 开发的爬虫展示网站实战爬坑篇》</a></h3>

.<br>.<br>.<br>.<br>.<br>

### 目录
1. [前期安装及其配置](#)
1. [编写博客的数据模型类](#)
1. [Html显示博客信息](#)

> 参考书籍：《跟老齐学 Python：Django实战》
### *前期安装及其配置：*
+ **下载django**
    ```shell
    pip3 install django
    ```
    ```shell
    # 如果还没有安装pip3：
    sudo apt-get install python3-pip
    ```
+ **建立django项目**
    ```django
    # 在项目文件夹下执行指令
    django-admin startproject crawlweb
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
        python3  ~/.local/bin/django-admin.py startproject crawlweb
        ```

    1. ok，大功告成！
+ **运行django项目**
    ```shell
    cd crawlweb
    python3 manage.py runserver 127.0.0.1:8000
    ```
    成功跑起～
+ **创建应用**

    项目已经创建好，现在要创建实现网站具体功能的“应用”（application）

    在之前创建的项目目录中，即 manage.py 文件所在目录下：
    ```shell
    ~/crawlweb$ ls
    db.sqlite3 manage.py crawlweb
    ~/crawlweb$ python3 manage.py startapp crawlweb
    ~/crawlweb$ ls
    blog db.sqlite3 manage.py crawlweb
    ```
+ **网站配置**

    前面只是创建了应用，但必须把应用注册到项目中才能访问。

    Django 项目中，主管信息注册的文件是 `./crawlweb/settings.py`

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
    
[返回目录↑](#目录) 
   
### *编写博客的数据模型类：*
+ **数据模型类**

    在`./blog/models.py`中编写博客的数据模型类 BLog：
    ```python
    from django.db import models
    from django.utils import timezone
    from django.contrib.auth.models import User

    # Create your models here.

    class BlogArticles(models.Model):
        # 标题
        title = models.CharField(max_length=300)
        # 作者
        ''' 
        文章与用户之间关系为：一个用户对应多篇文章
        ForeignKey()反映了“一对多”的关系
        类User是BlogArticles对应对象
        related_name='blog_posts'的作用是运行通过类User反向查询到BlogArticles
        '''
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
        # 内容
        body = models.TextField()
        # 发布日期
        publish = models.DateTimeField(default=timezone.now)

        '''
        内部类
        规定了BlogArticles实例对象的显示顺序
        即按照publish字段值的倒叙显示
        '''
        class Meta:
            ordering = ('-publish',)

        def __str__(self):
            return self.title
    ```
    
    将来数据库表的基本结构就是按照上述各字段及其属性而定的。现在来根据数据模型建立数据库表：
    ```python
    crawlweb$ ls
    blog db.sqlite3 manage.py crawlweb
    crawlweb$ python3 manage.py makemigrations
    Migrations for 'blog':
        blog/migrations/0001_initial.py
    - Create model BlogArticles
    ```
    > 我们在 `blog/migrations` 目录中创建了一个 BlogArticles 模型。如果想查看它的本质，可以在 `crawlweb$` 中执行 `python3 manage.py sqlmigrate blog 0001`，会发现，其实都是我们的SQL语句。
    
    上面我们创建了一个能够建立数据库表的文件，下面开始真正的创建（默认的是sqlite3）数据库：
    ```python
    crawlweb$ python3 manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, blog, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying blog.0001_initial... OK
      Applying sessions.0001_initial... OK
    ```
    
    在命令行中打开我们的 SQLite可视化工具选择我们 crawlweb 目录下`db.sqlite3`文件来查看创建好的数据库 `blog_blogarticles`：
    ```bash
    sqlitebrowser
    ```
    
+ **使用 Django 默认的管理功能发布博客文章**

    创建超级管理员：
    ```python
    crawlweb$ python3 manage.py createsuperuser
    用户名 (leave blank to use 'fmw'): admin
    电子邮件地址: fmw19990718@qq.com
    Password: 
    Password (again): 
    Superuser created successfully.
    ```
    > 如果提示“密码长度太短”或“密码太常见”，会提示`Bypass password validation and create user anyway? [y/N]:`（绕过密码验证并创建用户?）如果你想就这样...就这样吧...选择Y
    
    运行服务器：
    ```shell
    crawlweb$ python3 manage.py runserver 127.0.0.1:8000
    ```
    
    输入用户名和密码进入系统，现在增加[添加博客文章](#welcome)栏，在`./blog/admin.py`中：
    ```python
    from django.contrib import admin
    from .models import BlogArticles

    # Register your models here.

    admin.site.register(BlogArticles)
    ```
    
    点击`Blog articles`右侧[＋增加](#welcome)来添加博客文章，由于在`.blog/models.py`中使用了 `django.utils.timezone`，为此需要安装一个 pytz 模块，用它来提供时区数值：
    ```python
    $ sudo pip3 install pytz
    ```
    
    让列表页信息变丰富，可以在`./blog/admin.py`中：
    ```python
    from django.contrib import admin
    from .models import BlogArticles

    # Register your models here.

    class BlogArticlesAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'publish')
        list_filter = ('publish', 'author')
        search_fields = ('title', 'body')
        raw_id_fields = ('author',)
        date_hierarchy = 'publish'
        ordering = ['publish', 'author']

    admin.site.register(BlogArticles,BlogArticlesAdmin)
    ```

[返回目录↑](#目录) 

### *Html显示博客信息：*
