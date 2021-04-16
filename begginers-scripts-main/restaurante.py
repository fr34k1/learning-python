
import random,os,sys




def preparar_platillos(principal,guarnicion,bebidas,postres):

	return list(zip(principal,guarnicion,bebidas,postres))




def mostrar_platillos(permutacion_platillos):

	guion = '-'*20
	print(guion+"platillos disponibles"+guion)

	for i in range(len(permutacion_platillos)):

			platillo = permutacion_platillos[i][0]+", "+permutacion_platillos[i][1]+", "+permutacion_platillos[i][2]+", "+permutacion_platillos[i][3]
			print("Platillo numero "+str(i+1)+"- "+ platillo)


######FUNCION PARA MOSTRAR LOS PLATILLOS
def menu():

	print("Elige una opcion")
	print("1-Mostrar platillos")
	print("2-elegir platillo")
	print("3-salir del programa\n")
##########################################


######FUNCION PARA ELEGIR UN PLATILLO XD
def elegir_platillo(permutacion_platillos):
	while True:

			try:
				num_platillo=int(input("que numero de platillo quieres"))
				if(num_platillo>len(permutacion_platillos))and num_platillo<len(permutacion_platillos):
					print("Opcion de platillo invalida")
					continue

				print(f"Has elegido la opcion nº {num_platillo} ")
				print(f"tu orden de {permutacion_platillos[num_platillo][0]}, {permutacion_platillos[num_platillo][1]} {permutacion_platillos[num_platillo][2]}")
				print("estara lista en 1 hora GG WP REPORT TEEMO HONOR SORACA XD")

			except ValueError:
				print("Entrada invalida solo se admiten numeros")
	





def programa():

		guarnicion=["papas fritas","ensalada de tomate y lechuga",]

		principal=["asado","pollo",'milanesa']

		postres =["flan","postre borracho","postre de chocolate","torta"]

		bebidas=["agua","coca-cola","sprite","fanta"]

		permutacion_platillos=preparar_platillos(principal,guarnicion,bebidas,postres)

		while True:
				#os.system("cls")
				menu()
				try:
					opcion = int(input(""))

						if opcion ==1:
							mostrar_platillos(permutacion_platillos)

						elif opcion == 2:
							elegir_platillo(permutacion_platillos)
						elif opcion == 3:
							print("saliendo del programa gracias por su visita! GG")
							sys.exit()
				except ValueError:
					print("Entrada invalida solo se admiten numeros")
				

	

programa()






















