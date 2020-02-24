import pygame
white = (255, 255, 255)

class Car(pygame.sprite.Sprite):
	#represents a car
	def __init__(self, color, width, height):
		#call the parent class
		super().__init__()

		#pass in the colour and pos, w & h of car
		self.image = pygame.Surface([width, height])
		self.image.fill(white)
		self.image.set_colorkey(white)

		#draw car
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		#or load and actual img
		# self.image = pygame.image.load('car.png').convert_alpha()

		#fetch rectangle with dimensiton of image
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels