"""
Minesweeper!
"""

import sys, pygame, random
pygame.init()

size = width,height = (384,512)

black = (0,0,0)
white = (255,255,255)
grey = (196,196,196)
red = (224,0,0)
orange = (255,128,0)
yellow = (224,224,0)
green = (0,224,0)
cyan = (0,255,255)
blue = (0,0,224)
purple = (128,0,128)
pink = (224,0,224)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")
largeFont = pygame.font.Font(None,60)
mediumFont = pygame.font.Font(None,46)
smallFont = pygame.font.Font(None,30)
custWd = 10
custHt = 10
boxx = 27*width/100
boxwidth = width/8
boxheight = height/25
custMenu = False
gameOver = False
firstGuess = True
scrName = "home"

class HouseIcon: #draw menu screen icon
    global screen, width, height
    def __init__(self,location,size,color):
        self.location = location #as (x,y)
        self.size = size #as int
        self.color = color #as (r,g,b)

    def draw(self):
        (x,y,z) = (self.location[0],self.location[1],self.size)
        pygame.draw.rect(screen,self.color,(x,y,z,z))
        pygame.draw.line(screen,white,(x+(z/25),y+(9*z/20)),(x+(z/2),y+(z/25)),2)
        pygame.draw.line(screen,white,(x+(z/2),y+(z/25)),(x+(24*z/25),y+(9*z/20)),2)
        pygame.draw.rect(screen,white,(x+(z/6),y+(17*z/50),2*z/3,7*z/12),2)
        pygame.draw.rect(screen,white,(x+(3*z/8),y+(87*z/200),z/4,49*z/100),2)

    def click(self):
        screenChange(1)

home = HouseIcon((17*width/20,height/20),width/11,blue)

class Button:
    global screen, width, height
    def __init__(self,location,size,color,caption):
        self.location = location #as (x,y)
        self.size = size #as (width,height)
        self.color = color #as (r,g,b)
        self.caption = caption #as string, \n delimiter optional

    def draw(self):
        (x,y,w,h) = (self.location[0],self.location[1],self.size[0],self.size[1])
        pygame.draw.rect(screen,self.color,(x,y,w,h))
        items = self.caption.split("\n")
        buttonFont = pygame.font.Font(None,int(height/(10+len(items))))
        for ind,item in enumerate(items):
            captionText = buttonFont.render(item,1,white)
            if len(items) == 1: heightMod = h/2
            else: heightMod = (ind+2)*h/(2.5*len(items))
            captionPos = captionText.get_rect(center=(x+(w/2),y+int(heightMod)))
            screen.blit(captionText,captionPos)

    def click(self):
        if self.caption == "New Game":
            screenChange(2)
        elif self.caption == "How to Play":
            screenChange(3)
        elif self.caption == "High Scores":
            screenChange(4)

btnNG = Button((width/4,20*height/40),(width/2,height/8),green,"New Game")
btnHTP = Button((width/4,26*height/40),(width/2,height/8),blue,"How to Play")
btnHS = Button((width/4,32*height/40),(width/2,height/8),purple,"High Scores")
btnSML = Button((width/12,8*height/20),(4*width/11,4*width/11),red,"Small\n10x10")
btnMED = Button((7*width/12,8*height/20),(4*width/11,4*width/11),pink,"Medium\n15x15")
btnLRG = Button((width/12,13*height/20),(4*width/11,4*width/11),orange,"Large\n20x20")
btnCUS = Button((7*width/12,13*height/20),(4*width/11,4*width/11),yellow,
"Custom\n"+str(custWd)+"x"+str(custHt))

class Menu:
    global screen, width, height, clickPos
    def __init__(self,location,size,msg,opts):
        self.location = location #as (x,y)
        self.size = size #as (width,height)
        self.msg = msg #as string, \n delimiter
        self.opts = opts #as list of strings

    def draw(self):
        (x,y,w,h) = (self.location[0],self.location[1],self.size[0],self.size[1])
        pygame.draw.rect(screen,grey,(x,y,w,h))
        lines = self.msg.split("\n")
        menuFont = pygame.font.Font(None,int(height/(15+len(items))))
        for ind,line in enumerate(lines):
            menuText = menuFont.render(line,1,black)
            if len(items) == 1: heightMod = h/2
            else: heightMod = (ind+2)*h/(2.5*len(items))
            menuPos = (x,y+heightMod)
            screen.blit(menuText,menuPos)
        optHt = y+((len(items)+1)*h/((2.5*len(items))))
        #add option labels, scrollable areas
        #add choice buttons

def screenTitle(caption):
    scrTitle = largeFont.render(caption,1,white)
    titleRect = scrTitle.get_rect(center=(width/2,3*height/20))
    screen.blit(scrTitle,titleRect)

