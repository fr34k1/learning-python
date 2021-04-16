
import sys,random,pyperclip,os,pprint,re




def generatePassword(length):
	caracters=(
		'ABCDEFGHYJKLMNOPRccSTUVWXYZ',
		'abcdefghijklmnopqrstuvwxyz'
		'1234567890',
		'!"·$%&/()=\'\\¡?¿<>^[]{}'
	)
	password=''

	for i in range(0,length):
		index=random.randint(0,2)
		index2=random.randint(0,len(caracters[index])-1)
		password+=caracters[index][index2]

	return password







'''

def storePassword(app,username,password):

	archivo=open("db.txt",'r+')
	string = archivo.read()

	data =(
		'app='+app,
		'username='+username,
		'password='+password
	)
	string='\n'
	string+=','.join(data)
	archivo.write(string)
	archivo.close()



def searchPassword(app):

	archivo=open("db.txt",'r')

	for line in archivo.readlines():
		result = line.split(',')

		if app==result[0].split('=')[1]:
			pyperclip.copy(result[2].split('=')[1])
			print("the password for", result[0],"hasbeen copied to the clipboard")
			archivo.close()
			sys.exit()
	print("Not result for ",app)
	archivo.close()


def usage():
	print("Usage:password-manager.py -(option) (param)")
	print('options availables')
	print("-g (length) generate a password and copy it to clipboard")
	print("-s (app name) search for a  password app and copy its to clipboard")
	print("-i  save a record in db and copy its password to clipboard")



def validateAppname():
	ex=re.compile(r'\w+')
	entrada = None
	


	while True:
		entrada = input("Ingresa el nombre de la aplicacion:\n")
		if len(entrada)>20:
			print("El nombre es muy largo")
			continue
		try:

			result = ex.search(entrada)
			if result.group():
				break
		except NameError:
			print("Malote tenes que ingresar bien los caracteres xD")
			continue
		
	return entrada

def init():

	if(len(sys.argv)<2):
		usage()
		sys.exit()
	elif(sys.argv[1]=='-g'):

		try:
			if(sys.argv[2]!=None and sys.argv[2].isdecimal()):
				password=generatePassword(int(sys.argv[2]))
				pyperclip.copy(password)
				print("Your password has been copied to the clipboard system")
		except ValueError:
			usage()
			sys.exit()

	elif sys.argv[1]=='-s':

		searchPassword(sys.argv[2])

	elif sys.argv[1]=='-i':

		app= validateAppname()
		username= input("Ingresa el nombre de usuario:\n")
		length=int(input("Ingresa la longitud de la password:\n"))
		password=generatePassword(length) 
		pyperclip.copy(password)
		storePassword(app,username,password)
		print("los datos se han guardados y tu contraseña se ha copiado al clipboard")
	else:
		usage()
		sys.exit()



init()'''