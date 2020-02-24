from datetime import datetime, timedelta 
import time
import keyboard
import math
from os import system

class quit(Exception): pass

name = 'James'
mood = 'Fine'
action = 'Idle'
hunger = 100
energy = 100
needLoss = 0.5
needLossMultiplier = 1
dt = 0
debug = False

def checkKeyPress():
	if keyboard.is_pressed('esc'):
		raise quit
	elif keyboard.is_pressed('q'):
		global debug
		debug = not debug
		time.sleep(0.01)

def needsDecay():
	global hunger
	global energy

	hunger -= needLoss * needLossMultiplier * dt
	energy -= needLoss * needLossMultiplier * dt

def printGame():
	br = "\n-------------------\n"
	info = "Name: "+name+"\nMood: "+mood+"\nCurrent Action: "+action
	needs = "Needs:\nHunger: "+str(math.floor(hunger))+"\nenergy: "+str(math.floor(energy))
	print(info+br+needs)

def printDebug():
	print("DEBUG MODE:\n\ndt: "+str(dt))


def update():
	needsDecay()
	checkKeyPress()

try:
	while True:
		t1 = time.time()
		system("cls")
		###
		update()
		if debug == True:
			printDebug()
		else:
			printGame()
		###
		dt = time.time() - t1
		time.sleep(0.01)
except quit:
	print('Goodbye')