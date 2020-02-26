import pygame
white = (255, 255, 255)

class Player(pygame.sprite.Sprite):
	def __init__(self, colour, w, h):
		super().__init__()

		self.speed = 2
		self.facing = 0 # 0,1,2,3 = up,right,down,left | respectively

		self.anim = 0
		self.animSpeed = 0.1
		self.moving = False
		self.idle = []
		self.walk1 = []
		self.walk2 = []
		self.imgs = []

		self.image = pygame.Surface([w,h]) #set dimensions
		self.image.fill(white) #set blank colour (is changed)
		self.image.set_colorkey(white)

		for i in range(1,5): #loop through 1, 2, 3, 4 not 5
			#img dimension 79,100
			newIdle = pygame.image.load('assets/player/playerIdle' + str(i) + '.png')
			newW1 = pygame.image.load('assets/player/playerWalka' + str(i) + '.png')
			newW2 = pygame.image.load('assets/player/playerWalkb' + str(i) + '.png')
			self.idle.append(newIdle)
			self.walk1.append(newW1)
			self.walk2.append(newW2)
			self.imgs.append(self.idle)
			self.imgs.append(self.walk1)
			self.imgs.append(self.walk2)

		self.image = self.imgs[0][self.facing]

		self.rect = self.image.get_rect() # fetch a rect to represent player w/ player dimension

	def walkAnim(self):
		if self.moving:
			self.anim += 1 * self.animSpeed
			if self.anim > 1 and self.anim < 2:
				self.image = self.imgs[1][self.facing]
			elif self.anim > 3 and self.anim < 4:
				self.image = self.imgs[2][self.facing]
			else:
				self.image = self.imgs[0][self.facing]

			if self.anim > 4:
				self.anim = 0