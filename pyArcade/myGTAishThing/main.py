#import library & init game engine
import pygame
import os
from player import Player
from map import Map
pygame.init()

# Colours
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
#

# Open Game Window
screenW = 800
screenH = 600
size = (screenW, screenH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
#

# Manage Sprites
spriteList = pygame.sprite.Group()

world = Map(1000, 1000)
world.rect.x = 0
world.rect.y = 0

player = Player(green, 79, 100)
player.rect.x = screenW/2 - player.rect.w/2
player.rect.y = screenH/2 - player.rect.h/2

spriteList.add(world, player)
#

'''Main Program'''

carryOn = True #decides whether main loop continues
clock = pygame.time.Clock() #used to control fps

# Functions
def debug():
	print(player.anim)

# Main Loop
while carryOn:
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			carryOn = False #flag the exiting of the program
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #pressing x will quit
				carryOn = False
			elif event.key == pygame.K_F3:
				debug()
		elif event.type == pygame.KEYUP:
			player.moving = False
			player.anim = 0

	''' Game Logic '''
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:				##
		world.moveU(player.speed)		##	Char Controls
		player.moving = True			##
		player.facing = 0
	elif keys[pygame.K_s]:
		world.moveD(player.speed)
		player.moving = True
		player.facing = 2
	if keys[pygame.K_a]:
		world.moveL(player.speed)
		player.moving = True
		player.facing = 3
	elif keys[pygame.K_d]:
		world.moveR(player.speed)		##
		player.moving = True			##
		player.facing = 1				##

	#player animation
	player.walkAnim()

	# Draw #
	screen.fill(white) # Clear Screen first

	spriteList.draw(screen)

	pygame.display.flip() # Update the Screen

	# Limit FPS #
	clock.tick(60)
#

#Exit Program & Engine
pygame.quit()