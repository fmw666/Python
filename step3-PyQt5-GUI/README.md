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

[2. 控件](#2-控件)

[3. 布局管理](#3-布局管理)

[4. 事件和信号](#4-事件和信号)

[5. 使用 QSS 来美化界面](#5-使用-qss-来美化界面)

[6. 将 pyqt5 程序打包为 exe 可执行文件](#6-将-pyqt5-程序打包为-exe-可执行文件)

---

## 1. 初识和使用窗口

+ 下载依赖模块

    ```python
    pip install pyqt5
    ```

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

+ 我们一般把窗体信息封装成一个类，比如这样：

    ```python
    import sys
    from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            self.resize(250, 150)
            self.center()

            self.setWindowTitle('Center')
            self.show()

            # 后面可以再初始化一些控件（控件见下一节）


        def center(self):

            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())
    ```

    > center() 方法是将窗体居中于屏幕。

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>

## 2. 控件

+ 标签类：`QLabel`

+ 文本框类：`QLineEdit`、`QTextEdit`

+ 按钮类：`QPushButton`、`QRadioButton`、`QCheckBox`

+ 下拉列表框：`QComboBox`

+ 计数器：`QSpinBox`

+ 滑动条：`QSlider`

+ 窗口绘图类：`QPainter`、`QPen`、`QBrush`、`QPixmap`

+ 拖曳与剪贴板：`DragEnterEvent`、`DropEvent`、`QClipboard`

+ 日历控件：`QCalendar`

+ 日期时间控件：`QDateTimeEdit`

+ 菜单栏：`QMenuBar`

+ 工具栏：`QToolBar`

+ 状态栏：`QStatusBar`

+ 消息弹出式对话框：`QMessageBox`

+ 输入对话框：`QInputDialog`

+ 字体选择对话框：`QFontDialog`

+ 打开保存文件对话框：`QFileDialog`

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>

## 3. 布局管理

+ 盒布局（强适应性）

    ```python
    import sys
    from PyQt5.QtWidgets import (QWidget, QPushButton, 
        QHBoxLayout, QVBoxLayout, QApplication)


    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            okButton = QPushButton("OK")
            cancelButton = QPushButton("Cancel")

            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(okButton)
            hbox.addWidget(cancelButton)

            vbox = QVBoxLayout()
            vbox.addStretch(1)
            vbox.addLayout(hbox)

            self.setLayout(vbox)    

            self.setGeometry(300, 300, 300, 150)
            self.setWindowTitle('Buttons')    
            self.show()


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())
    ```

+ 栅格布局（最常用）

    ```python
    import sys
    from PyQt5.QtWidgets import (QWidget, QGridLayout, 
        QPushButton, QApplication)


    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            grid = QGridLayout()
            self.setLayout(grid)

            names = ['Cls', 'Bck', '', 'Close',
                    '7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '0', '.', '=', '+']

            positions = [(i,j) for i in range(5) for j in range(4)]

            for position, name in zip(positions, names):

                if name == '':
                    continue
                button = QPushButton(name)
                grid.addWidget(button, *position)

            self.move(300, 150)
            self.setWindowTitle('Calculator')
            self.show()


    if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())
    ```

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>

## 4. 事件和信号

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>

## 5. 使用 QSS 来美化界面

> 参考文章：[pyqt5中样式的介绍](https://blog.csdn.net/kuangshp128/article/details/87089446)

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>

## 6. 将 pyqt5 程序打包为 exe 可执行文件

+ 使用的打包工具是 pyinstaller

    ```python
    pip install pyinstaller
    ```

+ 执行指令

    ```python
    pyinstaller -Fw -i favicon xxx.py
    ```

    > -F：表示生成单个可执行文件；-w：表示去掉控制台窗口；-i：表示增添 icon 图标

<div align="right">
    <a href="#目录">返回目录⬆</a>
</div>

---

<br><br><br>
<div align="right">
    <a href="../step4-Algorithm">Python 数据结构与算法➡</a>
</div>