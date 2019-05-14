# 💬《Python之 GUI 编程——PyQt5》
&emsp;&emsp;图形用户界面（Graphical User Interface，简称 GUI，又称图形用户接口）是指采用图形方式显示的计算机操作用户界面。我们利用 GUI 编程可以写出很多实用的桌面应用程序，这样可以使我们更多的 python 函数和脚本更好的封装起来以此来方便用户的使用。

> ⭐ python 的图形界面库有很多，常用的有 [Tkinter](#welcome)、[PyQt](#welcome)、[wxPython](#welcome)、[PyGTK](#welcome)、[PySide](#welcome)。
>> 我们这里采用的是跨平台的 GUI 工具，Qt 所有类的 Python 封装 PyQt5 这个库。

---

🏷PyQt5 学习参考网站
+ [PyQt5 中文教程](https://maicss.gitbooks.io/pyqt5/content/)

    - [项目 github 地址](https://github.com/maicss/PyQt5-Chinese-tutorial)
    
+ [PyQt 官方网站](https://riverbankcomputing.com/news)

## 目录
[1. 初识和使用窗口](#1-初识和使用窗口)

[2. 打印文本](#2-打印文本)

[3. 绘制图形](#3-绘制图形)

[4. 制作pie游戏](#4-制作pie游戏)

---

## 1. 初识和使用窗口

+ 简单的窗口

```python
# 这里引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件。
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每个PyQt5应用都必须创建一个应用对象。
    # sys.argv是一组命令行参数的列表。
    # Python可以在shell里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)

    # QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。
    w = QWidget()
    # resize()方法能改变控件的大小，这里的意思是窗口宽250px，高150px。
    w.resize(250, 150)
    # move()是修改控件位置的的方法，它把控件放置到屏幕坐标的(300, 300)的位置。
    # 注：屏幕坐标系的原点是屏幕的左上角。
    w.move(300, 300)
    # 我们给这个窗口添加了一个标题，标题在标题栏展示。
    w.setWindowTitle('Simple')
    # show()能让控件在桌面上显示出来。
    w.show()

    # 主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
    # 当调用exit()方法或直接销毁主控件时，主循环就会结束。
    # sys.exit()方法能确保主循环安全退出，外部环境能通知主控件怎么结束。
    # exec_()之所以有个下划线，是因为exec是一个Python的关键字。
    sys.exit(app.exec_())
```

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>
