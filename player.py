import pygame

class Player():
	def __init__(self, x):
		self.x = x
		self.a = [i for i in range(0,100)]
		self.c = 0
		


	def move(self):
		f = open("data","r")
		self.x = f.read()
		f.close()
		


	