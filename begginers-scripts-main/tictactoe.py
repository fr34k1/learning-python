




theBoard = {'top-L': ' ', 
	'top-M': ' ', 'top-R': ' ',
 	'mid-L': ' ', 'mid-M':' ',
 	'mid-R': ' ', 'low-L': ' ', 
	'low-M': ' ', 'low-R': ' '}





def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-++--')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def validar_entrada(theboard):
	
	while True:
		move = input()
		
		#keys= move in theboard.keys()
		
		if theboard.get(move,0):
			break
		
		print("Entrada invalida")
	return move






turn = 'X'



def comprobar(turn):

		if theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn:
			return True
		elif theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn:
			return True
		elif theBoard['low-L'] == turn and theBoard['low-M'] == turn and theBoard['low-R'] == turn:
			return True
		elif theBoard['top-R'] == turn and theBoard['mid-R'] == turn and theBoard['low-R'] == turn:
			return True
		elif theBoard['top-M'] == turn and theBoard['mid-M'] == turn and theBoard['low-M'] == turn:
			return True
		elif theBoard['top-L'] == turn and theBoard['mid-L'] == turn and theBoard['low-L'] == turn:
			return True
		elif theBoard['top-L'] == turn and theBoard['mid-M'] == turn and theBoard['low-R'] == turn:
			return True
		elif theBoard['top-R'] == turn and theBoard['mid-M'] == turn and theBoard['low-L'] == turn:
			return True
		else:
			return False

	



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




printBoard(theBoard)






