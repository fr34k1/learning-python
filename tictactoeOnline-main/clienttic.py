

from os import system

from socket import socket,AF_INET,SOCK_STREAM,gethostname,error

from sys import exit

from time import sleep

from tictactoe import Tictactoe, Player


class Player:


	def __init__(self,name):
		self.name = name
		self.movement=None

	def name(self):
		return self.name

	def doPlay(self,movements):

		while True:
			self.movement = input("[Game Client] Do your movement\n")
			if self.movement in movements:
				break
			
			print("[Game Client] Entrada invalida")
		return self.movement


class ClientTic:

	def __init__(self):
		self.client = socket(AF_INET,SOCK_STREAM)
		self.host = gethostname()
		self.port = 5000
		self.tic= Tictactoe()
		self.player=None
		
	def encodeMsg(self,msg):
		return bytes(msg,'utf-8')


	def theBoard(slef):
		return self.theBoard

	def connect(self):
		try:
			self.client.connect((self.host,self.port))
			self.client.send(self.encodeMsg("Gracias bro"))
			while True:

				buff=self.client.recv(1024)
				res=str(buff)
				if "[Server Msg]" in res:
					self.handleServerMsg(res)
				elif "[Player Movement]" in res:
					self.handlePlayerMovement(res)
				elif "[Player Turn]" in res:
					self.handlePlayerTurns(res)

				sleep(3)
		except error as e:
			print(e)
			exit()
			raise e

	
	def handleServerMsg(self,res):
		if not self.player:
			if 'X' in res:
				#print("soy x")
				self.player = Player('X')
			elif 'O':
				#print("soy o")
				self.player = Player('O')
		print(res)

	def handlePlayerMovement(self,res):
		
		move = res.split(']')
		move=move[1].split("'")
		
		if(self.player.name=="X"):
			self.tic.printBoard(move[0],'O')
		else:
			self.tic.printBoard(move[0],'X')

	def handlePlayerTurns(self,res):
		move = self.player.doPlay(self.tic.theBoard.keys())
		system('cls')
		self.tic.printBoard(move,self.player.name)
		self.client.send(self.encodeMsg(move))





client=ClientTic()

client.connect()