def screenChange(index):
    global scrName
    screen.fill(black)
    objList=[]
    if index == 1: #menu
        scrName = "home" #back to home
        screenTitle("Minesweeper") #screen title
        objList = [btnNG,btnHTP,btnHS]
        for obj in objList:
            obj.draw()
    elif index == 2: #size select
        scrName = "select"
        home.draw() #back to home
        screenTitle("Size Selection")
        objList = [btnSML,btnMED,btnLRG,btnCUS]
        for obj in objList:
            obj.draw()
        if custMenu == True:
            menuText = "Choose your grid size below by \nscrolling the mouse wheel."
            menuOpt = ["Grid Width","Grid Height"]
            menuCUS = Menu((width/4,height/3),(width/2,height/3),grey,menuText,menuOpt)
            pygame.draw.rect(screen,grey,(width/4,height/3,width/2,height/3))
            screen.blit(tinyFont.render("Choose your grid size below by",1,black),(boxx,(height/3)+(height/100)))
            screen.blit(tinyFont.render("scrolling the mouse wheel.",1,black),(boxx,(height/3)+(3*height/100)))
            screen.blit(tinyFont.render("Grid Width:",1,black),(boxx,21*height/50))
            screen.blit(tinyFont.render("Grid Height:",1,black),(boxx,25*height/50))
            pygame.draw.rect(screen,white,(boxx,45*height/100,width/8,height/25))
            pygame.draw.rect(screen,white,(boxx,53*height/100,width/8,height/25))
            screen.blit(numFont.render(str(custWd),1,black),(boxx,23*height/50))
            screen.blit(numFont.render(str(custHt),1,black),(boxx,27*height/50))
            pygame.draw.rect(screen,black,(11*width/32,59*height/100,width/8,height/25),2)
            screen.blit(tinyFont.render("Start",1,black),((11*width/32)+(3*width/100),(59*height/100)+(height/100)))
            pygame.draw.rect(screen,black,(17*width/32,59*height/100,width/8,height/25),2)
            screen.blit(tinyFont.render("Cancel",1,black),((17*width/32)+(3*width/200),(59*height/100)+(height/100)))
    elif index == 3:
        scrName = "directions" #directions
        home.draw() #back to home
        screenTitle("How to Play") #screen title
    elif index == 4: #high scores
        scrName = "highscores"
        home.draw() #back to home
        screenTitle("High Scores") #screen title
    pygame.display.update()

#generate the next field
def fieldGen(gameMode):
    fieldSize = gameMode[0]*gameMode[1]
    mineNum = random.randrange(int(.1*fieldSize),int(.25*fieldSize)+1) #10-25% of cells are mines
    mineCount = 0
    screen.fill(black)
    for x in range(0,gameMode[0]):
        for y in range(0,gameMode[1]):
            if random.randrange(0,2) == 0:
                boom = False
            elif mineCount == mineNum:
                boom = False
            else:
                boom = True
                mineCount += 1
            #grid x, grid y, has mine?, user clicked?
            cell.append([x,y,boom,False])
            pygame.draw.rect(screen,grey,((x+1)*(width/gameMode[0]),(y+1)*(height/gameMode[1]),
            width/gameMode[0],width/gameMode[0]))
            pygame.display.flip()

#check if cell has mine
def cellCheck(cellPos):
    if firstGuess == False:
        #reveal number of mines surrounding square, clear any swathes of vacant space
        screen.blit(largeFont.render("Game Screen",1,white),(width/2,height/2))
    else:
        #if mine exists at location, remove and place at topmost/leftmost square
        screen.fill(black)
        screen.blit(largeFont.render("Game Screen",1,white),(width/2,height/2))

#show beginning screen
screen.fill(black)
scrNum = 1
screenChange(scrNum)
clicked = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True
            (mouseX,mouseY) = pygame.mouse.get_pos()

    if clicked == True:
        if scrName == "home": #main menu
            if mouseX>width/4 and mouseX<3*width/4:
                if mouseY>20*height/40 and mouseY<25*height/40:
                    btnNG.click() #size select
                elif mouseY>26*height/40 and mouseY<31*height/40:
                    btnHTP.click() #directions
                elif mouseY>32*height/40 and mouseY<37*height/40:
                    btnHS.click() #high scores

        elif scrName == "select": #size select
            if mouseY>home.location[1] and mouseY<home.location[1]+home.size:
                if mouseX>home.location[0] and mouseX<home.location[0]+home.size:
                    home.click() #main menu
            elif mouseY>6*height/20 and mouseY<(6*height/20)+(5*width/12):
                cell = []
                if mouseX>width/15 and mouseX<(width/15)+(5*width/12):
                    fieldGen([10,10]) #small
                elif mouseX>8*width/15 and mouseX<(8*width/15)+(5*width/12):
                    fieldGen([10,10]) #medium
                elif mouseY>13*height/20 and mouseY<(13*height/20)+(5*width/12):
                    if mouseX>width/15 and mouseX<(width/15)+(5*width/12):
                        fieldGen([10,10]) #large
                """
                while gameOver == False:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button =  = 1:
                        cellCheck([mouseX,mouseY])
                """
            elif mouseX>8*width/15 and mouseX<(8*width/15)+(5*width/12):
                if mouseX>boxx and mouseX<boxx+boxwidth:
                    if (mouseY>45*height/100 and mouseY<(45*height/100)+boxheight) or (mouseY>53*height/100 and mouseY<(53*height/100)+boxheight):
                        if event.type == pygame.MOUSEBUTTONUP and event.button == 5 and custWd<25: #upscroll
                            custWd+= 1
                        elif event.type == pygame.MOUSEBUTTONUP and event.button == 4 and custWd>10: #downscroll
                            custWd-= 1
                if mouseY>59*height/100 and mouseY<63*height/100:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if mouseX>11*width/32 and mouseX<15*width/32: #start
                            cell = []
                            fieldGen([custWd,custHt])
                            """
                            while gameOver == False:
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button =  = 1:
                                    cellCheck([mouseX,mouseY])
                            """
                        elif mouseX>17*width/32 and mouseX<21*width/32: #cancel
                            screenChange(2)
        elif scrName == "directions": #directions
            if mouseY>home.location[1] and mouseY<home.location[1]+home.size:
                if mouseX>home.location[0] and mouseX<home.location[0]+home.size:
                    home.click() #main menu
        elif scrName == "highscores": #high scores
            if mouseY>home.location[1] and mouseY<home.location[1]+home.size:
                if mouseX>home.location[0] and mouseX<home.location[0]+home.size:
                    home.click() #main menu
        clicked = False
        #add delay between click detections?
