
class Tictactoe:


	def __init__(self):
		self.theBoard = {'top-L': ' ', 
		'top-M': ' ', 'top-R': ' ',
	 	'mid-L': ' ', 'mid-M':' ',
	 	'mid-R': ' ', 'low-L': ' ', 
		'low-M': ' ', 'low-R': ' '}


	def printBoard(self,pos,player):
		if player == 'X':
			self.theBoard[pos]='X'
		else:
			self.theBoard[pos]='O'

		print(self.theBoard['top-L'] + '|' + self.theBoard['top-M'] + '|' + self.theBoard['top-R'])
		print('-+-+-')
		print(self.theBoard['mid-L'] + '|' + self.theBoard['mid-M'] + '|' + self.theBoard['mid-R'])
		print('-+-+-')
		print(self.theBoard['low-L'] + '|' + self.theBoard['low-M'] + '|' + self.theBoard['low-R'])


	




	def comprobar(self,turn):

		if self.theBoard['top-L'] == turn and self.theBoard['top-M'] == turn and self.theBoard['top-R'] == turn:
			return True
		elif self.theBoard['mid-L'] == turn and self.theBoard['mid-M'] == turn and self.theBoard['mid-R'] == turn:
			return True
		elif self.theBoard['low-L'] == turn and self.theBoard['low-M'] == turn and self.theBoard['low-R'] == turn:
			return True
		elif self.theBoard['top-R'] == turn and self.theBoard['mid-R'] == turn and self.theBoard['low-R'] == turn:
			return True
		elif self.theBoard['top-M'] == turn and self.theBoard['mid-M'] == turn and self.theBoard['low-M'] == turn:
			return True
		elif self.theBoard['top-L'] == turn and self.theBoard['mid-L'] == turn and self.theBoard['low-L'] == turn:
			return True
		elif self.theBoard['top-L'] == turn and self.theBoard['mid-M'] == turn and self.theBoard['low-R'] == turn:
			return True
		elif self.theBoard['top-R'] == turn and self.theBoard['mid-M'] == turn and self.theBoard['low-L'] == turn:
			return True
		else:
			return False

	




'''
	def play():



		for i in range(9):

			printBoard(theBoard)
			print('Turn for ' + turn + '. Move on which space?')
			
			move= validar_entrada(theBoard)
			
			theBoard[move] = turn
			
			if i>=4:
				print(turn)
			
				c_ganador=comprobar(turn)
				if c_ganador:
					print(f"El jugador {turn} Ha ganado ñaca ñaca xd")
					print("--------------FIN DEL JUEGO-------------")
					break


			if turn == 'X':
				turn = 'O'
			else:
				turn = 'X'



'''

