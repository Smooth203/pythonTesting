import pygame

from dud import Dud

pygame.init()

# Colours
black = (0,0,0)
white = (255, 255, 255)
#

# declarations
grid = []
#

# Open Game Window
size = (767, 423)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Nav Test')
#

'''Main Program'''

carryOn = True #decides whether main loop continues
clock = pygame.time.Clock() #used to control fps

# init sprites and shit
spriteList = pygame.sprite.Group()

dud = Dud(black, 22, 22)
dud.rect.x = 44
dud.rect.y = 44

fp = pygame.image.load('fp.png').convert_alpha()

spriteList.add(dud)

def initGrid(width, height):
	for i in range(width):
		new = []
		for j in range(height):
			new.append(0)
		grid.append(new)

def drawGrid(size):
	len1 = len(grid)
	for i in range(len1):
		len2 = len(grid[i])
		for j in range(len2):
			pygame.draw.rect(screen, black, (i*size, j*size, size, size), 1)

initGrid(70, 39)

# Main Loop
while carryOn:
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			carryOn = False #flag the exiting of the program
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #pressing x will quit
				carryOn = False

	''' Logic '''

	# Draw #
	screen.fill(white) # Clear Screen first

	drawGrid(11)
	spriteList.draw(screen)
	screen.blit(fp, (0,0))

	pygame.display.flip() # Update the Screen

	# Limit FPS #
	clock.tick(60)
#

#Exit Program & Engine
pygame.quit()