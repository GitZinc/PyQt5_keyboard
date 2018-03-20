#!/usr/bin/python3
# coding = utf-8
#导入代码块
import sys
from PyQt5.QtWidgets import QApplication, QWidget
#程序本身被执行的时候才会运行
if __name__ == '__main__':
#创建一个应用程序对象，sys.argv使得程序可以从命令行启动
    app = QApplication(sys.argv)
# QWidget小部件是PyQt5中所有用户界面对象的基类。 
#我们提供了QWidget的默认构造函数。 默认构造函数没有父类。 没有父类口小部件称为窗口。
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('学点编程吧出品')
    w.show()

    sys.exit(app.exec_())