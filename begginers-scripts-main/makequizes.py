
from os import path,makedirs
from sys import exit
from random import randint
import copy


def file2list(file):
	print(file)
	if not validateFile(file):
		return False

	print(file)
	quiz_file=open(file,'r',encoding='utf-8')
	qlist = quiz_file.readlines()
	quiz_file.close()
	return qlist
		
def validateFile(file):
	if not path.exists(file):
		return False
	if not path.isfile(file):
		return False 
	return True

def validateDir():
	pass

'''
	Funcion que me genera N archivos de quizes  
'''

def makeQuizes(desDir,nQuizes,quizFile):

	validateFile = quizQuestions=file2list(quizFile)

	if not validateFile:

		print(f"El archivo {quizFile} no existe o no es un archivo")
		exit()

	if not path.exists(desDir):
		if not makedirs(desDir):
			print("El directorio especificado no exite")
			print("No se ha podido crear el directorio")
			exit()
		print("El directorio especificado no exite")
		print("Se ha creado el directorio ",desDir)
		

	if not path.isdir(desDir):
			
		print("El directorio especificado no es un directorio")
		exit()


	quizList = file2list(quizFile)

	for i in range(0,nQuizes):

		check=copy.copy(quizList)
		file = open(path.join(desDir,f"quiz{i+1}.txt",'w')

		for j in range(0,len(quizList)-1):
			randIndex = randint(0,len(check)-1)
			file.write(check[randIndex])
			del check[randIndex]




makeQuizes('./',10,path.join('c:','users','fr34k','desktop','quiz.txt'))