import pygame
white = (255, 255, 255)

class Dud(pygame.sprite.Sprite):
	def __init__(self, colour, w, h):
		super().__init__()

		self.image = pygame.Surface([w,h]) #set dimensions
		self.image.fill(white) #set blank colour (is changed)
		self.image.set_colorkey(white)

		#draw
		pygame.draw.rect(self.image, colour, [0, 0, w, h])

		# fetch a rect to represent player w/ player dimension
		self.rect = self.image.get_rect()