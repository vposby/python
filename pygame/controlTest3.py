"""
Draw eight red circles at different
positions, then change their positions
in a linear fashion. If they hit the
outer edge, reverse their direction.

Draw a green circle that moves with
the user's keyboard input (wasd).

When user presses arrow keys, create
ray that originates from user's position
and moves until it hits the edge of the
screen. A maximum of five shots is allowed
on the screen.

There must be a delay between the shots
even if the key is pressed down.
"""

import sys, pygame
pygame.init()

size = width, height = (512, 512)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,224,0)

pos=[] #x coordinate, y coordinate, coordinate pair
pos.append([int(width/2),int(height/4),(int(width/2),int(height/4))]) #N
pos.append([int(2*width/3),int(height/3),(int(2*width/3),int(height/3))]) #NE
pos.append([int(3*width/4),int(height/2),(int(3*width/4),int(height/2))]) #E
pos.append([int(2*width/3),int(2*height/3),(int(2*width/3),int(2*height/3))]) #SE
pos.append([int(width/2),int(3*height/4),(int(width/2),int(3*height/4))]) #S
pos.append([int(width/3),int(2*height/3),(int(width/3),int(2*height/3))]) #SW
pos.append([int(width/4),int(height/2),(int(width/4),int(height/2))]) #W
pos.append([int(width/3),int(height/3),(int(width/3),int(height/3))]) #NW
pos.append([int(width/2),int(height/2),(int(width/2),int(height/2))]) #player
cirSize = 20

screen = pygame.display.set_mode(size)
screen.fill(black)
#pygame.mouse.set_visible(False)
screenFont = pygame.font.Font(None, 48) #in case I need to display values

for x in range(len(pos)-1):
	pygame.draw.circle(screen,red,pos[x][2],cirSize)
pygame.draw.circle(screen,green,pos[8][2],cirSize)
outN = outNE = outE = outSE = outS = outSW = outW = outNW = True

