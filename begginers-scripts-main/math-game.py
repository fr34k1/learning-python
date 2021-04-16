

###################Math Game###################

import random,os


points={} #points dictionary
'''
	Esta funcion imprime un menu en pantalla
'''

def menu():

	print("Choose the game difficulty")

'''
	Esta funcion captura la entrada del usuario 
	y verifica que sea un numero si no es 
	un nu
'''
def userInput():

	entrada=None
	while True:
		
		try:
			entrada=int(input("Ingresa tu respuesta\n"))
			break
		except ValueError:
			print("Solo se admiten numeros")
	return entrada 


'''
	esta funcion trada de elegir el divisor y el dividendo 
	cuyo resultado de un numero perfecto osea sin coma flotante
'''
def perfectDivition(num,num2):
	num=random.randint(1,50)
	num2=random.randint(1,10)
	try:
		while not num%num2==0:
			num=random.randint(0,50)
			num2=random.randint(0,10)
		
		return (num,num2)
	
	except Exception as e:
		raise e
	



def makeOperation(operations,difficulty):

	dictWin = { '+' : 100, '-' :150,'*':215,'/':258}
	dictLoss = { '+' : 15, '-' :17,'*':30,'/':45}
	pointWin=0
	pointLoss=0
	if(difficulty<1):
		raise Exception("Invalid difficulty value")
		
	num = random.randint(0,100)
	strOperation= str(num)

	for i in range(difficulty):
		ranIndex = random.randint(0,len(operations)-1)
		pointWin += dictWin[operations[ranIndex]]
		pointLoss += dictLoss[operations[ranIndex]]
		num=random.randint(0,100)
		strOperation+=operations[ranIndex]+str(num)


	return (strOperation,pointWin,pointLoss)


''''
	Esta funcion elige una operacion random y la retorna
	esta operacion puede ser + - * o /

'''


################################ funcion principal del jeugo###################
def play():

	operations=('+','*','/','-')
	playerPoints=0
	gameDificulty=0
	wrong=0

	player={
		"name":"",
		"points":0,
		"correctas":0,
		"incorrectas":0
	}
	difficulty=1


	while wrong<=5:

		os.system('cls')
		
		strOperation,pointWin,pointLoss = makeOperation(operations,difficulty)
		print(strOperation,'=')
		result=eval(strOperation)

		userResponse=userInput()

		if result == userResponse:
			playerPoints += pointWin
			difficulty+=1
			print("Correct!")
		else:
			wrong+=1
			playerPoints -= pointLoss
			print("Wrong!")
		
	if playerPoints<0:
		playerPoints=0
	print(f"Tu resultado ha sido {playerPoints} pts")






play()
