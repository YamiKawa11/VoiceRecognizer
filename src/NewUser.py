from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from src.Rec import *
import os
from os import path

class NewUserWin(QtWidgets.QWidget):
	def __init__(self, Model, adminpanel ,parent = None):
		self.m = Model
		self.ADMINPANEL = adminpanel
		super().__init__(parent)
		self.ui = NewUser()
		self.ui.setupUi(self)
		self.ui.SaveBtn.clicked.connect(self.Save)
		self.Voice = None
		self.ui.pushButton.clicked.connect(self.RecordVoice)
		self.Isreced = False
		self.fieldnames = ['Имя пользователя', 'Пароль', 'Имя', 'Фамилия', 'Отчество']
		self.ISSAVEPRESSED = False
		self.setWindowTitle("Добавление пользователя")
	def RecordVoice(self):
		self.RefreshParams()
		if self.CheckAllField():
			self.r = RecWin(self.data[0])
			self.r.show()

	def EndSave(self):
		os.remove('voice.wav')
		for i in range(1, 7):
			os.remove(f'voice_{i}.wav')
		self.m.NewUser(self.data[0], self.data[1], (self.data[3]+'\t'+self.data[2]+'\t'+self.data[4]), f"tables/{self.data[0]}.csv")
		self.ADMINPANEL.Update()
		self.ISSAVEPRESSED = True
		self.close()
	

	def closeEvent(self, event):



		if self.ISSAVEPRESSED == False:
			reply = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите закрыть окно? Данные не сохранятся.',
										 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if reply == QMessageBox.Yes:
				event.accept()
			else:
				event.ignore()
		else:
			event.accept()



	def Save(self):
		
		self.RefreshParams()
		if self.CheckAllField():
			if self.IsVoiceRecorded():
				self.EndSave()

			
	def CheckAllField(self):

		for i in range(len(self.data)): 
			if self.Prov(self.data[i], self.fieldnames[i]): #тут мы проверили поля
				if self.IsUserAlready():
					return True
				else:
					return False
			else:
				return False
		return False
						


	def IsVoiceRecorded(self):
		if path.exists("voice.wav") == False:				
			self.Err('Вы не записали снимок голоса')
			return False
		return True

	def IsUserAlready(self):
		for i in self.m.GetAllNames():
			if self.data[0] == i:
				self.Err('Такое имя пользователя уже существует')
				return False

		return True

	def Prov(self, text, name):
		if ' ' in text:
			self.Err(f'В поле "{name}" обнаружен пробел')
			return False
		if len(text) > 50:
			self.Err(f'Поле "{name}" имеет слишком большую длинну')
			return False
		if text == '':
			self.Err(f'Поле "{name}" пустое')
			return False
		for i in text:
			if i in '/:*?»<>|':
				self.Err(f'Исползьвание специальных символов в поле {name}')
				return False
		return True
	def RefreshParams(self):
		self.data = [self.ui.lineEdit_5.text(), self.ui.lineEdit_4.text(),
		self.ui.lineEdit_2.text(), self.ui.lineEdit.text(), self.ui.lineEdit_3.text()]

	def Err(self, text):
		msg = QMessageBox(self)
		msg.setWindowTitle("Ошибка!")
		msg.setText(text)
		msg.setIcon(QMessageBox.Warning)
		msg.exec_()


class NewUser(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(850, 150)
		self.gridLayout = QtWidgets.QGridLayout(Form)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_5 = QtWidgets.QLabel(Form)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout.addWidget(self.label_5)
		self.lineEdit_5 = QtWidgets.QLineEdit(Form)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.horizontalLayout.addWidget(self.lineEdit_5)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_4 = QtWidgets.QLabel(Form)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_2.addWidget(self.label_4)
		self.lineEdit_4 = QtWidgets.QLineEdit(Form)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.horizontalLayout_2.addWidget(self.lineEdit_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.verticalLayout_3.addLayout(self.verticalLayout_2)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_3.addWidget(self.pushButton)
		self.horizontalLayout_6.addLayout(self.verticalLayout_3)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(Form)
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.lineEdit = QtWidgets.QLineEdit(Form)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_3.addWidget(self.lineEdit)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.lineEdit_2 = QtWidgets.QLineEdit(Form)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout_4.addWidget(self.lineEdit_2)
		self.verticalLayout.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.label_3 = QtWidgets.QLabel(Form)
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_5.addWidget(self.label_3)
		self.lineEdit_3 = QtWidgets.QLineEdit(Form)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.horizontalLayout_5.addWidget(self.lineEdit_3)
		self.verticalLayout.addLayout(self.horizontalLayout_5)
		self.horizontalLayout_6.addLayout(self.verticalLayout)
		self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

		self.SaveBtn = QtWidgets.QPushButton(Form)
		self.SaveBtn.setObjectName("SaveBtn")
		self.gridLayout.addWidget(self.SaveBtn)
		self.SaveBtn.setText('Сохранить')


		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_5.setText(_translate("Form", "Имя пользователя:"))
		self.label_4.setText(_translate("Form", "Пароль:"))
		self.pushButton.setText(_translate("Form", "Записать образ голоса"))
		self.label.setText(_translate("Form", "Фамилия:"))
		self.label_2.setText(_translate("Form", "Имя:"))
		self.label_3.setText(_translate("Form", "Отсчество:"))
