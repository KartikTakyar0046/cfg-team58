import pygame
#inititate the pygame
pygame.init()
#creating the pygame window screen
screen=pygame.display.set_mode((800,600))
#setting the title of the window
pygame.display.set_caption('The GAME')
#setting the logo
icon=pygame.image.load('spaceship.png')
pygame.display.set_logo(icon)
#game loop
running=True
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False