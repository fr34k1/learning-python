#from Playertic import Playertic
from tictactoe import Tictactoe

class RoomTic:

	def __init__(self,n_rom):
		self.tic = Tictactoe()
		self.nrom=n_rom
		self.player_1=None
		self.player_2=None
		self.turn='X'
	'''
		Esta funcion comprueba si la sala esta llena
	'''
	def isFull(self):
		if self.player_1 and self.player_2:
			return True 

		return False

		'''
			Esta funcion agrega un jugador a la sala
		'''
	def addPlayer(self,s):
		if self.isFull():
			return False 

		if  not self.player_1:
			self.player_1=s
			s.send("[Server Msg] Seras jugador X".encode('utf-8'))
			return  self.player_1
		else:
			self.player_2=s
			s.send("[Server Msg] Seras el jugador O".encode('utf-8'))
			return self.player_2
		



	def gameLoop(self):

		hasWinner=False
		nturns = 0
		while hasWinner or nturns<9:

			if self.turn == 'X':
				hasWinner=self.playTurn(self.player_1,self.player_2,'X')	
			else:
				hasWinner=self.playTurn(self.player_2,self.player_1,'O')	

			if hasWinner:
				break
		
		if nturns==8:

			player_1.send("[Server Msg] Empate guachin los dos son recontra loosers jajaja giles".encode('utf-8'))
			player_2.send("[Server Msg] Empate guachin los dos son recontra loosers jajaja giles".encode('utf-8'))


	def playTurn(self,turn,opponent,player):

		

		if self.tic.comprobar(player):
			turn.send("[Server Msg] Has ganado Felicidades".encode('utf-8'))
			opponent.send("[Server Msg] Perdiste Caramono jajaj gil ".encode('utf-8'))
			
			return True
		else:
			turn.send("[Player Turn]".encode('utf-8'))
			opponent.send("[Server Msg] Waiting for the openents movement....".encode('utf-8'))
			buff=turn.recv(1024).decode('ascii')
			self.tic.theBoard[buff]=player
			msg = "[Player Movement]"+buff
			opponent.send(msg.encode("utf-8"))
			print("jugada del player 1",buff)
			
			if player=="X":
				self.turn="O"
			else:
				self.turn="X"
		return False

	def encodeMsg(self,msg):
		return msg.encode('utf-8')