
#asdasd
class Room:


	def __init__(rId):

		self.clients=[]


	def addClient(s):
		self.clients.append(s)


	def broadcasting(msg):
		
		for sock in self.clients:

			sock.send(msg.encode('utf-8'))
