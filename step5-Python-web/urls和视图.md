## flask的安装  
### pip安装flask：  
在cmd下```pip install flask```   
### 查看flask版本：  
在cmd下
```
python
>>>import flask
>>>print(flask.__version__)
```
## flask简介：   
```flask```是一款非常流行的```Python Web```框架，出生于2010年，作者是`Armin Ronacher`，本来这个项目只是作者在愚人节的一个玩笑，后来由于非常受欢迎，进而成为一个正式的项目。  
   
`flask`自2010年发布第一个版本以来，大受欢迎，深得开发者的喜爱，并且在[多个公司]()已经得到了应用，flask能如此流行的原因，可以分为以下几点：   

  
  - 微框架、简介、只做他需要做的，给开发提供了很大的扩展性。   
  - Flask和相关的依赖(Jinja2、Werkzeug)设计得非常优秀，用起来很爽。   
  - 开发效率非常高，比如使用`SQLAlchemy`的`ORM`操作数据库可以节省开发者大量书写`sql`的时间。   
  - 社会活跃度非常高。   
    
## 第一个flask程序：  
建立一个hello.py项目
```python
#encoding：utf-8

# 从flask这个框架中导入Flask这个类
from flask import Flask

# 初始化一个Flask对象
# Flask()
# 需要传递一个参数__name__
# 1. 方便flask框架去寻找资源
# 2. 方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)

# @app.route是一个装饰器
# @开头，并且在函数的上面，说明是装饰器
# 这个装饰器的作用，是做一个url与视图函数的映射
# 127.0.0.1:5000/  ->  去请求hello_world这个函数，然后将结果返回给游览器
@app.route('/')
def hello_world():
    return '我是第一个flask程序'
    
# 如果当前这个文件是作为入口程序运行，那么就执行app.run()    
if __name__ == '__main__':
    # app.run()
    # 启动一个应用服务器，来接受用户的请求
    # while True:
    # listen()
    app.run()
```
