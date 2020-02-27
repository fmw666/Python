## flask 教程

&emsp;&emsp;简介：flask 是一款非常流行的 Python Web 框架，出生于 2010 年，作者是 Armin Ronacher。本来这个项目只是作者在愚人节的一个玩笑，后来由于非常受欢迎，进而成为一个正式的项目。

&emsp;&emsp;flask 自 2010 年发布第一个版本以来，大受欢迎，深得开发者的喜爱，并且在多个公司已经得到了应用，flask 能如此流行的原因，可以分为以下几点：

+ 微框架、简洁，只做他需要做的，给开发提供了很大的扩展性。
+ flask 和相关的依赖（Jinja2、Werkzeug）设计得非常优秀，用起来很爽。
+ 开发效率非常高，比如使用 SQLAlchemy 的 ORM 操作数据库可以节省开发者大量书写 sql 的时间。
+ 社会活跃度非常高，保证了一个良好的生态。

> 中文文档：[http://docs.jinkan.org/docs/flask/](http://docs.jinkan.org/docs/flask/)

1. **[安装 flask](#-安装-flask)**

1. **[连接数据库](#-连接数据库)**

1. **[项目搭建](#-项目搭建)**

1. **[模板语言](#-模板语言)**

1. **[分页实现](#-分页实现)**

1. **[实现增删改查](#-实现增删改查)**

---

### 🔨 安装 flask

+ 执行 pip 模块下载命令：

    ```python
    pip install flask
    ```

+ 查看当前 flask 版本：

    ```python
    import flask

    print(flask.__version__)
    ```

+ 官方示例的一段简单的 flask Web 应用：

    ```python
    # 导入模块
    from flask import Flask

    # 构造 app 对象
    app = Flask(__name__)

    # 路由定义（装饰器方式）
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        # app.run(debug=True)   # 开发模式中开启 debug，默认为未开启
        app.run()
    ```

    > 代码用 Python 解释器来运行。注意：确保你的应用文件名不是 flask.py ，因为这将与 Flask 本身冲突。本示例此脚本名均为 **app.py**

### 🛢 连接数据库

> 这里以 MySQL 数据库为例。关于 Python 如何操纵数据库，[详情]()

+ 下载 Flask ORM 模块 `SQLAlchemy`：

    ```python
    pip install Flask-SQLAlchemy
    ```

+ 下载 Python 第三方 MySQL 模块 `mysqlclient`：

    ```python
    pip install mysqlclient
    ```

+ 预先创建 MySQL 数据库

    ```sql
    -- 创建数据库
    create database net_news charset=utf8mb4;
    ```

+ 在 flask 项目中配置数据库

    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/net_news?charset=utf8'
    db = SQLAlchemy(app)

    class News(db.Model):
        __tablename__ = 'news'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), nullable=False)
        content = db.Column(db.String(2000), nullable=False)
        types = db.Column(db.String(10), nullable=False)
        image = db.Column(db.String(300), )
        author = db.Column(db.String(20), )
        view_count = db.Column(db.Integer)
        created_at = db.Column(db.DateTime)
        is_valid = db.Column(db.Boolean)

        def __repr__(self):
            return '<News %r>' % self.title
    ```

+ 生成数据库表命令：

    ```python
    from app import db

    db.create_all()
    ```

+ 插入数据库表命令：

    ```python
    from app import News
    from app import db

    new_obj = News(
        title = '标题',
        content = '内容',
        types = '推荐',
    )

    db.session.add(new_obj)
    db.session.commit()
    ```

+ 查询数据库表命令：

    ```python
    from app import News

    news = News.query.all()
    ```

### ⚙ 项目搭建

+ 项目结构（`*` 代表可选）

    ```bash
    ├── 项目文件夹
    │   ├── app.py          # 程序运行主入口
    │   ├── *models.py      # ORM 数据库生成
    │   ├── *forms.py       # 模板表单生成
    │   ├── *config.py      # 配置文件
    │   ├── db.sql          # 数据库文件
    │   ├── static          # 静态文件存放文件夹
    │   │   ├── css
    │   │   ├── js
    │   │   ├── ..
    │   ├── templates       # 模板页面存放文件夹
    │   │   ├── index.html
    │   │   ├── ..
    ```

+ 我们整篇教程将以一个 **新闻前台展示** 和 **后台数据管理** 项目为例

    ```bash
    ├── 项目文件夹
    │   ├── app.py              # 程序运行主入口
    │   ├── static              # 静态文件存放文件夹
    │   │   ├── css
    │   │   ├── js
    │   │   ├── ..
    │   ├── templates           # 模板页面存放文件夹
    │   │   ├── admin
    │   │   │   ├── add.html
    │   │   │   ├── admin_base.html
    │   │   │   ├── index.html
    │   │   │   ├── update.html
    │   │   ├── base.html
    │   │   ├── cat.html
    │   │   ├── detail.html
    │   │   ├── index.html
    ```


**[⤴ get to top](#flask-教程)**