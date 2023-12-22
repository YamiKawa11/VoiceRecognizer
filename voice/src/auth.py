from PyQt5 import QtCore, QtGui, QtWidgets
from src import Model
from src.AdminPanel import *
import sys
from src.User import *
from src.CheckUserVoice import *
from time import sleep
class auth(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.CheckUser)
        self.ui.lineEdit_3.returnPressed.connect(self.FLineEnter)
        self.ui.lineEdit_2.returnPressed.connect(self.CheckUser)
        self.base_line_edit = [self.ui.lineEdit_3, self.ui.lineEdit_2]
        self.m = Model()
        self.IsFirst = False
        if len(self.m.GetAllUsers()) == 0:
            self.IsFirst = True
            msg = QMessageBox(self)
            msg.setWindowTitle('Ошибка!')
            msg.setText("Зарегистрируйте адсмнистратора")
            self.ui.pushButton.setText("Зарегистрироваться")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

            self.ui.lineEdit_3.setText('admin')
            self.ui.lineEdit_3.setEnabled(False)
        self.setWindowTitle("Вход")

    def FLineEnter(self):
        self.ui.lineEdit_2.setFocus()


        
    def CheckUser(self):
        UName = str(self.base_line_edit[0].text())
        UPass = str(self.base_line_edit[1].text())
        if self.IsFirst:
            self.m.RegAdmin(UPass)
            self.AdminEnter()

        else:
            if self.m.IsPassCorrect(UName, UPass):
                if self.m.IsAdmin(UName):
                    self.AdminEnter()
                else:
                    self.UserEnter()
            else:
                self.WrongPass()

    def UserEnter(self):
        if len(self.m.GetAllNames()) > 2:
            self.win = CheckUserVoiceWin(str(self.base_line_edit[0].text()), self.m, self)
            self.win.show()
            self.close()
        else:

            self.win = UserWin(str(self.base_line_edit[0].text()), self.m)
            self.win.show()
            self.close()
            
            
    def AdminEnter(self):
        self.AdminWin = AdminPanelWin()
        self.AdminWin.show()
        self.close()
    def WrongPass(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('Ошибка!')
        msg.setText("Неверное имя пользователя или пароль.")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 190)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.label_2.setText(_translate("Form", "Имя пользователя:"))
        self.label_3.setText(_translate("Form", "Пароль:"))
        self.pushButton.setText(_translate("Form", "Войти"))

