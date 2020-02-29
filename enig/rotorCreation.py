import random as r
import os
import math
from string import ascii_lowercase
alphabet = ascii_lowercase

rotor = []

ID = str(len(os.listdir('rotors/')) + 1)
for i in range(2):
	newIO = ''
	for letter in alphabet:
		hold = True
		while hold:
			rl = r.choice(alphabet)
			if rl not in newIO:
				newIO = newIO + rl
				hold = False
	rotor.append(newIO)

Rotor = rotor[0] + ' ' + rotor[1]

f = open('rotors/' + ID, 'w')
f.write(Rotor)
f.close()

'''
f = open('rotors/' + ID, 'r')
rawRotor = f.read()
f.close()

R = rawRotor.split()
print(R[0])
'''