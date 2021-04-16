import random,sys


#### type(arg) devuelve el tipo de la variable

def game():

	

	numero = random.randint(1,20)
	
	while True:

		try:
			entrada = int(input("Elige un numero del 1 al 20\n"))

			if entrada == numero:
				print("Felicidades adivinaste el numero")
				break
			elif entrada>numero and entrada<=20:
				print("demaciado alto")

			elif entrada<numero and entrada>0:
				print("demaciado bajo")

			else:
				print("Entrada invalida: solo numeros del 1 al 20")
				
		except ValueError:
			print("Entrada invalida: tipo de dato Incorrecto")
			pass

		



game()


