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
gRow = gCol = custWd = custHt = 10
custMenu = gameOver = False
firstGuess = True
scrName = "home"

class HouseIcon: #draw menu screen icon
    global screen, width, height
    def __init__(self,pos,size,color):
        self.pos = pos #as (x,y)
        self.size = size #as int
        self.color = color #as (r,g,b)

    def draw(self):
        (x,y,z) = (self.pos[0],self.pos[1],self.size)
        pygame.draw.rect(screen,self.color,(x,y,z,z))
        pygame.draw.line(screen,white,(x+(z/25),y+(9*z/20)),(x+(z/2),y+(z/25)),2)
        pygame.draw.line(screen,white,(x+(z/2),y+(z/25)),(x+(24*z/25),y+(9*z/20)),2)
        pygame.draw.rect(screen,white,(x+(z/6),y+(17*z/50),2*z/3,7*z/12),2)
        pygame.draw.rect(screen,white,(x+(3*z/8),y+(87*z/200),z/4,49*z/100),1)

    def click(self):
        screenChange(1)

class Button:
    global screen, width, height
    def __init__(self,pos,size,color,caption):
        self.pos = pos #as (x,y)
        self.size = size #as (width,height)
        self.color = color #as (r,g,b)
        self.caption = caption #as string, \n delimiter optional

    def draw(self):
        (x,y,w,h) = (self.pos[0],self.pos[1],self.size[0],self.size[1])
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
        elif "Small" in self.caption or "Medium" in self.caption \
        or "Large" in self.caption or "Start" == self.caption:
            screnChange(3)
        elif self.caption == "How to Play":
            screenChange(4)
        elif self.caption == "High Scores":
            screenChange(5)

class Menu:
    global screen, width, height, mouseX, mouseY
    def __init__(self,pos,msg,opts):
        self.pos = pos #as (x,y)
        self.msg = msg #as string, \n delimiter
        self.opts = opts #as [option,(min,max)] per option

    def draw(self):
        (x,y) = (self.pos[0],self.pos[1])
        items = []
        lines = self.msg.split("\n")
        menuFont = pygame.font.Font(None,int(height/(30+len(lines))))
        for ind,line in enumerate(lines):
            msgText = menuFont.render(line,1,black)
            xMod = width/50
            yMod = msgText.get_height()*(ind+1)
            msgPos = (x+xMod,y+yMod)
            items.append([msgText,msgPos])
        yMod = (msgText.get_height()*(len(lines)+1))+height/50
        lblRowWidth = 0
        for ind,lbl in enumerate(self.opts):
            lblText = menuFont.render(lbl[0],1,black)
            items.append([lblText])
            lblRowWidth += items(len(items)-1).get_width()+width/50
            optText = menuFont.render(str(lbl[1][0]),1,black)
            items.append([optText])
        w = width/2
        h = yMod+(lblText.get_height()+optText.get_height())+height/50
        self.pos = (self.pos[0],self.pos[1],w,h)
        pygame.draw.rect(screen,grey,(x,y,w,h))
        for ind,item in enumerate(items):
            if ind > len(lines)-1:
                (x1,y1) = (item[1][0],item[1][1]) #modify
                item.append((x1,y1))
                if ind%2 != len(lines)%2:
                    (w1,h1) = (item[0].get_width(),item[0].get_height())
                    pygame.draw.rect(screen,white,(x1,y1,w1,h1))
            screen.blit(item[0],item[1])
        pygame.display.update((x,y,w,h))
        #add choice buttons

    def click(self):
        screenChange(2) #placeholder

    def scroll(self):
        screenChange(2) #placeholder

class Cell:
    global screen, width, height, mouseX, mouseY
    def __init__(self,pos):
        self.pos = pos

home = HouseIcon((17*width/20,height/20),width/11,blue)
btnNG = Button((width/4,20*height/40),(width/2,height/8),green,"New Game")
btnHTP = Button((width/4,26*height/40),(width/2,height/8),blue,"How to Play")
btnHS = Button((width/4,32*height/40),(width/2,height/8),purple,"High Scores")
btnSML = Button((5*width/40,7*height/20),(7*width/20,7*width/20),red,"Small\n10x10")
btnMED = Button((21*width/40,7*height/20),(7*width/20,7*width/20),pink,"Medium\n15x15")
btnLRG = Button((5*width/40,13*height/20),(7*width/20,7*width/20),orange,"Large\n20x20")
btnCUS = Button((21*width/40,13*height/20),(7*width/20,7*width/20),yellow,
"Custom\n"+str(custWd)+"x"+str(custHt))

