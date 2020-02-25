## Tornado 教程

&emsp;&emsp;简介：

> 官方文档：[https://tornado-zh.readthedocs.io/zh/latest/index.html](https://tornado-zh.readthedocs.io/zh/latest/index.html)

1. **[安装 tornado](#-安装-tornado)**

1. **[项目搭建](#-项目搭建)**

1. **[模板语言](#-模板语言)**

1. **[连接数据库](#-连接数据库)**

---

### 🔨 安装 tornado

+ 执行 pip 模块下载命令：

    ```python
    pip install tornado
    ```

+ 官方示例的一段简单的 tornado Web 应用：

    ```python
    # 导入模块
    import tornado.ioloop
    import tornado.web

    # 创建视图类
    class MainHandler(tornado.web.RequestHandler):

        # 请求方式：get、post、put、delete
        def get(self):
            # 返回给客户端/浏览器的内容
            self.write('Hello world!')


    # 程序配置
    def make_app():
        # 路由配置
        return tornado.web.Application([
            (r"/", MainHandler),
        ])


    # 程序入口
    if __name__ == "__main__":
        # 加载配置
        app = make_app()
        # 设置监听
        app.listen(8888)
        # 开启服务(ioloop 实际上是对 epoll 的封装)
        tornado.ioloop.IOLoop.current().start()
    ```

    > 未使用 tornado 的任何异步特性

### ⚙ 项目搭建

```
├── 项目文件夹
│   ├── server.py       # 程序运行主入口
│   ├── static          # 静态文件存放文件夹
│   │   ├── css
│   │   ├── js
│   │   ├── ..
│   ├── templates       # 模板页面存放文件夹
│   │   ├── index.html
│   │   ├── ..
```

```python
# 导入模块
import tornado.ioloop
import tornado.web

# 创建视图类
class MainHandler(tornado.web.RequestHandler):

    # 请求方式：get、post、put、delete

    # 导入 html 方式1：读取文件
    # def get(self):
    #     # 打开文件返回
    #     with open('./templates/index.html', 'rb') as f:
    #         content = f.read()
    #     self.write(content)

    # 导入 html 方式2：专门用来显示模板内容的方法
    def get(self):
        self.render('index.html')

    def post(self):
        self.write('post')

    def put(self):
        self.write('put')

    def delete(self):
        self.write('delete')

# 程序配置
def make_app():
    # 路由配置
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
        static_path = './static',   # 静态文件夹路径
        template_path = './templates'   # 模板路径
    )


# 程序入口
if __name__ == "__main__":
    # 加载配置
    app = make_app()
    # 设置监听
    app.listen(8888)
    # 开启服务(ioloop 实际上是对 epoll 的封装)
    tornado.ioloop.IOLoop.current().start()
```

### 📝 模板语言

+ 视图类中向模板页面传入参数：

    ```python
    def get(self):
        # 参数为：name、age、stu_list...
        self.render('index.html', name='fmw', age=12, stu_list=[1, 2, 3])
    ```

+ 模板语法之变量

    ```html
    {{ name }}<br>
    {{ age }}<br>
    {{ stu_list }}
    ```

+ 模板语法之标签

    ```html
    {{# for 标签 #}
    <ul>
        {% for stu in stu_list %}
        <li>{{ stu }}</li>
        {% end %}
    </ul>

    {# if 标签 #}

    {% if age > 50 %}
        <span>ok</span>
    {% else %}
        <span>no</span>
    {% end %}
    ```

### 🛢 连接数据库

> 这里以 MySQL 数据库为例。关于 Python 如何操纵数据库，[详情]()

+ 预先创建 MySQL 数据库以及相应表

    ```
    -- 创建数据库
    create database book_manager charset=utf8;

    -- 使用数据库
    use book_manager;

    -- 创建表
    create table books(id in unsigned primary key auto_increment, btitle varchar(30) not null, bauthor varchar(30) not null, bperson varchar(30), bpub_date date not null, bread int unsigned, bcomment int unsigned);

    -- 查看表结构
    desc books;

    -- 插入数据
    insert into books(btitle, bauthor, bperson, bpub_date, bread, bcomment) values
    ('红楼梦', '曹雪芹', '宝玉', '1980-5-1', 12, 34),
    ('西游记', '施耐庵', '悟空', '1986-7-24', 36, 50),
    ('水浒传', '吴承恩', '林冲', '1995-12-24', 20, 80),
    ('三国演义', '罗贯中', '曹操', '1980-5-1', 58, 24);

    -- 查看数据
    select * from books;
    ```

+ 安装 Python 操纵数据库模块

    ```python
    pip install pymysql
    ```

+ 读取数据库数据

    ```python
    import pymysql

    ...

    def get(self):
        # 读取数据库数据，传入给模板页面用以渲染

        # 1. 连接数据库
        conn = connect(host='localhost', port=3306, database='book_manager', user='root', password='xxx', charset='utf8')

        # 获得 Cursor 对象
        cs1 = conn.cursor()

        # 2. 执行查询的 sql 语句
        cs1.execute("select * from books;")
        # 得到返回的数据
        data = cs1.fetchall()

        # 3. 关闭数据库连接
        cs1.close()
        conn.close()

        # 传入模板页面
        self.render('index.html', show_list=data)
    ```