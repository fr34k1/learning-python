
import sqlite3

def createTables():

	try:
		con = sqlite3.connect("reproductor.db")
		cursor = con.cursor()
		cursor.execute("CREATE TABLE rep_list (id INTEGER primary key autoincrement,name TEXT,artis path TEXT,weight REAL,duration TEXT)")
		
		con.close()

	except Exception as e:
		print(e)
	

def insertRow(title,path,weight,duration):

	string = title+','+path+','+weight+','+duration
	try:
		con = sqlite3.connect("reproductor.db")
		cursor = con.cursor()
		cursor.execute(f"INSERT INTO rep_list VALUES({string})")
		con.close()

	except Exception as e:
		print(e)


def selectAll():

	try:
		con = sqlite3.connect("reproductor.db")
		cursor = con.cursor()
		cursor.execute(f"SELECT * FROM rep_list")
		con.close()

		return cursor.fetchall()

	except Exception as e:
		print(e)