def screenTitle(caption):
    scrTitle = pygame.font.Font(None,60).render(caption,1,white)
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
        if custMenu == True:
            menuText = "Choose your grid size below by \nscrolling the mouse wheel."
            menuOpt = [["Grid Width",(10,20)],["Grid Height",(10,20)]]
            menuCUS = Menu((width/4,height/3),menuText,menuOpt)
            objList.append(menuCUS)
            """
            #nnnnn(yyyy)nn(yyyy)nnnnn
            menuBtnW = menuCUS.pos[2]/5
            menuBtnH = pygame.font.Font(None,int(height/(30+len\
            (menuText.split("\n"))))).render("l",1,black).get_height()+4
            menuBtnSize = (menuBtnW,menuBtnH)
            btnSTpos = (menuCUS.pos[0],menuCUS.pos[1])
            btnCNpos = (menuCUS.pos[0],menuCUS.pos[1])
            btnST = Button((btnSTpos),(menuBtnSize),grey,"Start")
            btnCN = Button((btnCNpos),(menuBtnSize),grey,"Cancel")
            objList.append(menuCUS)
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
            """
        for obj in objList:
            obj.draw()
    elif index == 3:
        scrName = "game"
        #for cell in cells:
            #w = width/
    elif index == 4:
        scrName = "directions" #directions
        home.draw() #back to home
        screenTitle("How to Play") #screen title
    elif index == 5: #high scores
        scrName = "highscores"
        home.draw() #back to home
        screenTitle("High Scores") #screen title
    pygame.display.update()


def fieldGen(gameMode): #generate the game field
    cells = {}
    fieldSize = gameMode[0]*gameMode[1]
    mineNum = random.randrange(int(.1*fieldSize),int(.25*fieldSize)+1) #10-25% of cells are mines
    mineCount = 0
    for x in range(0,gameMode[0]):
        for y in range(0,gameMode[1]):
            if random.randrange(0,2) == 0:
                boom = False
            elif mineCount == mineNum:
                boom = False
            else:
                boom = True
                mineCount += 1
            #key: has mine?, user clicked?, number of adjacent mines
            cells.update({(x,y):[boom,False,0]})
    screenChange(3)

#check if cell has mine
def cellCheck(cellPos):
    if firstGuess == False:
        #reveal number of mines surrounding square, clear any swathes of vacant space
        pygame.display.update()
    else:
        #if mine exists at pos, remove and place at topmost/leftmost square
        pygame.display.update()

#show beginning screen
screen.fill(black)
screenChange(1)
clicked = scrolling = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            scrolling = True #5:up::4:down
        (mouseX,mouseY) = pygame.mouse.get_pos()

    if clicked == True:
        if scrName == "home": #main menu
            if mouseX>width/4 and mouseX<3*width/4:
                if mouseY>btnNG.pos[1] and mouseY<btnNG.pos[1]+btnNG.size[1]:
                    btnNG.click() #size select
                elif mouseY>btnHTP.pos[1] and mouseY<btnHTP.pos[1]+btnHTP.size[1]:
                    btnHTP.click() #directions
                elif mouseY>btnHS.pos[1] and mouseY<btnHS.pos[1]+btnHS.size[1]:
                    btnHS.click() #high scores
        elif scrName == "select":
            if custMenu == False: #size select
                if mouseX>home.pos[0] and mouseX<home.pos[0]+home.size \
                and mouseY>home.pos[1] and mouseY<home.pos[1]+home.size:
                    home.click() #main menu
                elif mouseX>btnSML.pos[0] and mouseX<btnSML.pos[0]+btnSML.size[0]\
                and mouseY>btnSML.pos[1] and mouseY<btnSML.pos[1]+btnSML.size[1]:
                    fieldGen([10,10]) #small
                elif mouseX>btnMED.pos[0] and mouseX<btnMED.pos[0]+btnMED.size[0]\
                and mouseY>btnMED.pos[1] and mouseY<btnMED.pos[1]+btnMED.size[1]:
                    fieldGen([15,15]) #medium
                elif mouseX>btnLRG.pos[0] and mouseX<btnLRG.pos[0]+btnLRG.size[0]\
                and mouseY>btnLRG.pos[1] and mouseY<btnLRG.pos[1]+btnLRG.size[1]:
                    fieldGen([20,20]) #large
                elif mouseX>btnCUS.pos[0] and mouseX<btnCUS.pos[0]+btnCUS.size[0]\
                and mouseY>btnCUS.pos[1] and mouseY<btnCUS.pos[1]+btnCUS.size[1]:
                    custMenu = True
                    screenChange(2)
            else:
                #what happens if menu buttons are clicked?
                #btnST
                #btnCN
                custMenu == False
        elif scrName == "directions": #directions
            if mouseY>home.pos[1] and mouseY<home.pos[1]+home.size:
                if mouseX>home.pos[0] and mouseX<home.pos[0]+home.size:
                    home.click() #main menu
        elif scrName == "highscores": #high scores
            if mouseY>home.pos[1] and mouseY<home.pos[1]+home.size:
                if mouseX>home.pos[0] and mouseX<home.pos[0]+home.size:
                    home.click() #main menu
        elif scrName == "game":
            pygame.display.update() #change later
        clicked = False

    if scrolling == True:
        scrolling = False
