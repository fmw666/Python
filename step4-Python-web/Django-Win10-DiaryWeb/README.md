> <h3><a href="#no-jump">《本文是基于 Win10 操作系统下 Django 开发的日记markdown自动模板生成篇》</a></h3>

.<br>.<br>.<br>.<br>.<br>

### 目录
1. [前期安装及其配置](#前期安装及其配置)
1. [编写日记的数据模型类](#编写日记的数据模型类)
1. [html前台展示页面](#html前台展示页面)
1. [xxxx](#xxxx)

.<br>.<br>

> 预览网站：[https://www.xxx.com/](#not-well)

.<br>.<br>

### *前期安装及其配置：*
+ **建立虚拟环境**
    ```shell
    # 在你想创建的项目文件夹下打开CMD，执行：
    D:\My-Project> virtualenv django_diary_md_env
    ```
+ **在 vs code 终端下开启虚拟环境**
    ```shell
    $ ls
    Include  Lib  pip-selfcheck.json  Scripts  tcl
    
    # 'code' 文件夹用于存放一系列测试代码 
    $ mkdir code
    
    # 'demo.py' 文件用于进行代码测试
    $ touch code/demo.py
    
    # 开启虚拟环境。（tips，输入's'后按下tab，然后再输入'a'按下tab）
    $ source Scripts/activate
    
    # 出现下面提示即成功开启虚拟环境
    (django_day_write_github)
    ```
+ **下载django**
    ```shell
    # 在当前虚拟环境终端下（后面所有均默认在虚拟环境下）
    $ pip install django
    ```
+ **建立django项目**
    ```django
    # 在项目文件夹下执行指令
    django-admin startproject web
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
    ~/crawlweb$ python3 manage.py startapp blog
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

---

.<br>.<br>
   
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

---

.<br>.<br>

### *html显示博客信息：*
+ **建立templates和static目录**
    
    templates文件夹用于存放html代码，static文件夹用于存放静态文件。在`crawlweb`目录下：
    ```bash
    crawlweb$ ls
    blog  crawlweb  db.sqlite3  manage.py
    crawlweb$ mkdir templates
    crawlweb$ mkdir static
    crawlweb$ ls
    blog  crawlweb  db.sqlite3  manage.py  static  templates
    ```
+ **编写前段展示页面**

    static文件夹下复制过去我们要的文件：
    ```shell
    static$ ls
    css  fonts  images  js
    ```
    
    在`./crawlweb/setting.py`中配置static和templates路径：
    ```python
    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates'),],
            'APP_DIRS': False,
            ...
        },
    ]
    ```
    ```python
    STATIC_URL = '/static/'
    # 在其下方添加：
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    ```

    templates文件夹下建立 `base.html` 文件：
    ```html
    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="zh-cn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{% block title %}{% endblock %}</title>
        <link rel="icon" href="{% static 'images/icon.png' %}">
        <link rel="stylesheet" href="{% static 'css/semantic.css' %}">
    </head>
    <body>
    
    </body>
    </html>
    ```
    
    建立视图函数。在`./blog/views.py`文件中：
    ```python
    from django.shortcuts import render
    from .models import BlogArticles

    # Create your views here.

    def blog_title(request):
        blogs = BlogArticles.objects.all()
        return render(request, 'blog/titles.html', {'blogs':blogs})
    ```
    
    建立基础模板。即在`./templates/blog/`文件夹下建立 `titles.html` 文件：
    ```html
    {% extends "base.html" %}
    {% load staticfiles %}
    {% block title %}博客专栏{% endblock %}

    {% block content %}
    <div class="ui very padded text segment" style="width:80%;">
        <h1 align="center">我的博客</h1>
        <div class="ui items">
            文章目录：
            <div class="item">
                <ul>
                    {% for blog in blogs %}
                        <li><a href="{{ blog.id }}">{{ blog.title }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
    {% endblock %}
    ```

    显示每篇文章：编辑`./blog/views.py`文件，继续建立视图函数。
    ```python
    def blog_article(request, article_id):
        article = BlogArticles.objects.get(id=article_id)
        pub = article.publish
        return render(request, 'blog/content.html',{'article':article,'publish':pub})
    ```

    创建与之对应的模板，在`./templates/blog/`文件夹下，建立`content.html`文件：
    ```html
    {% extends "base.html" %}
    {% load staticfiles %}
    {% block title %}文章内容{% endblock %}

    {% block content %}
    <div class="ui very padded text segment" style="width:80%;">
        <h1 align="center">{{ article.title }}</h1>
        <div class="ui container">
            {{ article.author.username }}
            {{ publish }}
            <div class="">
                {{ article.body }}
            </div>
        </div>
    </div>
    {% endblock %}
    ```
    
    接着配置URL，在`./blog/urls.py`中增添新的路径：
    ```python
    path('<int:article_id>/', views.blog_article, name='blog_article'),
    ```
    
    添加请求对象不存在时的异常处理，在`./blog/views.py`中：
    ```python
    from django.shortcuts import render, get_object_or_404
    from .models import BlogArticles
    
    def blog_article(request, article_id):
        # article = BlogArticles.objects.get(id=article_id)
        article = get_object_or_404(BlogArticles, id=article_id)
        pub = article.publish
        return render(request, 'blog/content.html',{'article':article,'publish':pub})
    ```
    
[返回目录↑](#目录) 

---

.<br>.<br>

### *重置后台模板与实现用户登录*
+ **重置后台模板**

    由于之前设定了模板访问位置只能在templates文件夹下，所以我们重新打开`127.0.0.1:8000/admin`会出现 [TemplateDoesNotExist](#welcome) 的报错信息。
    
    打开终端，查找文件：
    ```shell
    sudo find / -name "templates"
    ```
    
    找到`python3.6/site-packages/django/contrib/admin/templates`这个路径，复制完后然后继续进入目录：
    ```shell
    $ cd /home/fmw/.local/lib/python3.6/site-packages/django/contrib/admin/templates
    $ ls
    admin  registration
    $ sudo find / -name "crawlweb"
    # 找到并复制项目路径
    $ cp -r admin 项目路径/templates
    $ cp -r registration 项目路径/templates
    ```
    
    重启服务器，打开`127.0.0.1:8000/admin`，完美～
    
+ **用户登录**

    创建一个用于实现用户登录、退出、注册功能的应用：
    ```shell
    crawlweb$ python3 manage.py startapp account
    crawlweb$ ls
    account blog crawlweb db.sqlite3 manage.py static templates
    ```
    
    在`./crawlweb/settings.py`中配置新的应用：
    ```python
    INSTALLED_APPS = [
        ...,
        'blog',
        'account',
    ]
    ```
    
    在`./crawlweb/urls.py`中配置路径：
    ```python
    urlpatterns = [
        ...,
        path('account/', include('account.urls', namespace='account')),
    ]
    ```
    
    在`./account`目录中创建 `urls.py` 文件，并设置好本应用中的路径：
    ```python
    from django.urls import path
    from . import views

    from django.conf import settings
    
    from django.contrib.auth import views as auth_views

    app_name = 'account'

    urlpatterns = [
        path(r'login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'), # django内置的登录
    ]
    ```
    
    在`./templates/account/login.html`中编辑：
    ```html
    {% extends "base.html" %}
    {% load staticfiles %}
    {% block title %}登录{% endblock %}
    ```
    
    改写`./templates/base.html`文件中登录按钮跳转：
    ```html
    <a class="ui button" href="{% url 'account:user_login' %}">登录</a>
    ```
    
    登录后重定向设置：在`./crawlweb/settings.py`文件中设置`LOGIN_REDIRECT_URL`的值（放代码最后）
    ```python
    LOGIN_REDIRECT_URL = '/blog/'
    ```

[返回目录↑](#目录) 

---

.<br>.<br>

<div align="right">
    查看下一节→
</div>
