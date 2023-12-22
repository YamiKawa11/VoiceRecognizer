import sys
from src import Model
from PyQt5 import QtCore, QtGui, QtWidgets
from src.auth import *
from src.AdminPanel import *
#from src.ShowUser import *



class VoiceCheckWin(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = n
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('src/icon.png'))
	mywin = auth()
	mywin.show()
	sys.exit(app.exec())

