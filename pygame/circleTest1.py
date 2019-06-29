"""
Desktop/Software/Python/Pygame
Draw six circles of different colors at
different positions, then change their
sizes randomly.
"""

import sys, pygame, random
pygame.init()

#display size
size = width, height = (512, 512) 

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
pink = (255,0,255)
cyan = (0,255,255)

#circle positions
topRt = (int(width/4),int(height/3))
topMid = (int(width/2),int(height/3))
topLt = (int(3*width/4),int(height/3))
btmRt = (int(width/4),int(2*height/3))
btmMid = (int(width/2),int(2*height/3))
btmLt = (int(3*width/4),int(2*height/3))

#initial circle size
cirSize = redSize = greenSize = blueSize = yellowSize = pinkSize = cyanSize = 10 

screen = pygame.display.set_mode(size)
screen.fill(black)

#first circles
redCir = pygame.draw.circle(screen,red,topRt,cirSize)
greenCir = pygame.draw.circle(screen,green,topMid,cirSize)
blueCir = pygame.draw.circle(screen,blue,topLt,cirSize)
yellowCir = pygame.draw.circle(screen,yellow,btmRt,cirSize)
pinkCir = pygame.draw.circle(screen,pink,btmMid,cirSize)
cyanCir = pygame.draw.circle(screen,cyan,btmLt,cirSize)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	screen.fill(black)
	
	#change circle sizes
	redCir = pygame.draw.circle(screen,red,topRt,redSize)
	redSize+=random.randrange(int((-1*redSize)+10),int(2*redSize/3))

	greenCir = pygame.draw.circle(screen,green,topMid,greenSize)
	greenSize+=random.randrange(int((-1*greenSize)+10),int(2*greenSize/3))

	blueCir = pygame.draw.circle(screen,blue,topLt,blueSize)
	blueSize+=random.randrange(int((-1*blueSize)+10),int(2*blueSize/3))

	yellowCir = pygame.draw.circle(screen,yellow,btmRt,yellowSize)
	yellowSize+=random.randrange(int((-1*yellowSize)+10),int(2*yellowSize/3))

	pinkCir = pygame.draw.circle(screen,pink,btmMid,pinkSize)
	pinkSize+=random.randrange(int((-1*pinkSize)+10),int(2*pinkSize/3))

	cyanCir = pygame.draw.circle(screen,cyan,btmLt,cyanSize)
	cyanSize+=random.randrange(int((-1*cyanSize)+10),int(2*cyanSize/3))
	
	pygame.time.wait(300)
	pygame.display.update()