shotCount = 0
shot=[]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_ESCAPE]: sys.exit()

	screen.fill(black)

	#move circles
	for cir in range(0,len(pos)):
		if cir==0: #N
			x=pos[cir][0]
			if outN==True:
				if pos[cir][1]-1>25:
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outN=False
					pos[cir][1]=y=pos[cir][1]+1
			else:
				if pos[cir][1]+1<487:
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outN=True
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
			y=pos[cir][1]
			if outE==True:
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
				else:
					outE=False
					pos[cir][0]=x=pos[cir][0]-1
			else:
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
				else:
					outE=True
					pos[cir][0]=x=pos[cir][0]+1
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
			x=pos[cir][0]
			if outS==True:
				if pos[cir][1]+1<487:
					pos[cir][1]=y=pos[cir][1]+1
				else:
					outS=False
					pos[cir][1]=y=pos[cir][1]-1
			else:
				if pos[cir][1]-1>25:
					pos[cir][1]=y=pos[cir][1]-1
				else:
					outS=True
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
			y=pos[cir][1]
			if outW==True:
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-1
				else:
					outW=False
					pos[cir][0]=x=pos[cir][0]+1
			else:
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+1
				else:
					outW=True
					pos[cir][0]=x=pos[cir][0]-1
		elif cir==7: #NW
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
		#move user
		else:
			if pressed[pygame.K_w] and pressed[pygame.K_d]: #NE
				if pos[cir][0]+1<487 and pos[cir][1]-1>25:
					pos[cir][0]=x=pos[cir][0]+3
					pos[cir][1]=y=pos[cir][1]-3
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_w] and pressed[pygame.K_a]: #NW
				if pos[cir][0]-1>25 and pos[cir][1]-1>25:
					pos[cir][0]=x=pos[cir][0]-3
					pos[cir][1]=y=pos[cir][1]-3
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_s] and pressed[pygame.K_d]: #SE
				if pos[cir][0]+1<487 and pos[cir][1]+1<487:
					pos[cir][0]=x=pos[cir][0]+3
					pos[cir][1]=y=pos[cir][1]+3
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_s] and pressed[pygame.K_a]: #SW
				if pos[cir][0]-1>25 and pos[cir][1]+1<487:
					pos[cir][0]=x=pos[cir][0]-3
					pos[cir][1]=y=pos[cir][1]+3
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_w]: #N
				if pos[cir][1]-1>25:
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]-3
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_a]: #W
				if pos[cir][0]-1>25:
					pos[cir][0]=x=pos[cir][0]-3
					y=pos[cir][1]
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_s]: #S
				if pos[cir][1]+1<487:
					x=pos[cir][0]
					pos[cir][1]=y=pos[cir][1]+3
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			elif pressed[pygame.K_d]: #E
				if pos[cir][0]+1<487:
					pos[cir][0]=x=pos[cir][0]+3
					y=pos[cir][1]
				else:
					x=pos[cir][0]
					y=pos[cir][1]
			else:
				x=pos[cir][0]
				y=pos[cir][1]
		pos[cir][2]=(x,y)

	#fire shots
	if shotCount<5:
		#create short line segment in direction specified by user
		shotStart=[x,y,(x,y)]
		shotFin=[x,y,(x,y)]
		if pressed[pygame.K_UP]: #N
			pygame.key.set_repeat(750,500)
			shotStart[1]-=20
			shotStart[2]=(shotStart[0],shotStart[1])
			shotFin[1]-=30
			shotFin[2]=(shotFin[0],shotFin[1])
			shotCount+=1
			shot.append(["N",shotStart,shotFin])
		elif pressed[pygame.K_RIGHT]: #E
			pygame.key.set_repeat(750,500)
			shotStart[0]+=20
			shotStart[2]=(shotStart[0],shotStart[1])
			shotFin[0]+=30
			shotFin[2]=(shotFin[0],shotFin[1])
			shotCount+=1
			shot.append(["E",shotStart,shotFin])
		elif pressed[pygame.K_DOWN]: #S
			pygame.key.set_repeat(750,500)
			shotStart[1]+=20
			shotStart[2]=(shotStart[0],shotStart[1])
			shotFin[1]+=30
			shotFin[2]=(shotFin[0],shotFin[1])
			shotCount+=1
			shot.append(["S",shotStart,shotFin])
		elif pressed[pygame.K_LEFT]: #W
			pygame.key.set_repeat(750,500)
			shotStart[0]-=20
			shotStart[2]=(shotStart[0],shotStart[1])
			shotFin[0]-=30
			shotFin[2]=(shotFin[0],shotFin[1])
			shotCount+=1
			shot.append(["W",shotStart,shotFin])
	#move line segment in previously-specified direction
	shotNum=0
	pygame.key.set_repeat()
	while shotNum<shotCount:
		if shot[shotNum][0]=="N":
			shot[shotNum][1][1]-=3
			shot[shotNum][1][2]=(shot[shotNum][1][0],shot[shotNum][1][1])
			shot[shotNum][2][1]-=3
			shot[shotNum][2][2]=(shot[shotNum][2][0],shot[shotNum][2][1])
			shotNum+=1
			#check for collision
			if shot[shotNum-1][1][1]<0:
				shotCount-=1
				shot.pop(shotNum-1)
				shotNum-=1
		elif shot[shotNum][0]=="E":
			shot[shotNum][1][0]+=3
			shot[shotNum][1][2]=(shot[shotNum][1][0],shot[shotNum][1][1])
			shot[shotNum][2][0]+=3
			shot[shotNum][2][2]=(shot[shotNum][2][0],shot[shotNum][2][1])
			shotNum+=1
			if shot[shotNum-1][1][0]>512:
				shotCount-=1
				shot.pop(shotNum-1)
				shotNum-=1
		elif shot[shotNum][0]=="S":
			shot[shotNum][1][1]+=3
			shot[shotNum][1][2]=(shot[shotNum][1][0],shot[shotNum][1][1])
			shot[shotNum][2][1]+=3
			shot[shotNum][2][2]=(shot[shotNum][2][0],shot[shotNum][2][1])
			shotNum+=1
			if shot[shotNum-1][1][1]>512:
				shotCount-=1
				shot.pop(shotNum-1)
				shotNum-=1
		elif shot[shotNum][0]=="W":
			shot[shotNum][1][0]-=3
			shot[shotNum][1][2]=(shot[shotNum][1][0],shot[shotNum][1][1])
			shot[shotNum][2][0]-=3
			shot[shotNum][2][2]=(shot[shotNum][2][0],shot[shotNum][2][1])
			shotNum+=1
			if shot[shotNum-1][1][0]<0:
				shotCount-=1
				shot.pop(shotNum-1)
				shotNum-=1

	for x in range(len(pos)-1):
		pygame.draw.circle(screen,red,pos[x][2],cirSize)
	pygame.draw.circle(screen,green,pos[8][2],cirSize)
	screen.blit(screenFont.render(str(shotCount),1,white),(256,0))

	for x in range(0,shotCount):
		pygame.draw.line(screen,yellow,shot[x][1][2],shot[x][2][2],4)


	pygame.display.update()
