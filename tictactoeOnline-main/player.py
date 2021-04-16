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



