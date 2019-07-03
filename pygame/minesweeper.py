"""
Desktop/Software/Python/Pygame
Minesweeper!
Current Issues:
*custMenu doesn't drop when Cancel button is pressed
*clicking new game needs a delay between clicks
 (goes straight to small or medium game depending on
  mouse position)
"""

import sys, pygame, random, pdb
pygame.init()

size=width,height=(384,512)

black=(0,0,0)
white=(255,255,255)
grey=(196,196,196)
red=(224,0,0)
orange=(255,128,0)
yellow=(224,224,0)
green=(0,224,0)
cyan=(0,255,255)
blue=(0,0,224)
purple=(128,0,128)
pink=(224,0,224)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")
titleFont=pygame.font.Font(None,60)
menuFont=pygame.font.Font(None,46)
listFont=pygame.font.Font(None,30)
textFont=pygame.font.Font(None,18)
numFont=pygame.font.Font(None,22)
custWd=10
custHt=10
boxx=27*width/100
boxwidth=width/8
boxheight=height/25
custMenu=False
gameOver=False
firstGuess=True

#draw menu screen icon
def drawHouse(x,y,width,height):
	#roof
	pygame.draw.line(screen,white,(x+(width/25),y+(9*height/20)),(x+(width/2),y+(height/25)),2)
	pygame.draw.line(screen,white,(x+(width/2),y+(height/25)),(x+(24*width/25),y+(9*height/20)),2)
	#walls/floor
	pygame.draw.rect(screen,white,(x+(width/6),y+(17*height/50),2*width/3,7*height/12),2)
	#door
	pygame.draw.rect(screen,white,(x+(3*width/8),y+(87*height/200),width/4,49*height/100),2)
	return;

#switch between menu, size selection, game, directions, and high score list screens
def screenChange(screenNum):
	screen.fill(black)
	#menu screen
	if screenNum==1:
		#game title
		screen.blit(titleFont.render("Minesweeper",1,white),(width/6,3*height/20))
		#new game button
		pygame.draw.rect(screen,green,(width/4,20*height/40,width/2,5*height/40))
		screen.blit(menuFont.render("New Game",1,white),((width/4)+15,(10*height/20)+18))
		#directions button
		pygame.draw.rect(screen,blue,(width/4,26*height/40,width/2,5*height/40))
		screen.blit(menuFont.render("How to Play",1,white),((width/4)+6,(13*height/20)+18))
		#high scores button
		pygame.draw.rect(screen,purple,(width/4,32*height/40,width/2,5*height/40))
		screen.blit(menuFont.render("High Scores",1,white),((width/4)+6,(16*height/20)+18))
	#size selection screen
	elif screenNum==2:
		#back to home
		pygame.draw.rect(screen,blue,(4*width/5,height/20,width/10,width/10))
		drawHouse(4*width/5,height/20,width/10,width/10)
		#screen title
		screen.blit(titleFont.render("Size Selection",1,white),(width/8.5,3*height/20))
		#small
		pygame.draw.rect(screen,red,(width/15,6*height/20,5*width/12,5*width/12))
		screen.blit(menuFont.render("  Small",1,white),((width/15)+6,(6*height/20)+48))
		#medium
		pygame.draw.rect(screen,pink,(8*width/15,6*height/20,5*width/12,5*width/12))
		screen.blit(menuFont.render("  Medium",1,white),((8*width/15)+6,(6*height/20)+48))
		#large
		pygame.draw.rect(screen,orange,(width/15,13*height/20,5*width/12,5*width/12))
		screen.blit(menuFont.render("  Large",1,white),((width/15)+6,(13*height/20)+48))
		#custom
		pygame.draw.rect(screen,yellow,(8*width/15,13*height/20,5*width/12,5*width/12))
		screen.blit(menuFont.render("  Custom",1,white),((8*width/15)+6,(13*height/20)+48))

		if custMenu==True:
			pygame.draw.rect(screen,grey,(width/4,height/3,width/2,height/3))
			screen.blit(textFont.render("Choose your grid size below by",1,black),(boxx,(height/3)+(height/100)))
			screen.blit(textFont.render("scrolling the mouse wheel.",1,black),(boxx,(height/3)+(3*height/100)))
			screen.blit(textFont.render("Grid Width:",1,black),(boxx,21*height/50))
			screen.blit(textFont.render("Grid Height:",1,black),(boxx,25*height/50))
			pygame.draw.rect(screen,white,(boxx,45*height/100,width/8,height/25))
			pygame.draw.rect(screen,white,(boxx,53*height/100,width/8,height/25))
			screen.blit(numFont.render(str(custWd),1,black),(boxx,23*height/50))
			screen.blit(numFont.render(str(custHt),1,black),(boxx,27*height/50))
			pygame.draw.rect(screen,black,(11*width/32,59*height/100,width/8,height/25),2)
			screen.blit(textFont.render("Start",1,black),((11*width/32)+(3*width/100),(59*height/100)+(height/100)))
			pygame.draw.rect(screen,black,(17*width/32,59*height/100,width/8,height/25),2)
			screen.blit(textFont.render("Cancel",1,black),((17*width/32)+(3*width/200),(59*height/100)+(height/100)))
	#directions screen
	elif screenNum==3:
		#back to home
		pygame.draw.rect(screen,blue,(4*width/5,height/20,width/10,width/10))
		drawHouse(4*width/5,height/20,width/10,width/10)
		screen.blit(titleFont.render("How to Play",1,white),(width/8.5,2*height/20))
	#high score screen
	elif screenNum==4:
		#back to home
		pygame.draw.rect(screen,blue,(4*width/5,height/20,width/10,width/10))
		drawHouse(4*width/5,height/20,width/10,width/10)
		screen.blit(titleFont.render("High Scores",1,white),(width/8.5,2*height/20))
	pygame.display.update()

