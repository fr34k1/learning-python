from socket import *
from select import select,error as serror
from Room import Room
from threading import Thread
from time import sleep
import sys
import json



class ServerChat:
	def __init__(self):
		self.server = socket(AF_INET,SOCK_STREAM)
				#self.rooms = [Room(len(self.room))]
		self.sockets=[self.server]

	def listening(self):
		try:
			self.server.bind((gethostname(),40000))
			self.server.listen()
			print(f"Servidor escuchando en {gethostname()}:40000")
			self.server.setblocking(False)
		except serror as e:
			print(e)
			sys.exit()
		


	def start(self):

		self.listening()

		while 1:
			sleep(3)
			readable,writable,inerror=select(self.sockets,[],[])
			'''
				recorre todos los sockets conectados
				que mandaron
				algun tipo de mensaje al server
			'''
			for sock in readable:

				if sock == self.server:
					'''
						Comprueba si es un cliente nuevo
						si es un cliente nuevo acepta la conexion 
						y lo agrega al arreglo
						de cleintes conectados
					'''
					self.handleNewConnections(sock)
				
				else:
					'''
						Si no es un cliente nuevo entonces
						recibe el mensaje y se lo manda a los
						cleintes conectados
					'''
					msg = self.recvData(sock)
					
					'''
						verifica el codigo del mensaje 
						y realiza una accion dependiendo
						de el
					'''
					if msg['code'] == 0: 
						#si el cod es 0 entonces se trata de un usuario nuevo
						#manda un mesaje a todos los cleintes informando la nueva conexion
						
						self.handleNewClient(sock,msg['body'])
						
					elif msg['code'] == 1:
						#si es 1 entonces se trata de un mensaje al chat
						#manda un mensaje a todos los clientes con el mensaje
						#print(msg)
						self.handleChatMessage(sock,msg['body'])
					elif msg['code']==2:
						#si es 2 termina el proceso del servidor. Solo para debuggear
						sys.exit()
					else:
						print("Hola mama estoy en la tele!!")
						pass
				







	def broadcast(self,sock,msg):
		for i in range(1,len(self.sockets)):
			
				if self.sockets[i]!=sock:
					#print("mandando un msg a ",self.sockets[i])
					self.sendData(self.sockets[i],msg)

	def equal(self,sock,msg):

		#print(type(msg),"a123123123")

		self.sendData(sock,{'code':1,'body':{'message':f"Bienvenido Al servidor {msg['username']}"}})


	def sendData(self,sock,msg):
		try:
			sock.send(json.dumps(msg).encode("utf-8"))
		except serror as e:
			print("Se ha desconectado un cliente")
			self.broadcast(sock,{'code':1,'body':{'message':f"Se ha desconectado un username "}})
			self.sockets.remove(sock)
			

	def recvData(self,sock):
		try:
			data = sock.recv(1024)
			return json.loads(data.decode('ascii'))
						
		except serror as e:

			print("Se perdio la conexion con el socket")

			self.broadcast(sock,{'code':1,'body':{'message':f"Se ha desconectado un username "}})

			self.sockets.remove(sock)

		return False 
		
		
	'''
	Acepta y Agrega un socket a la lista de clientes conectados 
	'''
	def handleNewConnections(self,sock):
		s,addr = sock.accept()		
		print(f"Se ha conectado el cliente {addr[0]}:{addr[1]}")		
		#s.send("Wellcome to the fucking server".encode('utf-8'))		
		self.sockets.append(s)
	
	'''
	Hace saber a todos los clientes que se conecto un nuevo cliente
	'''
	def handleNewClient(self,sock,msg,equal=None):
		#print(msg['username'])
		self.broadcast(sock,{'code':1,'body':{'message':f'El usuario {msg["username"]} se ha unio al chat'}})

	'''
	Manda un mensaje a todos los clientes
	'''
	def handleChatMessage(self,sock,msg):
		print(f"El usuario {msg['username']} dijo: {msg['message']}")
		self.broadcast(sock,{'code':1,'body':{'username':msg['username'],'message':msg['message']}})


server = ServerChat()

server.start()