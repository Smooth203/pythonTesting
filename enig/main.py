from string import ascii_lowercase
import os

alphabet = ascii_lowercase
plugboard = ''
rotors = []

def setPB():
	pb = ''
	for letter in alphabet:
		hold = True
		while hold:
			result = input(letter + ' = ')
			if result in alphabet and len(result) == 1 and result not in pb:
				hold = False
		pb = pb + result
	return pb

def savePB():
	name = input('What is the file name? ')
	f = open('plugboardSettings/' + name, 'w')
	f.write(plugboard)
	f.close()

def loadPB():
	name = input('What is the file name? ')
	f = open('plugboardSettings/' + name, 'r')
	return f.read()
	f.close()

def loadRotors(a, b, c):
	for i in range(3):
		f = open('rotors/' + str(i+1), 'r')
		rawRotor = f.read()
		f.close()

		rotor = rawRotor.split()
		rotors.append(rotor)
		print('Rotor ' + str(i+1) + ' Loaded')

while True:
	x = input('Type:\n1 - Set Plugboard\n2 - Save Plugboard\n3 - Load a Plugboard\n4 - View Current Plugboard\n5 - Load Rotors\n10 - Quit\n')
	os.system('clear')
	if x == '1':
		plugboard = setPB()
	elif x == '2':
		savePB()
	elif x == '3':
		plugboard = loadPB()
	elif x == '4':
		print(alphabet + "\n" + plugboard)
	elif x == '5':
		x = input('Which Rotors? (a,b,c): ').split(',')
		loadRotors(x[0], x[1], x[2])
	elif x == '10':
		break
	else:
		print('Try Again')