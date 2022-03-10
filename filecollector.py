from main import * 
from file import *

class FileCollector:
	def __init__(self, path, lang):
		self.projectDirectory = path
		self.exten = extension[lang]
		self.files = []

	def getFiles(self):
		for r, d, f in os.walk(self.projectDirectory):
			for file in f:
				if file.endswith(self.exten):
					self.files.append(File(os.path.join(r, file)))            		
