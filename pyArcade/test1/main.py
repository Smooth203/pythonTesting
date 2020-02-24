#import library & init game engine
import pygame
#import classes
from car import Car
#
pygame.init()

#define colours
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#open the game window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')

#sprite creation
all_sprites_list = pygame.sprite.Group()

playerCar = Car(red, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

all_sprites_list.add(playerCar)
#

'''main program loop'''

#loop will ocntinue untill user exits the game
carryOn = True

#clock controls screen updates
clock = pygame.time.Clock()

#Main Loop
while carryOn:
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			carryOn = False #flag the exiting of the program
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #pressing x will quit
				carryOn = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		playerCar.moveLeft(5)
	if keys[pygame.K_d]:
		playerCar.moveRight(5)

	'''game logic'''

	#game drawing	
	#clear screen
	screen.fill(white)
	#now draw shit
	all_sprites_list.draw(screen)

	#update the screen with new drawings
	pygame.display.flip()

	#limit to 60fps
	clock.tick(60)

#if main loop if exited, stop game engine and therefore program
pygame.quit()