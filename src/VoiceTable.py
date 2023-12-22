from os import path
from os import mkdir
import pandas as pd
from sklearn import preprocessing
import numpy as np
class VoiceTable:



	def __init__(self, tablename):
		self.tablename = tablename
		if (path.exists('tables')) == False:
			mkdir("tables")
		self.TableFile = f"tables/{tablename}.csv"
		if path.exists(self.TableFile) == False:
			self.df = self.CSVFile()
			self.SaveTable(self.df)
		else:
			self.df = pd.read_csv(self.TableFile, index_col=0)
			self.SaveTable(self.df)

	def AddPosition(self, mas):
		#q = preprocessing.normalize([np.array(mas[1:])])
		q = [np.array(mas[1:])]
		self.df.loc[len(self.df.index)] = np.concatenate([[mas[0]], q[0]])
		self.SaveTable(self.df)
		
	def ClearTable(self):
		self.SaveTable(self.CSVFile())
	def Table(self):
		return self.df
	def CSVFile(self): #создаёт пустой дата фрейм с проименнованными колонками
		mfccs_Count = 128
		mas_columns = []
		for i in range(mfccs_Count):
			mas_columns.append(f"mm_{i}")
			mas_columns.append(f"ms_{i}")
		df = pd.DataFrame(columns = mas_columns)
		return df
	def SaveTable(self, table):
		table.to_csv(self.TableFile)


