#import library & init game engine
import pygame
pygame.init()

# Colours
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
#

# Open Game Window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
#

'''Main Program'''

carryOn = True #decides whether main loop continues
clock = pygame.time.Clock() #used to control fps

# Main Loop
while carryOn:
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			carryOn = False #flag the exiting of the program

	''' Game Logic '''

	# Draw #
	screen.fill(white) # Clear Screen first

	

	pygame.display.flip() # Update the Screen

	# Limit FPS #
	clock.tick(60)
#

#Exit Program & Engine
pygame.quit()