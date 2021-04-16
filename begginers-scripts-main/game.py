

import sys,random


'''asdasd'''


def playTurn(player,player2):

	hits = player['attack'].split('-')
	attack = random.randint(int(hits[0]),int(hits[1]))
	bruteAttak = int(attack)-(int(attack)*(player2['armor']/10)/100)
	player2['life']-=bruteAttak
	print(f"""El jugador {player['name']} le ha inflingio 
{str(round(bruteAttak))}p de daño al jugador {player2['name']}
reduciendo su vida a {str(round(player2['life']))}p

		""")

	return player2['life']

def game():
	add_stats=(

		"+5 armor",
		"+3 daño"
	)

	player={
		'name':'player1',
		'class':'warrior',
		'habilities':{},
		'energy':100,
		'life':50,
		'attack':'3-10',
		'armor':10,
	}

	player2={
		'name':'player2',
		'class':'paladin',
		'habilities':{},
		'mana':100,
		'life':50,
		'attack':'5-10',
		'armor':10,

	}

	turno=player

	while True:

		
		actualPlayer=turno
		if turno['name']=='player1':

			actualPlayer['life']=playTurn(player,player2)
			turno=player
		else:
			
			actualPlayer['life']=playTurn(player2,player)
			turno=player2

		if actualPlayer['life'] <= 0:

			print("El jugador ",actualPlayer['name']," ha ganado el combate")
			break



game()
