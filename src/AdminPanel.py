from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from src.Rec import *
from src.NewUser import *
from src.Model import *
class AdminPanelWin(QtWidgets.QWidget):
	def __init__(self, parent = None):

		self.m = Model()
		super().__init__(parent)
		self.ui = AdminPanel()
		self.ui.setupUi(self)
		self.Update()
		self.setWindowTitle("Админ-панель")
	def Click(self, name):
		self.m.DelUser(name)
		self.Update()
		
	def SaveBtn(self):
		mas = self.WichNamesNeedToCheck()
		if mas == False:
			return 0
		self.a = self.m.GetAllUsers()
		if self.CheckPass(mas) and self.FIOCheck(mas):
			pass

	def Err(self, text):
		msg = QMessageBox(self)
		msg.setWindowTitle("Ошибка!")
		msg.setText(text)
		msg.setIcon(QMessageBox.Warning)
		msg.exec_()
		
	def Update(self):
		for i in self.ui.butns:
			i.deleteLater()
		self.ui.butns = []
		for i in self.ui.labels:
			i.deleteLater()
		self.ui.labels = []
		for i in self.ui.lines:
			i.deleteLater()
		self.ui.lines = []
		for i in self.ui.layouts:
			i.deleteLater()
		self.ui.layouts = []
		counter = 0
		
		for i in self.m.GetAllNames()[1:]:
			
			self.ui.NewPos(self, f'(Пользователь {counter}): {i}', counter)
			x = (lambda c=i: self.Click(c))
			self.ui.butns[counter].clicked.connect(lambda checked, counter=i: x(counter))
			counter+=1
		
		self.ui.AddBtn.clicked.connect(self.AddUser)


	def Record(self):
		self.RecWin = RecWin()
		self.RecWin.show()

	def AddUser(self):
		self.NUWin = NewUserWin(self.m, self)
		self.NUWin.show()

class AdminPanel(object):

	def NewPos(self, Form, name, num, btnText = 'Удалить'):
	
		#self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
		#self.verticalLayout.setObjectName("verticalLayout")

		self.layouts.append(QtWidgets.QHBoxLayout())

		self.layouts[-1].setObjectName("horizontalLayout"+str(num))

		self.labels.append(QtWidgets.QLabel(self.scrollAreaWidgetContents))
		self.labels[-1].setObjectName("label"+str(num))
		self.layouts[-1].addWidget(self.labels[-1])

		
		self.butns.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
		self.butns[-1].setObjectName("pushButton"+str(num))
		self.layouts[-1].addWidget(self.butns[-1])
		
		self.lines.append(QtWidgets.QFrame(self.scrollAreaWidgetContents))
		self.lines[-1].setFrameShape(QtWidgets.QFrame.HLine)
		self.lines[-1].setFrameShadow(QtWidgets.QFrame.Sunken)
		self.lines[-1].setObjectName("line"+str(num))
		

		self.labels[-1].setText(self._translate("Form", name))

		self.butns[-1].setText(self._translate("Form", btnText))

		self.verticalLayout.addLayout(self.layouts[-1])
		self.verticalLayout.addWidget(self.lines[-1])
		if num == 0:
			return [self.labels[-1]]	
		return [self.labels[-1], self.butns[-1]]

	def setupUi(self, Form):
		self.labels = []
		self.layouts = []
		self.butns = []
		self.lines = []
		Form.setObjectName("Form")
		Form.resize(434, 503)
		self.gridLayout = QtWidgets.QGridLayout(Form)
		self.gridLayout.setObjectName("gridLayout")
		self.scrollArea = QtWidgets.QScrollArea(Form)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 641))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout.setObjectName("verticalLayout")
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

		self.AddBtn = QtWidgets.QPushButton(Form)
		self.AddBtn.setObjectName("AddBtn")
		self.gridLayout.addWidget(self.AddBtn)
		self.AddBtn.setText("Добавить полльзователя")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		self._translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(self._translate("Form", "Form"))
		