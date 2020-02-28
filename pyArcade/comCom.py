## Classes
import pygame
white = (255, 255, 255)

class CLASS(pygame.sprite.Sprite):
	def __init__(self, colour, w, h):
		super().__init__()

		self.image = pygame.Surface([w,h]) #set dimensions
		self.image.fill(white) #set blank colour (is changed)
		self.image.set_colorkey(white)

		#Draw
		pygame.draw.rect(self.image, colour, [0, 0, w, h])

		self.rect = self.image.get_rect() # fetch a rect to represent player w/ player dimension