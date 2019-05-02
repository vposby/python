"""
Desktop/Software/Python/Pygame
Draw eight circles of different colors at
different positions, then change their
positions in a linear fashion. If they
hit the outer edge, reverse their direction.
"""

import sys, pygame
pygame.init()

size = width, height = (512, 512)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,128,0)
yellow = (255,255,0)
green = (0,192,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (128,0,128)
pink = (255,0,255)

pos=[]
pos.append([int(width/2),int(height/4),(int(width/2),int(height/4))]) #N
pos.append([int(2*width/3),int(height/3),(int(2*width/3),int(height/3))])  #NE
pos.append([int(3*width/4),int(height/2),(int(3*width/4),int(height/2))])  #E
pos.append([int(2*width/3),int(2*height/3),(int(2*width/3),int(2*height/3))])  #SE
pos.append([int(width/2),int(3*height/4),(int(width/2),int(3*height/4))])  #S
pos.append([int(width/3),int(2*height/3),(int(width/3),int(2*height/3))])  #SW
pos.append([int(width/4),int(height/2),(int(width/4),int(height/2))])  #W
pos.append([int(width/3),int(height/3),(int(width/3),int(height/3))])  #NW
cirSize = 25

screen = pygame.display.set_mode(size)
screen.fill(black)

redCir = pygame.draw.circle(screen,red,pos[0][2],cirSize)
orangeCir = pygame.draw.circle(screen,orange,pos[1][2],cirSize)
yellowCir = pygame.draw.circle(screen,yellow,pos[2][2],cirSize)
greenCir = pygame.draw.circle(screen,green,pos[3][2],cirSize)
cyanCir = pygame.draw.circle(screen,cyan,pos[4][2],cirSize)
blueCir = pygame.draw.circle(screen,blue,pos[5][2],cirSize)
purpleCir = pygame.draw.circle(screen,purple,pos[6][2],cirSize)
pinkCir = pygame.draw.circle(screen,pink,pos[7][2],cirSize)
outN = outNE = outE = outSE = outS = outSW = outW = outNW = True

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	screen.fill(black)
	for cir in range(0,len(pos)):
		if cir==0: #N
			if outN==True:
				if pos[cir][1]-1>25:
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outN=False
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]+1
			else:
				if pos[cir][1]+1<487:
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outN=True
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]-1
		elif cir==1: #NE
			if outNE==True:
				if pos[cir][1]-1>25:
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outNE=False
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]+1
			else:
				if pos[cir][1]+1<487:
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outNE=True
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]-1			
		elif cir==2: #E
			if outE==True:
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
					y=pos[cir][1]
				else:
					outE=False
					pos[cir][0]=x=pos[cir][0]-1
					y=pos[cir][1]
			else:
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
					y=pos[cir][1]
				else:
					outE=True
					pos[cir][0]=x=pos[cir][0]+1
					y=pos[cir][1]
		elif cir==3: #SE
			if outSE==True:
				if pos[cir][1]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outSE=False
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]-1
			else:
				if pos[cir][1]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outSE=True
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]+1
		elif cir==4: #S
			if outS==True:
				if pos[cir][1]+1<487:
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outS=False
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]-1
			else:
				if pos[cir][1]-1>25:
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outS=True
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]+1
		elif cir==5: #SW
			if outSW==True:
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outSW=False
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]-1
			else:
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outSW=True
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]+1
		elif cir==6: #W
			if outW==True:
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
					y=pos[cir][1]
				else:
					outW=False
					pos[cir][0]=x=pos[cir][0]+1
					y=pos[cir][1]
			else:
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
					y=pos[cir][1]
				else:
					outW=True
					pos[cir][0]=x=pos[cir][0]-1
					y=pos[cir][1]
		else: #NW
			if outNW==True:
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outNW=False
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]+1
			else:
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outNW=True
					pos[cir][0]=x=pos[cir][0]-1
					pos[cir][1]=y=pos[cir][1]-1
		pos[cir][2]=(x,y)

	redCir = pygame.draw.circle(screen,red,pos[0][2],cirSize)
	orangeCir = pygame.draw.circle(screen,orange,pos[1][2],cirSize)
	yellowCir = pygame.draw.circle(screen,yellow,pos[2][2],cirSize)
	greenCir = pygame.draw.circle(screen,green,pos[3][2],cirSize)
	cyanCir = pygame.draw.circle(screen,cyan,pos[4][2],cirSize)
	blueCir = pygame.draw.circle(screen,blue,pos[5][2],cirSize)
	purpleCir = pygame.draw.circle(screen,purple,pos[6][2],cirSize)
	pinkCir = pygame.draw.circle(screen,pink,pos[7][2],cirSize)
	
	pygame.time.wait(50)
	pygame.display.update()