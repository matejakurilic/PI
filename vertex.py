class Vertex:
	def __init__(self, identification, name):
		self.identification = identification
		self.name = name 

	def isEqual(self, v):
		return self.name == v.name