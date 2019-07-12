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

class HouseIcon:
    global screen, width, height
    def __init__(self,location,size,color):
        self.location = location
        self.size = size
        self.color = color

    def draw(self):
        (x,y,z) = (self.location[0],self.location[1],self.size)
        pygame.draw.rect(screen,self.color,(x,y,z,z))
        pygame.draw.line(screen,white,(x+(z/25),y+(9*z/20)),(x+(z/2),y+(z/25)))
        pygame.draw.line(screen,white,(x+(z/2),y+(z/25)),(x+(24*z/25),y+(9*z/20)),2)
        pygame.draw.rect(screen,white,(x+(z/6),y+(17*z/50),2*z/3,7*z/12),2)
        pygame.draw.rect(screen,white,(x+(3*z/8),y+(87*z/200),z/4,49*z/100),2)

    def click(self):
        self.color = pink
        self.draw()

screen.fill(black)
clicked=False

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1: clicked=True

    clickPos = pygame.mouse.get_pos()

    home=HouseIcon((width/2,width/2),64,blue)
    home.draw()
    if clicked==True:
        if clickPos[0]>home.location[0] and clickPos[0]<home.location[0]+home.size:
            if clickPos[1]>home.location[1] and clickPos[1]<home.location[1]+home.size:
                home.click()
                clicked=False

    updateRect = pygame.Rect(home.location[0],home.location[1],home.size,home.size)
    pygame.display.update(updateRect)
