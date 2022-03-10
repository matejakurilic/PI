import sys
import os
from helper import *
from parser import *
from filecollector import *

projectPath = ""

def setProjectDirectory(directory):
	if (os.path.isdir(directory) and os.access(directory, os.R_OK)):
		global projectPath 
		projectPath = directory
	else:
		print("Check if directory exists and whether it is accessible!")
		exit()

def main():
	num_of_arg = len(sys.argv)-1
	argument = sys.argv[1:]
	
	if (num_of_arg < 2):
		print("You forgot to set directory or language as an input argument!\n"
			"Run program like this: python3 ./main.py <lang> <path_to_dir>\n"
			"<lang> options are: " + str(languages))
		exit()

	if (argument[0] not in languages):
		print("<lang> options are: " + str(languages))
		exit()
	
	while (num_of_arg > 1):
		lang = argument[0]
		setProjectDirectory(argument[1])
		fc = FileCollector(projectPath, lang)
		fc.getFiles()
		par = Parser()
		par.parse(fc)
		argument.pop(0)
		num_of_arg -= 1

if __name__ == "__main__":
    main()