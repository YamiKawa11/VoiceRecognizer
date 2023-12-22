import pyaudio
import wave
import librosa
import librosa.display
import numpy as np
import soundfile as sf
from time import sleep
from PyQt5.QtWidgets import QMessageBox
from progress.bar import IncrementalBar
class Record:
	def __init__(self, time = 2, FileName = 'voice.wav'):
		
		self.p = pyaudio.PyAudio()
		self.seconds = time
		self.samplerate = 44100
		self.chunks = 1024
		self.FileName = FileName
	def GetDefLink(self, FName = "test.wav"):
		self.FileName = FName
		return self.FileName
	def OpenStream(self):
		self.wf = wave.open(self.FileName, 'wb')
		self.wf.setnchannels(1)
		self.wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
		self.wf.setframerate(self.samplerate)
		self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.samplerate, input=True)
	
	def RecordOnce(self):
		data = self.stream.read(self.chunks)
		
		self.wf.writeframes(data)
	def CloseStream(self):
		self.p.terminate()
		self.stream.close()
		self.wf.close()
		sleep(1)
		return self.FileName

	def StartRecord(self):
		
		with wave.open(self.FileName, 'wb') as wf:
			wf.setnchannels(1)
			wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
			wf.setframerate(self.samplerate)
			stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.samplerate, input=True)
			evrythk = self.samplerate // self.chunks * self.seconds
			bar = IncrementalBar('Recrording...', max = evrythk)
			for q in range(0, int(evrythk)):
				
				bar.next()

				wf.writeframes(stream.read(self.chunks))


			stream.close()
			self.p.terminate()
		return self.FileName
	
