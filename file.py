from token import *

class File():
	def __init__(self, path):
		self.path = path
		self.lines = []
		self.name = ""

	def readFile(self):
		file = open(self.path)
		self.name = file.name.split('/')[-1]
		self.lines = file.read()
		

