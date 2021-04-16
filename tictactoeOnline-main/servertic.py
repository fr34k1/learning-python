
from socket import *
from threading import Thread
from sys import exit

from time import sleep
#from server import ServerSocket

from RoomTic import RoomTic

class ServerTic:

	def __init__(self):	
		
		self.rooms=[]
		self.server = socket(AF_INET,SOCK_STREAM)
		self.host = gethostname()
		self.port = 5000
		self.server.bind((self.host,self.port))
		self.server.listen(20)
		print("SERVER LISTENING ON ",self.host,self.port)
		
	'''
		esta function es manejada por el hilo cada vez que se detecta una conexion se crea un hilo y cuando el 2do jugador se conecta
		se usa el hilo del socket del jugador 2 para dar lugar a la partida
	'''

	def clientHandler(self,s,addr):

		print("El cliente ",addr[0],":",addr[1]," se ha conectado\n")
		
		buff=s.recv(1024)
		message=str(buff)
		print(buff)

		lrooms = len(self.rooms)
		croom=None

		##a si no hay ninguna sala en la lista creamos una sala nueva y un jugador y la metemos en la lista
		if not lrooms:
			croom = RoomTic(lrooms-1)

			croom.addPlayer(s)
			self.rooms.append(croom)
			

		##sino evaluamos si la ultima sala esta llena en ese caso creamos
		## una nueva si no agregamos al jugador en la ultima sala
		else: 
			croom=self.rooms[lrooms-1]

			if not croom.addPlayer(s):
				croom = RoomTic(lrooms-1)
				croom.addPlayer(s)
				self.rooms.append(croom)
			else:
				self.rooms[lrooms-1].addPlayer(s)
		
			
				croom.gameLoop()
		



'''
	Funcion que pone a correr el servidor
'''
	
	def start(self):
		try:
			while True:

				s,addr = self.server.accept() ## Aceptamos una conexion nueva 
				t=Thread(target=self.clientHandler,args=(s,addr))
				t.start()

					
		except error as e:
			print(e)
			exit()
			raise e






server = ServerTic()


server.start()
