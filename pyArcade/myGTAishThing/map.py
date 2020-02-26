import pygame
white = (255, 255, 255)

class Map(pygame.sprite.Sprite):
	def __init__(self, w, h):
		super().__init__()

		self.image = pygame.Surface([w,h]) #set dimensions
		self.image.fill(white) #set blank colour (is changed)
		self.image.set_colorkey(white)

		# pygame.draw.rect(self.image, colour, [0, 0, w, h]) #draw 
		self.image = pygame.image.load('assets/map.png').convert_alpha()

		self.rect = self.image.get_rect() # fetch a rect to represent object w/ object dimension

	def moveR(self, amount):
		self.rect.x -= amount

	def moveL(self, amount):
		self.rect.x += amount

	def moveU(self, amount):
		self.rect.y += amount

	def moveD(self, amount):
		self.rect.y -= amount