from src import Record as vr


import librosa
import librosa.display
import numpy as np

import scipy
from os import remove

class Static:
	def __init__(self):
		pass



	def Record(self, time):
		mas = self.StartRecord(time)
		return mas
	def FromFile(self, fileway):
		mas = []
		waves = librosa.load(fileway)
		mfccs = librosa.feature.mfcc(y=waves[0], sr=waves[1], n_mfcc=128)
		mfccs_mean=np.mean(mfccs,axis=1)
		mfccs_std=np.std(mfccs,axis=1)
		for i in mfccs_mean:
			mas.append(i)
		for i in mfccs_std:
			mas.append(i)
		self.file = fileway
		return mas
	def StartRecord(self, time = 0, file = None):
		mas = []
		if file == None:
			wav = vr.Record(time).StartRecord()
		else:
			wav = file
			self.file = file
		waves = librosa.load(wav)
		mfccs = librosa.feature.mfcc(y=waves[0], sr=waves[1], n_mfcc=128)
		mfccs_mean=np.mean(mfccs,axis=1)
		mfccs_std=np.std(mfccs,axis=1)
		for i in mfccs_mean:
		    mas.append(i)
		for i in mfccs_std:
		    mas.append(i)
		return mas


	def DelFile(self):
		remove(self.file)









	

	
	


	
