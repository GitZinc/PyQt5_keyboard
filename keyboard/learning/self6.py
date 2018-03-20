#coding=utf-8

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser)
import sys
from PyQt5.QtGui import QColor

class keyboard(QWidget):
	"""docstring for keyboard"""
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(500,500,500,550)
		self.setWindowTitle('keyboard siulator')

	#	self.key_a = QLabel('A',self)
    #   self.key_a.move(20,20)

		self.bt_q = QPushButton('Q',self)
		self.bt_q.move(40,20)

		self.bt_w = QPushButton('W',self)
		self.bt_w.move(80,20)

		self.bt_e = QPushButton('E',self)
		self.bt_e.move(140,20)

		self.bt_r = QPushButton('R',self)
		self.bt_r.move(200,20)

		self.tb = QTextBrowser(self)
		self.tb.move(320,20)

		self.show()

		self.bt_q.clicked.connect(self.showDialog)
		self.bt_w.clicked.connect(self.showDialog)
		self.bt_e.clicked.connect(self.showDialog)
		self.bt_r.clicked.connect(self.showDialog)


	def showDialog(self):
		sender = self.sender()
		if sender == self.bt_q:
			text = 'q'
			self.tb.insertPlainText(text)
		elif sender == self.bt_w:
			text = 'w'
			self.tb.insertPlainText(text)
		elif sender == self.bt_e:
			text = 'e'
			self.tb.insertPlainText(text)
		elif sender == self.bt_r:
			text = 'r'
			self.tb.insertPlainText(text)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = keyboard()
	sys.exit(app.exec_())