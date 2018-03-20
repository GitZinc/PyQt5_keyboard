#coding = 'utf-8'

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧-计算器')

        self.lcd =  QLCDNumber()
        #addWidget参数分别为，行、列、占用行、占用列、（对齐方式）
        grid.addWidget(self.lcd,0,0,3,0)
        #设置网格间距
        grid.setSpacing(10)

        names = ['Q', 'W', 'E','R', 'T' ,'Y' ,'U' ,'I' ,'O' ,'P',
                'A', 'S', 'D', 'F','G','H','J','K','L',':',
                'Z', 'X', 'C', 'V', 'B','N','M',',','.','?',
                ]       
        #   self.key_a = QLabel('A',self)
        #   self.key_a.move(20,20)
        positions = [(i,j) for i in range(4,7) for j in range(4,14)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)

        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())