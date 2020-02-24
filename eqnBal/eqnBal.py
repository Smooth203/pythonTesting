import os

R = [] #Reactants
P = [] #Products

def areYouSure():
	ans = input("Is this the correct equation?\n" + str(R) + "-->" + str(P) + "\n'y' for yes, 'n' for no")
	if ans == 'y':
		print("cool")
	elif ans == 'n':
		print("okay..")
	else:
		print("Try again")
		os.system('cls')
		areYouSure()

def addR():
	r = input("What is the new reactant? (If done, answer, 'n')")
	if r == 'n':
		addP()
	elif r == '':
		print("Not Added")
		addR()
	else:
		R.append(r)
		addR()

def addP():
	p = input("What is the new product? (If done, answer, 'n')")
	if p == 'n':
		areYouSure()
	elif p == '':
		print('Not Added')
		addR()
	else:
		P.append(p)
		addP()

def start():
	addR()


start()