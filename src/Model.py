import pandas as pd
import hashlib
from os import path
import numpy as np
class Model:

	def __init__(self):
		
		if path.exists('db.csv') == False:
			m = ['name', 'pass', 'fio', 'data']
			n = pd.DataFrame(columns = m)
			n.to_csv('db.csv')
		self.df = pd.read_csv('db.csv', index_col=0)

	def NewUser(self, name, password, fio, data):
		self.df.loc[len(self.df.index)]= [name, self.H(password), fio, data]
		self.df.to_csv('db.csv')

	def RegAdmin(self, password):
		self.df.loc[0] = ['admin', self.H(password), '', '']
		self.df.to_csv('db.csv')

	def IsPassCorrect(self, name, password):
		for i in self.df.to_numpy():

			if i[0] == name and i[1] == self.H(password):
				return True
		return False
	
	def IsAdmin(self, name):
		for i in self.df.fillna('').to_numpy():
			
			if name == i[0] and i[3] == '':
				return True
		return False

	def DelUser(self, name):

		for index, row in self.df.iterrows():
			if row[0] == name:
				self.df = self.df.drop(index)
				self.df.to_csv('db.csv')
				return 0
				#тут ещё можно уждалить снимок

	def GetAllUsers(self):
		return self.df

	def GetAllNames(self):
		return self.df['name']
	
	def GetAdmin(self):
		return(self.GetAllNames().to_numpy()[0])
	def __del__(self):
		pass
	def H(self,string):
		hash_object = hashlib.sha256(string.encode())
		return hash_object.hexdigest()