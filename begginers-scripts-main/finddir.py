import os,sys


class Find:

	def __init__(self,root):

		self.root=root
		self.dirs=os.walk(self.root)

	def findDir(self,dirname):
		
		found=False
		for i in self.dirs:
			if dirname in i[0]:
				print(f"The directory {dirname} is in ",i[0])
				found=True
				break

		if not found:

			print("No result for ",dirname)

	def findFile(self,filename):

		found=False
		for i in self.dirs:
			if filename in i[2]:
				print(f"The file {filename} is in ","./"+i[1][0])
				found=True
				break


		if not found:

			print("No result for ",filename)


def usage():
	print("usage: -d (root dirname) (directory to find)")
	print(" -f (root dirname) (file to find)")

def main():

	if len(sys.argv)<2:
		
		usage()

	if sys.argv[1] == '-d' and sys.argv[2] and sys.argv[3]:

		find = Find(sys.argv[2])
		find.findDir(sys.argv[3])
	elif sys.argv[1] == '-f' and sys.argv[2] and sys.argv[3]:
		
		find = Find(sys.argv[2])
		find.findFile(sys.argv[3])

	else:
		usage()



main()




