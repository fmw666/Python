## Tornado 教程

&emsp;&emsp;简介：我们会使用 tornado 搭建一个最基本的项目，然后用 MySQL 数据库去连接，并实现增删改查方法。最后我们会使用 tornado 的特性——异步，以及 MySQL 异步操作，来重新实现增删改查功能。

> 官方文档：[https://tornado-zh.readthedocs.io/zh/latest/index.html](https://tornado-zh.readthedocs.io/zh/latest/index.html)

1. **[安装 tornado](#-安装-tornado)**

1. **[项目搭建](#-项目搭建)**

1. **[模板语言](#-模板语言)**

1. **[连接数据库](#-连接数据库)**

1. **[实现增删改查](#-实现增删改查)**

1. **[异步——类视图方法](#-异步类视图方法)**

1. **[异步——MySQL 操作](#-异步mysql-操作)**

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

+ 项目结构

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

+ 基本框架

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
    from pymysql import connect

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

### 🔍 实现增删改查

> 前端传值基于 jQuery ajax

+ **增**

    *前端模板 html 展示*：

    ```html
    <table>
        <tr>
            <th>图书编号</th>
            <th>图书名字</th>
            <th>图书作者</th>
            <th>书中人物</th>
            <th>出版时间</th>
            <th>阅读数</th>
            <th>评论数</th>
        </tr>
        <tr class="addlist">
            <td><input type="text" value=""></td>
            <td><input type="text" value=""></td>
            <td><input type="text" value=""></td>
            <td><input type="text" value=""></td>
            <td><input type="text" value=""></td>
            <td><input type="text" value=""></td>
            <td><input type="text" value=""></td>
            <td><input class="add" type="text" value="增加"></td>
        </tr>
    </table>
    ```

    *前端通过 ajax 向后端传值：*

    ```javascript
    $(function() {
        $('.add').on('click', function() {
            var addTds = $('.addlist input')
            dict_data = {}
            for (var i=0; i<(addTds.length-1); i++) {
                if (i == 0) {
                    dict_data.btitle = addTds.eq(i).val()
                } else if (i == 1) {
                    dict_data.bauthor = addTds.eq(i).val()
                } else if (i == 2) {
                    dict_data.bperson = addTds.eq(i).val()
                } else if (i == 3) {
                    dict_data.bpub_date = addTds.eq(i).val()
                } else if (i == 4) {
                    dict_data.bread = addTds.eq(i).val()
                } else if (i == 5) {
                    dict_data.bcomment = addTds.eq(i).val()
                }
            }
            if (dict_data.name == "" | dict_data.author == "" | dict_data.hero == "" | dict_data.time == "" | dict_data.read == "" | dict_data.comment == "") {
                alert('输入内容不能为空！')
                return
            }
            $.post({
                url: '/',
                dataType: 'json',
                data: dict_data,
                success: function(dat) {
                    alert(dat.data)
                    window.location.reload()
                    // 清空所有输入框
                    for (var i=0; i<(addTds.length-1); i++) {
                        console.log(i)
                        addTds.eq(i).val("")
                    }
                }
            })
        })
    })
    ```

    *后端数据处理：*

    ```python
    def post(self):
        # 得到前端的数据，再插入到数据库

        # 1. 创建一个列表用以接收前端数据
        params_list = list()
        params_list.append(self.get_argument('btitle'))
        params_list.append(self.get_argument('bauthor'))
        params_list.append(self.get_argument('bperson'))
        params_list.append(self.get_argument('bpub_date'))
        params_list.append(self.get_argument('bread'))
        params_list.append(self.get_argument('bcomment'))

        # 2. 连接数据库，进行插入
        conn = connect(host='localhost', port=3306, database='book_manager', user='root', password='xxx', charset='utf8')
        cs1 = conn.cursor()
        cs1.execute("insert into books(btitle, bauthor, bperson, bpub_date, bread, bcomment) values (%s, %s, %s, %s, %s, %s)", params_list)
        # 提交数据
        conn.commit()
        # 关闭连接
        cs1.close()
        conn.close()

        # 3. 返回一个 json 格式的数据，或直接返回一个字典
        self.write('data': '添加成功')
    ```

+ **删**

    *前端模板 html 展示*：

    ```html
    {% for book in show_list %}
    <tr>
        <td><input type="text" value="{{ book[0] }}"></td>
        <td><input type="text" value="{{ book[1] }}"></td>
        ...
        <td class="del"><input type="button" value="删除"></td>
    </tr>
    {% end %}
    ```

    *前端通过 ajax 向后端传值：*

    ```javascript
    $(function() {
        $('.del').on('click', function() {
            result = $(this).siblings().eq(0).children('input').val()
            $.ajax({
                url: '/',
                dataType: 'json',
                type: 'delete',
                data: JSON.stringify({id: result}),
                success: function(dat) {
                    alert(dat.data)
                    $(this).parent().remove()
                    console.log($(this))
                    window.location.reload()
                }
            })
        })
    })
    ```

    *后端数据处理：*

    ```python
    import json
    from pymysql import connect

    ...

    def delete(self):

        # 1. 得到前端的数据 并 解码
        decode_body = self.request.body.decode('utf-8')

        # 2. 转成字典
        params_dict = json.loads(decode_body)

        # 3. 连接数据库
        conn = connect(host='localhost', port=3306, database='book_manager', user='root', password='xxx', charset='utf8')
        cs1 = conn.cursor()

        # 4. 执行 sql 更新语句
        cs1.execute("delete from books where id = %(id)s", params_dict)
        # 提交
        cs1.commit()
        # 关闭连接
        cs1.close()
        conn.close()

        # 5. 返回对应的数据
        self.write({"data": "删除成功"})
    ```

+ **改**

    *前端模板 html 展示*：

    ```html
    {% for book in show_list %}
    <tr>
        <td><input type="text" value="{{ book[0] }}"></td>
        <td><input type="text" value="{{ book[1] }}"></td>
        ...
        <td class="update"><input type="button" value="修改"></td>
    </tr>
    {% end %}
    ```

    *前端通过 ajax 向后端传值：*

    ```javascript

    ```

    *后端数据处理：*

    ```python
    import json
    from pymysql import connect

    ...

    # put、delete 数据都是在 body 中获取
    def put(self):

        # 1. 得到前端传过来的 body 数据 并 解码
        decode_body = self.request.body.decode('utf-8')

        # 2. 把字符串转成字典
        params_dict = json.loads(decode_body)

        # 3. 连接数据库
        conn = connect(host='localhost', port=3306, database='book_manager', user='root', password='xxx', charset='utf8')
        cs1 = conn.cursor()

        # 4. 执行 sql 更新语句
        cs1.execute("update books set btitle=%(btitle)s, bauthor=%(bauthor)s, bperson=%(person)s, bpub_date=%(bpub_date)s, bread=%(bread)s, bcomment=%(bcomment)s where id = %(id)s", params_dict)
        # 提交
        cs1.commit()
        # 关闭连接
        cs1.close()
        conn.close()

        # 5. 返回对应的数据
        self.write({"data": "更新成功"})
    ```

+ **查**

    *前端模板 html 展示*：

    ```html
    <table>
        <tr>
            <th>图书编号</th>
            <th>图书名字</th>
            <th>图书作者</th>
            <th>书中人物</th>
            <th>出版时间</th>
            <th>阅读数</th>
            <th>评论数</th>
        </tr>
        {% for book in show_list %}
        <tr>
            <td><input type="text" value="{{ book[0] }}"></td>
            <td><input type="text" value="{{ book[1] }}"></td>
            <td><input type="text" value="{{ book[2] }}"></td>
            <td><input type="text" value="{{ book[3] }}"></td>
            <td><input type="text" value="{{ book[4] }}"></td>
            <td><input type="text" value="{{ book[5] }}"></td>
            <td><input type="text" value="{{ book[6] }}"></td>
        </tr>
        {% end %}
    </table>
    ```

    *后端数据处理：*

    ```python
    def get(self):

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



### 💡 异步——类视图方法

### ⚡ 异步——MySQL 操作
