import pygame
import random

from villager import villager

pygame.init()

# Colours
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
#

# Declaration

#

# Open Game Window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
#

'''Main Program'''

carryOn = True #decides whether main loop continues
clock = pygame.time.Clock() #used to control fps

# Sprites
spriteList = pygame.sprite.Group()
#

# Functions
def generateVillagers(amount):
	for i in range(amount):
		x = random.randrange(300, 500)
		y = random.randrange(200,400)
		spriteList.add(villager(black, x, y, 5, 5))

def moveVillager():
	villagers = spriteList.sprites()
	for i in villagers:
		i.move()

def getVillagerPos():
	villagers = spriteList.sprites()
	for i in villagers:
		return i.getPos()

def checkVillagers(checkFor):
	villagers = spriteList.sprites()
	for i in villagers:
		x = i.rect.x
		y = i.rect.y
		if getMouse('x') >= x and getMouse('x') <= x + 5 and getMouse('y') >= y and getMouse('y') <= y + 5:
			print('found')

def getMouse(pos):
	x, y = pygame.mouse.get_pos()
	if pos == 'x':
		return x
	else:
		return y
#

# Load
generateVillagers(10)
#

# Main Loop
while carryOn:
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			carryOn = False #flag the exiting of the program
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #pressing x will quit
				carryOn = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			checkVillagers('pos')
			#if getMouse() == getVillagerPos():
			#	print(1)

	''' Game Logic '''

	# Draw #
	screen.fill(white) # Clear Screen first

	spriteList.draw(screen)

	pygame.display.flip() # Update the Screen

	# Limit FPS #
	clock.tick(60)
#

#Exit Program & Engine
pygame.quit()