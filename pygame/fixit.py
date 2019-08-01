"""
redo components of other projects
so that they actually work!!

current issue:
ers.py
get function to change global variable for screen tracking
"""

import sys, pygame
pygame.init()

size=width,height=(512,338)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Y I K E S")
largeFont=pygame.font.Font(None,50)
Clock = pygame.time.Clock()

black=(0,0,0)
white=(255,255,255)
orange=(255,128,0)

def screenChange():
	screen.fill(black)
	x,y=width/2,height/2
	i=0
	timeStart = pygame.time.get_ticks()
	while pygame.time.get_ticks()-timeStart<301:
		if pygame.time.get_ticks()-timeStart%100==0:
			a = largeFont.render(str(3-i),1,white)
			(w,h) = (a.get_width(),a.get_height())
			b = a.get_rect(center=(x,y))
			pygame.draw.rect(screen,black,(x,y,w,h))
			screen.blit(a,b)
			pygame.display.update((x,y,w,h))

screen.fill(black)
placeholder=largeFont.render('Under Construction',1,orange)
position=placeholder.get_rect(center=(width/2,height/2))
screen.blit(placeholder,position)
clicked=False

while 1:
	Clock.tick()
	for event in pygame.event.get():
		if event.type==pygame.QUIT: sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN and event.button==1: clicked=True

	if clicked==True:
		screenChange()
		clicked=False

	pygame.display.update()
