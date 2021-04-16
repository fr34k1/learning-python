import re


'''
	Funcion para filtrar malas palabras de una cadena
'''

def filter(words,string):


	for i in words:
		
		try:
			ex = re.compile(r''+i)
			print(ex)
			isThere = ex.search(string)
			result = isThere.group()
			
			print(i," esta wea esta aca",' n rep:',len(result))

		except NameError:
			print(i," esta wea esta aca")
			continue
			



filter(('putisima','perra','conchuda','gay'),'La re putisima putisima putisima madre hijo de la gran perra conchuda de tu hermana por que no te vas bien a la puta que te re pario gay rerimido de la sociedad')