#generate the next field
def fieldGen(gameMode):
	pdb.set_trace()
	fieldSize=gameMode[0]*gameMode[1]
	mineNum=random.randrange(int(.1*fieldSize),int(.25*fieldSize)+1) #10-25% of cells are mines
	mineCount=0
	screen.fill(black)
	for x in range(0,gameMode[0]):
		for y in range(0,gameMode[1]):
			if random.randrange(0,2)==0:
				boom=False
			elif mineCount==mineNum:
				boom=False
			else:
				boom=True
				mineCount+=1
			#grid x, grid y, has mine?, user clicked?
			cell.append([x,y,boom,False])
			pygame.draw.rect(screen,grey,((x+1)*(width/gameMode[0]),(y+1)*(height/gameMode[1]),
			width/gameMode[0],width/gameMode[0]))
			pygame.display.update()

#check if cell has mine
def cellCheck(cellPos):
	if firstGuess==False:
		#reveal number of mines surrounding square, clear any swathes of vacant space
		screen.blit(titleFont.render("Game Screen",1,white),(width/2,height/2))
	else:
		#if mine exists at location, remove and place at topmost/leftmost square
		screen.fill(black)
		screen.blit(titleFont.render("Game Screen",1,white),(width/2,height/2))

#show beginning screen
screen.fill(black)
screenChange(1)

while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT: sys.exit()

	clicked=pygame.mouse.get_pos()

	if screenNum==2 and custMenu==True:
		if clicked[0]>boxx and clicked[0]<boxx+boxwidth:
				if clicked[1]>45*height/100 and clicked[1]<(45*height/100)+boxheight:
					#upscroll
					if event.type==pygame.MOUSEBUTTONUP and event.button==5 and custWd<25:
						custWd+=1
					#downscroll
					elif event.type==pygame.MOUSEBUTTONUP and event.button==4 and custWd>10:
						custWd-=1
				elif clicked[1]>53*height/100 and clicked[1]<(53*height/100)+boxheight:
					#upscroll
					if event.type==pygame.MOUSEBUTTONUP and event.button==5 and custHt<25:
						custHt+=1
					#downscroll
					elif event.type==pygame.MOUSEBUTTONUP and event.button==4 and custHt>10:
						custHt-=1

				if clicked[1]>59*height/100 and clicked[1]<63*height/100:
					if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
						#start
						if clicked[0]>11*width/32 and clicked[0]<15*width/32:
							cell=[]
							fieldGen([custWd,custHt])
							"""
							while gameOver==False:
								cellCheck([clicked[0],clicked[1]])
							"""
						#cancel
						elif clicked[0]>17*width/32 and clicked[0]<21*width/32:
							custMenu=False
							screenChange(2)

	if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:

		#main menu screen
		if screenNum==1:
			if clicked[0]>width/4 and clicked[0]<3*width/4:
				#go to size selection screen
				if clicked[1]>20*height/40 and clicked[1]<25*height/40:
					custMenu=False
					screenChange(2)
				#go to high score screen
				elif clicked[1]>26*height/40 and clicked[1]<31*height/40:
					screenChange(3)
				#go to directions screen
				elif clicked[1]>32*height/40 and clicked[1]<37*height/40:
					screenChange(4)

		#game screen
		elif screenNum==2:
			if clicked[1]>height/20 and clicked[1]<(height/20)+(width/10):
				#go to main menu
				if clicked[0]>4*width/5 and clicked[0]<9*width/10:
					screenChange(1)
			elif clicked[1]>6*height/20 and clicked[1]<(6*height/20)+(5*width/12):
				if clicked[0]>width/15 and clicked[0]<(width/15)+(5*width/12):
					cell=[]
					fieldGen([10,10])
					"""
					while gameOver==False:
						cellCheck([clicked[0],clicked[1]])
					"""
				elif clicked[0]>8*width/15 and clicked[0]<(8*width/15)+(5*width/12):
					cell=[]
					fieldGen([15,15])
					"""
					while gameOver==False:
						cellCheck([clicked[0],clicked[1]])
					"""
			elif clicked[1]>13*height/20 and clicked[1]<(13*height/20)+(5*width/12):
				if clicked[0]>width/15 and clicked[0]<(width/15)+(5*width/12):
					cell=[]
					fieldGen([20,20])
					"""
					while gameOver==False:
						cellCheck([clicked[0],clicked[1]])
					"""
				elif clicked[0]>8*width/15 and clicked[0]<(8*width/15)+(5*width/12) and custMenu==False:
					custMenu=True
					screenChange(2)

		#directions screen
		elif screenNum==3:
			if clicked[1]>height/20 and clicked[1]<(height/20)+(width/10):
				#main menu
				if clicked[0]>4*width/5 and clicked[0]<9*width/10:
					screenChange(1)

		#high score screen
		elif screenNum==4:
			if clicked[1]>height/20 and clicked[1]<(height/20)+(width/10):
				#main menu
				if clicked[0]>4*width/5 and clicked[0]<9*width/10:
					screenChange(1)

		#add delay between click detections?
