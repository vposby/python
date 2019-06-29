"""
Desktop/Software/Python/Pygame
Draw six circles of different colors at
different positions, then change their
positions randomly.
"""

import sys, pygame, random
pygame.init()

size = width, height = (512, 512)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
pink = (255,0,255)
cyan = (0,255,255)

pos=[]
pos.append([int(width/4),int(height/3),(int(width/4),int(height/3))]) #top left
pos.append([int(width/2),int(height/3),(int(width/2),int(height/3))])  #top middle
pos.append([int(3*width/4),int(height/3),(int(3*width/4),int(height/3))])  #top right
pos.append([int(width/4),int(2*height/3),(int(width/4),int(2*height/3))])  #bottom left
pos.append([int(width/2),int(2*height/3),(int(width/2),int(2*height/3))])  #bottom middle
pos.append([int(3*width/4),int(2*height/3),(int(3*width/4),int(2*height/3))])  #bottom right
cirSize = 25

screen = pygame.display.set_mode(size)
screen.fill(black)

redCir = pygame.draw.circle(screen,red,pos[0][2],cirSize)
greenCir = pygame.draw.circle(screen,green,pos[1][2],cirSize)
blueCir = pygame.draw.circle(screen,blue,pos[2][2],cirSize)
yellowCir = pygame.draw.circle(screen,yellow,pos[3][2],cirSize)
pinkCir = pygame.draw.circle(screen,pink,pos[4][2],cirSize)
cyanCir = pygame.draw.circle(screen,cyan,pos[5][2],cirSize)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)
	for cir in range(0,len(pos)):
		pos[cir][0]=x=pos[cir][0]+random.randrange(-2,3)
		pos[cir][1]=y=pos[cir][1]+random.randrange(-2,3)
		pos[cir][2]=(x,y)

	redCir = pygame.draw.circle(screen,red,pos[0][2],cirSize)
	greenCir = pygame.draw.circle(screen,green,pos[1][2],cirSize)
	blueCir = pygame.draw.circle(screen,blue,pos[2][2],cirSize)
	yellowCir = pygame.draw.circle(screen,yellow,pos[3][2],cirSize)
	pinkCir = pygame.draw.circle(screen,pink,pos[4][2],cirSize)
	cyanCir = pygame.draw.circle(screen,cyan,pos[5][2],cirSize)
	
	pygame.time.wait(25)
	pygame.display.update()