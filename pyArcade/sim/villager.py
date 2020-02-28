import pygame
white = (255, 255, 255)

class villager(pygame.sprite.Sprite):
	def __init__(self, colour, x, y, w, h):
		super().__init__()

		self.image = pygame.Surface([w,h]) #set dimensions
		self.image.fill(white) #set blank colour (is changed)
		self.image.set_colorkey(white)

		#Draw
		pygame.draw.rect(self.image, colour, [0, 0, w, h])

		self.rect = self.image.get_rect() # fetch a rect to represent player w/ player dimension

		self.rect.x = x
		self.rect.y = y

	def move(self):
		self.rect.x += 1

	def getPos(self):
		pos = "(" + str(self.rect.x) + "," + str(self.rect.y) + ")"
		return pos

	def check(self, checkFor):
		if checkFor == 'pos':
			self.x = self.rect.x
			self.y = self.rect.y