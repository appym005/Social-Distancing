import pygame

class Object():
	def __init__(self, x):
		self.x = x
		

	

	def inp(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.x = 1

		if keys[pygame.K_RIGHT]:
			self.x = 2


		