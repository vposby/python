"""
redo components of other projects
so that they actually work!!

current issue:
minesweeper.py
fix button clicks
"""

import sys, pygame
pygame.init()

size=width,height=(384,512)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Y I K E S")

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

class Button:
    global screen
    def __init__(self,location,size,color):
        self.location = location
        self.size = size
        self.color = color

    def drawHouse(self):
        drawHouse(self.location[0],self.location[1],self.size,self.size)

    def click(self):
        self.color = pink

    #def click(self):

def drawHouse(x,y,width,height): #draw menu screen icon
    pygame.draw.rect(screen,blue,(x,y,width,height))
    pygame.draw.line(screen,white,(x+(width/25),y+(9*height/20)),(x+(width/2),y+(height/25)),2)
    pygame.draw.line(screen,white,(x+(width/2),y+(height/25)),(x+(24*width/25),y+(9*height/20)),2)
    pygame.draw.rect(screen,white,(x+(width/6),y+(17*height/50),2*width/3,7*height/12),2)
    pygame.draw.rect(screen,white,(x+(3*width/8),y+(87*height/200),width/4,49*height/100),2)

screen.fill(black)
clicked=False

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1: clicked=True

    clickPos = pygame.mouse.get_pos()

    #clicked=pygame.mouse.get_pos()
    home=HouseIcon((int(3*width/4),int(width/4)+64),32,purple)
    home.draw()
    if clicked==True:
        houseIcon.click()
        clicked=False
    updateRect = pygame.Rect(width/4,height/4,192,192)
    pygame.display.update(updateRect)
