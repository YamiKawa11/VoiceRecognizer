from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from src import Record
import threading
import pandas as pd
from time import sleep
from pydub import AudioSegment
from src import Static
from src import VoiceTable as vt
from src import Static
from src.AdminPanel import * 


from src.User import *
import os
from sklearn import svm
from os import path

class CheckUserVoiceWin(QtWidgets.QWidget):
    def __init__(self,username, model, win, par = None):
        super().__init__(par)
        self.IsRecorder = True 
        self.z = win
        self.m = model
        self.u = username
        self.ui = CheckVoice()
        self.ui.setupUi(self)
        self.file = 'voice.wav'
        self.IsRecorder = True
        self.ui.label_3.setText('')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.seconds = 0
        self.part_delation = 3
        self.TeachModel()
        self.RV()
        self.setWindowTitle("Проверка")

    def RV(self):
        self.lastseconds = self.seconds
        self.seconds = 0
        self.ui.label_3.setText('Запись идёт!')
        self.ui.label.setText('00:00')
        self.timer.start(1000)
        thread = threading.Thread(target=self.RecVoice)
        thread.daemon = True
        thread.start()

    def RecVoice(self):
        r = Record.Record()            
        r.OpenStream()
          
        while(self.IsRecorder):
            r.RecordOnce()
            if self.lastseconds<self.seconds-self.part_delation:
                self.lastseconds = self.seconds
                if self.Compile() == self.u:
                    r.CloseStream()
                    self.IsRecorder = False
                    
    
    def Compile(self):
        s = Static.Static()
        mas = s.FromFile(self.file)
        self.pred = self.model.predict([mas])[0]
        return self.pred

    def TeachModel(self):
        tabletouser = {}
        for i in self.m.GetAllUsers().to_numpy():
            if type(i[3]) == type('a'):
                tabletouser[i[0]] = i[3]
        X = []
        y = []
        for table in tabletouser:
            for i in pd.read_csv(tabletouser[table], index_col=0).to_numpy():
                X.append(i)
                y.append(table)          
        self.model = svm.SVC()
        self.model.fit(X, y)
         
   




    def update_time(self):
        self.seconds += 1
        if self.seconds > 30:
            self.timer.stop()
            self.IsRecorder = False
            self.close()
            self.win = UserWin('Вы не прошли провеку!')
            self.win.show()
            return 0
        if self.IsRecorder == False:
            self.timer.stop()
            self.close()
            self.win = UserWin(self.u, self.m)
            self.win.show()
        else:  
            print(self.seconds)
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            self.ui.label.setText(f'{minutes}:{seconds:02}')

    def StopRec(self):
        self.timer.stop()
        sleep(1)
        self.file = r.CloseStream()
        stram_is_opened = True
            


class CheckVoice(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(486, 155)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Запись идёт!"))
        self.label_2.setText(_translate("Form", "Говорите, пока программа не поймёт, что это ваш голос"))
        self.label.setText(_translate("Form", "Время"))
