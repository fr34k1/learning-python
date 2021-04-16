
from random import randint
import re,os

''' Ahorcado de consolita guachin'''


class Game:

	def __init__(self,wordlist):

		self.wordlist=wordlist
		self.selected=None
		self.current=None
			
	def selectWord(self):
		self.selected=self.wordlist[randint(0,len(self.wordlist)-1)]
		self.current=[0]*len(self.selected)

	def printBoard(self):
		
		s=''
		for i in range(len(self.current)):
			if self.current[i]!=0:
				s+=self.current[i]
				s+=' '
			else:
				s+='_ '

		print(s)



	def findMatches(self,inp):
		accerts=0
		for i in range(len(self.selected)-1):
			
			if str(self.selected[i]).lower() == str(inp).lower():
				accerts+=1
				self.current[i]=self.selected[i]
		return accerts


	def start(self):
		player= Player("Ricardo Montaner")
		self.selectWord()
		print("Seleccionando un Nombre Aleatorio...\n")
		
		intents=1

		while  intents<len(self.selected)*2:
			self.printBoard()
			accerts=self.findMatches(player.doplay())
			if accerts>0:
				print("Cool you have accerted",accerts,' positions')
			
			intents+=1
			os.system("cls")

		if(intents==len(self.selected)*2):
			print("Perdiste gil vola de aca conche tu mae qlo merda xd")
		else:
			print("He felicidades ganaste una patada en el ojt jajaj por bolud xd")



class Player:

	def __init__(self,name):

		self.name = name

	def doplay(self):
		

		return input("Ingresa una letra\n")



game = Game(["Carlos",'Franco','Cabeza de p','Julian Mamarelli','Julian Rion'])



game.start()


