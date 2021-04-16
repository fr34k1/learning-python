
from socket import socket,AF_INET,SOCK_STREAM,gethostname
from threading import Thread



class ServerSocket:

	def __init__(self,ip,port,stype=''):
		self.ip=ip
		self.port=port
		self.socket=None
		self.stype=stype
		self.clients=[]

	def createSocket(self):
		self.socket=socket(AF_INET,SOCK_STREAM)
		self.socket.bind((self.ip,self.port))
		self.socket.listen(3)
		print("Server listening on ",self.ip,":",self.port)

	def run(self):
		self.createSocket()
		while True:
			s,addr = self.socket.accept()
			print("estegil se coencto ",addr[0])
			self.clients.append(s)
			t=Thread(target=self.handleClient,args=[s])
			t.run()

	def getClients(self):
		return self.clients


	def handleClient(self,sock):
		
		
		while True:
			
			sock.send(bytes(input("Escribile algo a este gil").encode()))
			while True:
				s=sock.recv(4096)
				if not s:
					break
				buff+=str(s)

			print(buff)
			
				
		return buff




server = ServerSocket("localhost",5000)

server.run()