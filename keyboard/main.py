# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from test import *

if __name__ == '__main__':
    '''
    主函数
    '''

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())