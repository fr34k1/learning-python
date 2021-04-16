#
from socket import socket,AF_INET,SOCK_STREAM,error,gethostname
import select
from threading import Thread
import sys 

import json




class ClientChat:


	def __init__(self):
		self.client  = socket(AF_INET,SOCK_STREAM)
		self.config = (gethostname(),40000)
		self.username = ''
	
	'''
	Esta funcion convierte un diccionario a formato cadena binaria  utf-8

	'''
	def parseMsg(self,dictionary):

		return json.dumps(dictionary).encode("utf-8")

		
	'''
	Manda un mensaje al servidor
	'''
	def sendData(self,data):
		try:

			self.client.send(self.parseMsg(data))

		except error as e:

			print("[Client Error] Connection with the server lost, cant send the message\n")

			self.client.close()

			sys.exit()
		
	
	'''
	Recibe un mensaje del servidor
	'''
	def recvData(self,sock):

		try:
			msg = sock.recv(1024)

		except :
			print("[Client Error] Connection with the server lost, cant receive the message\n")

			self.client.close()

			sys.exit()

		msg = json.loads(msg.decode("ascii"))

		#print(msg['body']['message'])
		print(f"{msg['body']['username']} says: {msg['body']['message']}\n")


	'''
	Esta funcion  captura y valida la entrada del usuario
	'''
	def getInput(self,msg=''):

		i=''
		while True:
			i= input(msg)
			if i =='':
				print("\nEntrada invalida\n")
				continue	
			else:
				break
		return i


	'''
	Esta funcion connecta el socket con el servidor
	'''
	def connect(self):

		try:
			self.client.connect(self.config)

			print("\n[Client Msg] Connection to the server successfully.",self.config[0],":",self.config[1],end='\n\n')

		except error as e:

			print("\n[Client Error] Connot establish connection with server. Check your Internet.\n\n")

			self.client.close()

			sys.exit()


	'''
	Esta funcion permite enviar mensajes al servidor  hasta que el usuario decida salir
	'''
	def clientLoop(self):

		self.connect()

		self.getUsername()
			
		while True:	
				
			# Pone a recivir los datos en un hilo aparte para que no se blokee la entrada y pueda recivir mensajes 
			t=Thread(target=self.recvData,args=[self.client])

			t.start()

			msg = self.getInput("\nType Something: ")

			

			if '!exit' in msg:
				self.sendData({'code':2})
				
				sys.exit()

			else:

				self.sendData({'code':1,'body':{'username':self.username,'message':msg}})
				
		



	def getUsername(self):

		self.username = self.getInput('Insert your username: ')

		self.sendData({'code':0,'body':{'username':self.username}})

		
		
client=ClientChat()


client.clientLoop()



