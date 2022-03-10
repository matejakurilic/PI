from connections import *

class Parser:
	
	def parse(self, fc):
		class_methods = {}	
		for file in fc.files:
			file.readFile()
			#c = Connections(fc.projectDirectory)
			#c.walk(ast.parse(file.lines))
			for node in ast.walk(ast.parse(file.lines)):
				if isinstance(node, ast.FunctionDef):
					if hasattr(node, "parent"):
						class_methods[node.parent.name].append(node.name)
				if isinstance(node, ast.ClassDef):
					class_methods[node.name] = []
					for child in node.body:
						if isinstance(child, ast.FunctionDef):
							child.parent = node
		for k,v in class_methods.items():
			print(k + ' -> ' + str(v))



# methods for Java			
	def isMethod(self, line):
		declaration = [b'public ', b'private ', b'protected ']
		if (any(d in line.text for d in declaration) and b'(' in line.text and b');' not in line.text):
			line.lineType = 'method'
	
	def isInstance(self, line):
		if (b'= new ' in line.text):
			line.lineType = 'instance'

	def isClass(self, line):
		if (b'class ' in line.text):
			line.lineType = 'class'

	def isPackage(self, line):
		if (b'package ' in line.text):
			line.lineType = 'package'

	def isComment(self, line):
		if (b'/*' in line.text):
			if (b'*/' in line.text):
				return 'one'
			else: 
				return 'multiple'
		elif (b'//' in line.text):
			return 'one'


	def isImport(self, line):
		pass

