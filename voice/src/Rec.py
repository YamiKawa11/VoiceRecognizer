from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from src import Record
import threading
from time import sleep
from pydub import AudioSegment
from src import Static
from src import VoiceTable as vt
import os
from os import path
class RecWin(QtWidgets.QWidget):
    def __init__(self, Username, par = None):
        super().__init__(par)
        self.Uname = Username
        self.ui = Rec()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.RV)
        self.ui.pushButton_2.clicked.connect(self.StopRec)
        self.ui.pushButton_3.clicked.connect(self.SaveFile)
        self.ui.pushButton_3.setEnabled(False)
        self.file = 'voice.wav'


        self.ui.pushButton_2.setEnabled(False)
        self.IsRecorder = False
        self.ui.label_3.setText('')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.seconds = 0
        self.setWindowTitle("Запись")
    def RV(self):
        self.seconds = 0
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.label_3.setText('Запись идёт!')
        self.ui.label.setText('00:00')
        self.timer.start(1000)
        thread = threading.Thread(target=self.RecVoice)
        thread.daemon = True
        thread.start()

    def RecVoice(self):

        r = Record.Record()
        self.chunks = r.chunks
        sio = False
        if sio == False:
            r.OpenStream()
            sio = True
        self.IsRecorder = True   
        while(self.IsRecorder):
            
            r.RecordOnce()
        self.timer.stop()
        sleep(1)
        self.file = r.CloseStream()
        sio = True

    def update_time(self):
        self.seconds += 1
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        self.ui.label.setText(f'{minutes}:{seconds:02}')

    def StopRec(self):
        if self.seconds>3:

            self.ui.label_3.setText('')
            self.IsRecorder = False
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_3.setEnabled(True)
            
    def SaveFile(self):
        self.ui.pushButton_3.setEnabled(False)
        mas = self.CutFile(self.file)
        params = []
        s = Static.Static()
        v = vt.VoiceTable(self.Uname)
        for i in mas:
             v.AddPosition(s.FromFile(i))
        self.close()
    def closeEvent(self, event):
        self.ui.label_3.setText('')
        self.IsRecorder = False
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(True)
        if path.exists("voice.wav") == False:                
            self.Err('Вы не записали снимок голоса')
        event.accept()
        
    
        
    def Err(self, text):
        msg = QMessageBox(self)
        msg.setWindowTitle("Ошибка!")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def CutFile(self, filename):
        audio = AudioSegment.from_wav(filename)
        out = []
        num_chunks = len(audio) // self.chunks
        num = 6 #ЧИСЛО ЧАСТЕЙ
        part = int(num_chunks//num) 
        for i in range(num):
            start_time = i * self.chunks * part
            end_time = (i + 1) * self.chunks * part
            chunk = audio[start_time:end_time]
            output_file = f"{filename.replace('.wav', '')}_{i + 1}.wav"
            chunk.export(output_file, format="wav")
            out.append(output_file)
        return out




class Rec(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(486, 218)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Запись идёт!"))
        self.label_2.setText(_translate("Form", "Нажимите на кнопку и запишите свой голос в течении 20-30 секунд."))
        self.label.setText(_translate("Form", "Время"))
        self.pushButton.setText(_translate("Form", "Начать запись"))
        self.pushButton_2.setText(_translate("Form", "Остоновить запись"))
        self.pushButton_3.setText(_translate("Form", "Сохранить"))
