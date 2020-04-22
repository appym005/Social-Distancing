import pygame
from network import Network
from player import Player



def main():
	n = Network()
	p1 = n.getP()
	run = True
	clock = pygame.time.Clock()

	while run:

		clock.tick(60)
		p2 = n.send(p1)

		
		

		

		p1.move()
		

main()
