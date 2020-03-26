"""
Egyptian War!
v 2.0 - straight card play, single player, pygame gui
!!!add save file creation/modification/load capability
"""

import sys,random,pprint,pygame,pdb
from datetime import datetime

#INITIALIZE PYGAME
pygame.init()
size=width,height=(512,338)

#COLORS
black=(0,0,0)
white=(255,255,255)
lgrey=(196,196,196)
dgrey=(128,128,128)
red=(224,0,0)
orange=(255,128,0)
yellow=(224,224,0)
green=(0,224,0)
cyan=(0,255,255)
blue=(0,0,224)
purple=(128,0,128)
pink=(224,0,224)

#WINDOW ATTRIBUTES
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Egyptian War')

#FONTS
largeFont=pygame.font.Font(None,50)
mediumFont=pygame.font.Font(None,28)
smallFont=pygame.font.Font(None,20)
tinyFont=pygame.font.Font(None,14)

#ITEM TRACKERS
dictScreen={} #screen tracker as {key:[visible,{object ID,object}}
listComps=[] #competitor tracker as [(competitor,difficulty),...]
listSlaps=[] #rule tracker as [rule,...]
dictHands={} #hand tracker as {competitor:[(order,active),[card,...]]}

#BEGIN GUI CLASSES
class Label:
	global screen,width,height
	def __init__(self,pos,color,text,font,centered=False):
		self.pos=pos #as (x,y)
		self.color=color #as (r,g,b)
		self.text=text #as string
		caption=font.render(text,1,color)
		height=caption.get_height()
		self.font=(font,caption,height) #as font
		self.centered=centered #as boolean
	def draw(self):
		w=self.font[1].get_width()+15
		h=self.font[1].get_height()+15
		lblRect = (self.pos[0],self.pos[1],w,h)
		ctrPos=self.font[1].get_rect(center=(self.pos))
		pos=ctrPos if self.centered else self.pos
		screen.blit(self.font[1],pos)
		pygame.display.update(lblRect)

class Slider:
	global screen,width,height,mousePos
	def __init__(self,id,vals=[1,(1,2),{1:1,2:2}],pos=(0,0),caption='Default'):
		self.id=id
		self.vals=vals #output as int, val range as (min=int,max=int), output list as dict
		#NOTE!!! output list dictionary must have integers as keys
		(min,max)=self.vals[1]
		self.caption=caption+': '+str(self.vals[2].get(self.vals[0])) #caption
		self.active=True #as boolean; allow/disallow user interactivity
		key=maxLen=0
		for item in vals[2]: #find longest possible output
			if len(str(vals[2][item]))>maxLen:
				key,maxLen=item,len(str(vals[2][item]))
			else:
				key,maxLen=key,maxLen
		(x,y)=(int(pos[0]),int(pos[1]))
		maxLen=smallFont.render(caption+': '+str(vals[2][key]),1,color)
		leftEnd=int(x+maxLen.get_width()+(width/50)) #length of the longest item
		rightEnd=int(leftEnd+(width/6))
		sldrHt=int(y+(maxLen.get_height()/2))
		self.pos=[pos,leftEnd,rightEnd,sldrHt] #slider positional values
		self.points=[]
		for x in range(max-min+1):
			xMod=int(x*(rightEnd-leftEnd)/(max-min))
			ptPos=(leftEnd+xMod,sldrHt)
			ptVals=[lgrey,ptPos,3] if x+min != vals[0] else [green,ptPos,4]
			self.points.append(ptVals) #slider value indicators positions/colors
	def draw(self):
		color=white if self.active else dgrey
		caption=smallFont.render(self.caption,1,color)
		(x,y)=self.pos[0]
		(w,h)=(self.pos[2]-self.pos[0][0]+int(width/50),caption.get_height())
		pygame.draw.rect(screen,black,(x,y,w,h)) #set blank background rect
		screen.blit(caption,self.pos[0]) #draw caption
		#draw slider line, value indicators (min to max)
		pygame.draw.line(screen,color,(self.pos[1],self.pos[3]),(self.pos[2],self.pos[3]),3)
		for x in range(len(self.points)):
			pygame.draw.circle(screen,self.points[x][0],self.points[x][1],self.points[x][2])
		pygame.display.update((x,y,w,h)) #(re)draw slider
	def click(self):
		area=int(self.points[1][1][0]-self.pos[1])/2
		min=self.vals[1][0]
		(mouseX,mouseY)=mousePos
		for x in range(len(self.points)): #compare mouse position to interactive areas
			(self.points[x][0],self.points[x][2])=(lgrey,3) #reset to lgrey
			if mouseX>self.pos[1] and mouseX<self.pos[1]+area:
					self.vals[0]=self.vals[1][0] #min
			elif mouseX>self.pos[2]-area and mouseX<self.pos[2]:
					self.vals[0]=self.vals[1][1] #max
			elif mouseX>self.points[x][1][0]-area and mouseX<self.points[x][1][0]+area:
					self.vals[0]=x+min #any value between min and max
		val=self.vals[0]
		(self.points[val-min][0],self.points[val-min][2])=(green,4) #value circle: green
		self.caption=self.caption.split(':')[0]+': '+str(self.vals[2].get(val)) #update slider caption
		self.draw() #redraw slider to reflect changes

class TextButton:
	global screen,width,height,mousePos,sfName,listComps,listSlaps,dictHands
	def __init__(self,id,pos,font,caption='Default'):
		self.id=id
		self.caption=caption #as string
		self.font=font
		(x,y)=pos #as (x,y)
		captionText=font.render(caption,1,black)
		(w,h)=(captionText.get_width()+15,captionText.get_height()+15)
		self.pos=[x,y,(w,h)] #list form so x and y can change as needed
		self.active=True #as boolean; default=True
	def draw(self):
		(x,y,(w,h))=self.pos
		captionText=self.font.render(self.caption,1,black)
		captionPos=captionText.get_rect(center=(x+(w/2),y+(h/2)))
		color=lgrey if self.active else dgrey
		pygame.draw.rect(screen,color,(x,y,w,h))
		screen.blit(captionText,captionPos)
	def click(self):
		sfERS=open(sfName,'w+')
		if self.id=='tbNg':
			list=dictScreen[1][1]
			#set up save file
			for item in list:
				if 'sldr' in item and item!='sldrCount':
					competitor.append((item,item.active,item.val[0]))
				elif 'cb' in item and item!='cbSlap':
					listSlaps.append((item,item.active,item.val))
			lines=competitor+listSlaps
			for line in lines:
				if line[1]:
					sfERS.write(str(line[0])+': '+str(line[2]))
			sfERS.close()
			print('start new game')
			screenChange(2)
		elif self.id=='tbCg':
			#set up game using save file
			#open save file
			#for rule in rules:
			#if rule[1]:
			#add rule to gameplay dictionary
			print('continue saved game')
			screenChange(2)
		elif 'DB' in self.id:
			if self.caption=='Yes':
				screenChange(1)
			elif self.caption=='No':
				screenChange(2)
		sfERS.close()

class Checkbox:
	global screen,width,height
	def __init__(self,id,pos,caption):
		self.id=id
		self.caption=caption #as string
		h=smallFont.render(caption,1,white).get_height()
		w=smallFont.render(caption,1,white).get_width()+h
		self.pos=(pos[0],pos[1],w,h) #pos as (x,y)
		self.val=False #as boolean; default False
		self.active=False #as boolean; default False
	def draw(self):
		(x,y,w,h)=self.pos
		color=white if self.active else dgrey
		cbText=smallFont.render(self.caption,1,color)
		pygame.draw.rect(screen,black,self.pos) #set blank background rect
		pygame.draw.rect(screen,color,(x,y+(h/4),(h/2),(h/2)),1) #checkbox
		if self.val: #if true, check box
			pointList=[(x,y+(h/4)),(x+(h/4),y+(h/2)),(x+(h/2),y)]
			pygame.draw.lines(screen,color,False,pointList,2) #checkmark!!!
		x+=h
		screen.blit(cbText,(x,y)) #caption
		pygame.display.update(self.pos)
	def click(self):
		self.val=not self.val #toggle value
		self.draw()

class PlayButton: #draw menu screen icon
	global screen,width,height,mousePos
	def __init__(self,id,pos,size):
		self.id=id
		self.pos=pos #as (x,y)
		self.size=size #as int (because square)
		self.paused=False #as boolean; default "Pause"; pause icon shows
		self.active=True #as boolean; always True
	def draw(self):
		(x,y,z)=(self.pos[0],self.pos[1],self.size)
		bounds=(x,y,z,z)
		if self.paused: #play icon
			pygame.draw.rect(screen,green,bounds) #background
			pointList=[]
			pointList.append((x+(z/4),y+(z/4))) #top point
			pointList.append((x+(3*z/4),y+(z/2))) #far right point
			pointList.append((x+(z/4),y+(3*z/4))) #bottom point
			pygame.draw.polygon(screen,white,pointList)
		else: #pause icon
			pygame.draw.rect(screen,red,bounds) #background
			v,w=z/7,z/6
			rect1=(x+(1*v),y+w,2*v,4*w) #left rect
			rect2=(x+(4*v),y+w,2*v,4*w) #right rect
			pygame.draw.rect(screen,white,rect1)
			pygame.draw.rect(screen,white,rect2)
		pygame.display.update(bounds)
	def click(self):
		if self.paused:
			print('3\n2\n1\nrestart game') #placeholder
			#countdown to game restart (3,2,1)
		else:
			pdb.set_trace()
			print('pause game')
			for list in dictScreen:
				if dictScreen[list][0]:
					dict=dictScreen[list][1]
			msg='Exit to lobby?'
			opts=['Yes','No']
			dbPause=DialogBox('Pause',msg,opts)
			dict.update({'Pause':dbPause})
			dbPause.draw() #open dialog box
			pygame.display.update()
			chosen=clicked=False
			while not chosen:
				if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
					clicked=True
				if clicked and objCheck(mousePos)!='':
					dict[objCheck(mousePos)].click()
					chosen=True
		self.paused=not self.paused #toggle
		self.draw()

class DialogBox:
	global screen,width,height
	def __init__(self,id,msg,opts=['Yes','No']):
		self.id=id #as string; use to differentiate between boxes on same screen
		self.msg=msg #msg as string
		self.opts=opts #opts as list of button captions; 2 max
	def draw(self):
		active=screenCheck() #find active screen
		msg=smallFont.render(self.msg,1,black) #display message
		msgW,msgH=msg.get_width(),msg.get_height()
		msgX=(width-msg.get_width())/2
		msgY=(height-msg.get_height())/2
		optCount=tbDBwidth=0
		for opt in self.opts:
			optCount+=1
			tbDB=TextButton('tbDB'+self.id+str(optCount),(0,0),smallFont,opt)
			dictScreen[active][1].update({tbDB.id:tbDB})#option buttons
			tbDBwidth+=tbDB.pos[2][0]
		tbDBwidth+=(width/50)*len(self.opts)
		dbRect=(msgX-15,msgY-15,msgW+30,msgY+tbDB.pos[2][1]) #light grey background rect
		pygame.draw.rect(screen,lgrey,(dbRect))
		screen.blit(msg,(msgX,msgY))
		tbDB1=dictScreen[active][1]['tbDB'+self.id+'1']
		tbDB2=dictScreen[active][1]['tbDB'+self.id+'2']
		tbDB1.pos[0]=int((width-tbDBwidth)/2) #change tbDB1 x coord
		tbDB2.pos[0]=int(tbDB1.pos[0]+(tbDBwidth-tbDB2.pos[2][0])) #change tbDb2 x coord
		tbDB1.pos[1]=tbDB2.pos[1]=int(msgY+(msgH*2.25)) #change y coord
#END GUI CLASSES

#BEGIN OBJECT RENDER DEFINITIONS
#Lobby screen
dictScreen.update({1:[True,{}]}) #prep index of Lobby screen items; initially visible
lblTitle=Label((width/2,height/8),white,'Egyptian War',largeFont,True)
dictScreen[1][1].update({'lblTitle':lblTitle}) #add to Lobby screen index
newY=lblTitle.pos[1]+(lblTitle.font[2]/2)+(height/25)
lblPlayer=Label((width/18,newY),white,'Player Options',mediumFont,False)
dictScreen[1][1].update({'lblPlayer':lblPlayer}) #add to Lobby screen index

#slider, checkbox dictionaries
dictCount={
	2: 2,
	3: 3,
	4: 4,
	5: 5,
}

dictDiff={
	1: 'Easy',
	2: 'Medium',
	3: 'Hard'
}

dictSlaps={
	1: 'Doubles',
	2: 'Sandwiches',
	3: 'Hoagies',
	4: 'Consecutives'
}

#slider creation
newY=lblPlayer.pos[1]+lblPlayer.font[2]+(height/25)
countVals=[2,(2,5),dictCount]
countPos=(width/18,newY)
countID='Competitors'
sldrCount=Slider('sldrCount',countVals,countPos,countID) #competitor count slider
dictScreen[1][1].update({sldrCount.id:sldrCount}) #add to Lobby screen index
countHeight=int((sldrCount.pos[3]-sldrCount.pos[0][1])*2)
countBottom=int(sldrCount.pos[0][1])
yMod=countHeight+int(height/25)
diffVals=[1,(1,3),dictDiff]
for x in range(sldrCount.vals[1][1]):
	diffPos=(width/18,countBottom+(yMod*(x+1)))
	diffID='Comp '+str(x+1)+' Difficulty'
	sldrDiff=Slider('sldrDiff'+str(x+1),diffVals,diffPos,diffID) #computer difficulty slider
	dictScreen[1][1].update({sldrDiff.id:sldrDiff}) #add to Lobby screen index

#button creation
tbNg=TextButton('tbNg',(0,0),mediumFont,'New Game') #new game
dictScreen[1][1].update({tbNg.id:tbNg}) #add to Lobby screen index
tbCg=TextButton('tbCg',(0,0),mediumFont,'Continue Game') #continue game
dictScreen[1][1].update({tbCg.id:tbCg}) #add to Lobby screen index
tbWidth=int(tbNg.pos[2][0]+(width/50)+tbCg.pos[2][0])
tbNg.pos[0]=int((width-tbWidth)/2) #change ng x coord
tbCg.pos[0]=int(tbNg.pos[0]+(tbWidth-tbCg.pos[2][0])) #change cg x coord
tbNg.pos[1]=tbCg.pos[1]=int(countBottom+(yMod*(sldrCount.vals[1][1]+1.25))) #change y coord

#checkbox creation
diffRt=0
objs=dictScreen[1][1]
for obj in objs: #find max slider width
	if 'sldrDiff' in obj:
		diffRt=objs[obj].pos[2] if objs[obj].pos[2]>diffRt else diffRt
newX=diffRt+(width/25) #use max slider width to determine x
newY=lblPlayer.pos[1] #same y as lblPlayer
lblRules=Label((newX,newY),white,'Gameplay Rules',mediumFont,False)
dictScreen[1][1].update({'lblRules':lblRules}) #add to Lobby screen index
newY=lblRules.pos[1]+(lblRules.font[2]/2)+(height/20)
cbSlap=Checkbox('cbSlap',(newX,newY),'Slaps?') #master checkbox
dictScreen[1][1].update({cbSlap.id:cbSlap}) #add to Lobby screen index
newX+=width/25
yMod=smallFont.render(cbSlap.caption,1,white).get_height()+int(height/50)
for x in range(len(dictSlaps)):
	newY+=yMod
	cbRule=Checkbox('cbRule'+str(x+1),(newX,newY),dictSlaps[x+1]) #individual rule checkbox
	dictScreen[1][1].update({cbRule.id:cbRule}) #add to Lobby screen index

#save file check
sfName='sfERS.txt'
sfERS=open(sfName,'w+')
sfText=sfERS.read()
sfERS.close()
#End Lobby screen items

#Game screen
dictScreen.update({2:[False,{}]}) #prep index of Game screen items; initially hidden
pbGame=PlayButton('pbGame',(17*width/20,height/20),width/11) #play/pause button
dictScreen[2][1].update({pbGame.id:pbGame}) #add to Game screen index
#played card area (rounded rect)
#hand track (same color as bg; not visible)
#hands (number of hands=compCount+1)
#card representation (rounded rect,smaller than main)
#player name above
#number of cards in hand below
#sidebar on right to track played cards, hand results
#END OBJECT RENDER DEFINITIONS

#BEGIN GAMEPLAY FUNCTIONS
def screenChange(screenNum): #draws menu or game screen; screenNum as int
	screen.fill(black)
	items=['sldr','cb','tb','pb']
	for list in dictScreen:
		dict=dictScreen[list][1]
		if list==screenNum:
			dictScreen[list][0]=True
			for entry in dict:
				if 'lbl' not in entry and entry.isalpha():
					dict[entry].active=True
					parentCheck(entry) #update any dependent objects
		else:
			dictScreen[list][0]=False
			for entry in dict:
				for item in items:
					if item in entry: dict[entry].active=False
	for obj in dictScreen[screenNum][1]:
		dictScreen[screenNum][1][obj].draw() #draw each visible object
	pygame.display.update()

def screenCheck(): #check which screen is active
	screen=0
	for list in dictScreen:
		screen=dictScreen[list][0] if dictScreen[list][0] else 0
		if screen!=0: break
	return screen

def objCheck(pos): #returns dictScreen key of clicked object; pos as (x,y)
	global mousePos
	x1=x2=y1=y2=0
	(mouseX,mouseY)=mousePos
	dict=dictScreen[screenCheck()][1]
	for obj in dict: #check if active area was clicked
		if 'sldr' in obj: #slider
			x1,x2=dict[obj].pos[0][0],dict[obj].pos[2]
			y1,y2=dict[obj].pos[3]-15,dict[obj].pos[3]+15
		elif 'cb' in obj: #checkbox
			x1,x2=dict[obj].pos[0],dict[obj].pos[0]+dict[obj].pos[2]
			y1,y2=dict[obj].pos[1],dict[obj].pos[1]+dict[obj].pos[3]
		elif 'tb' in obj: #textbutton
			x1,x2=dict[obj].pos[0],dict[obj].pos[0]+dict[obj].pos[2][0]
			y1,y2=dict[obj].pos[1],dict[obj].pos[1]+dict[obj].pos[2][1]
		elif 'pb' in obj: #playpause
			x1,x2=dict[obj].pos[0],dict[obj].pos[0]+dict[obj].size
			y1,y2=dict[obj].pos[1],dict[obj].pos[1]+dict[obj].size
		else:
			continue
		area=obj if (x1<mouseX<x2 and y1<mouseY<y2) else ''
		if area!='': break #once the correct object is found, exit loop
	return area

def parentCheck(obj): #redraws any dependent objects; obj as str (object name)
	global listSlaps
	dict=dictScreen[screenCheck()][1]
	item=dict.get(obj, '') #if object not in active screen, do nothing
	if item!='':
		if 'sldr' in obj:
			for diff in dict:
				if 'sldrDiff' in diff:
					dict[diff].active=True if \
					int(diff.split('sldrDiff')[1])<=\
					dict[obj].vals[0] else False
					dict[diff].draw()
		elif 'cb' in obj:
			for rule in dict:
				if 'cb' in rule and not rule.isalpha():
					dict[rule].active=True if dict[obj].val \
					else False
					dict[rule].draw()
		elif 'tb' in obj:
			dict[obj].active=True if len(sfText)>0 or obj=='tbNg' else False

def rearrange(listInput,index):
	listInput.append(listInput[index])
	listInput.pop(index)

def playCard(playerIndex,handIndex):
	hand.append(player[playerIndex][2][0])
	history.append([])
	history[handIndex].append([player[playerIndex][0],[hand[len(hand)-1][0],hand[len(hand)-1][1]]])
	print('\n'+player[playerIndex][0]+' played the '+hand[len(hand)-1][0]+' of '+hand[len(hand)-1][1])
	player[playerIndex][2].pop(0)
	player[playerIndex][1]=len(player[playerIndex][2])

	if player[playerIndex][1]==0:
		removePlayer(playerIndex)

	if len(player)==1: #if there is only one player left
		print('\nCongratulations, '+player[0][0]+'! You won the game!')
		print('Goodbye!')
		pprint.pprint(history)
		sys.exit()

def chooseNext():
	global person
	if person+1>=len(player):
		person=0
	else:
		person+=1

def removePlayer(playerIndex):
	print('\nSorry, '+player[playerIndex][0]+', you\'re out of cards! Goodbye!')
	player.pop(playerIndex)
#END GAMEPLAY FUNCTIONS

values=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits=['Hearts','Diamonds','Clubs','Spades']
deck=[]
for suit in suits: #create deck
	for value in values:
		deck.append([value,suit])

for x in range(random.randrange(5,11)): #shuffle cards
	for y in range(len(deck)):
		rearrange(deck,random.randrange(0,len(deck)))


#BEGIN GAME CODE
screenChange(1) #activate lobby screen
clicked=scrollUp=scrollDown=False

while 1: #loop until sys.exit() is called
	mousePos=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
			clicked=True
		dict=dictScreen[screenCheck()][1]
		obj=objCheck(mousePos)
		if obj!='':
			if clicked: #only allow one click action per click
				if dict[obj].active:
					dict[obj].click()
				if 'lbl' not in obj and 'pb' not in obj \
				and 'db' not in obj and obj.isalpha():
					parentCheck(obj) #change object.active as needed
				clicked=False
	#PRESERVE GAMEPLAY CODE BELOW
	"""
	human=0
	computer=0
	players=human + computer

	hChosen=cChosen=False #numbers of players
	invalid=0 #count number of invalid entries
	while hChosen==False: #how many human players? (1-6)
		checkInvalid()
		human=str(input('\nHow many human players will there be? '))
		if human.isdigit()==False or 1>int(human)>6: #if input size/chartype is wrong
			printInvalid('Please enter a digit between 1 and 6.')
		else:
			human=int(human)
			if human==6: #skip computer player code
				players=human + computer
				cChosen=True
			hChosen=True

	invalid=0	#reset invalid counter
	while cChosen==False: #how many computer players? (0-5)
		checkInvalid()
		computer=str(input('\nHow many computer players will there be? '))
		cLevel=[]
		if computer.isdigit()==False or 0>int(computer)>6-human: #if input size/chartype is wrong
			printInvalid('Please enter a digit between 0 and ' + str(6-human) + '.')
		elif human + int(computer)==1: #if there is only one human player
			printInvalid('Please enter a digit between 1 and ' + str(6-human) + '.')
		else:
			computer=int(computer)
			if computer != 0: #choose computer player difficulty (slap likelihood, speed in seconds)
				for x in range(computer):
					level=str(input('\nChoose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
					if level.isdigit()==False or 1>int(level)>3: #if input size/chartype is wrong
						printInvalid('Please enter a digit between 1 and 3.')
					else:
						if int(level)==1: #1.5 to 2 seconds, 66% chance to slap
							cLevel.append(['Computer ' + str(x+1),'Easy'])
						elif int(level)==2: #1 to 1.5 seconds, 75% chance to slap
							cLevel.append(['Computer ' + str(x+1),'Medium'])
						else: #0.5 to 1 seconds, 100% chance to slap
							cLevel.append(['Computer ' + str(x+1),'Hard'])
			players=human + computer
			cChosen=True

	player=[] #player name, number of cards, cards in hand as list
	namedPlayers=0
	while namedPlayers<players:
		checkInvalid()
		if namedPlayers<human:
			invalid=0
			playerName=str(input('\nPlayer ' + str(namedPlayers+1) + ', what is your name? '))
			if playerName=='':
				printInvalid('Please enter your name.')
			else:
				player.append([playerName,0,[]])
				namedPlayers+=1
		else:
			player.append([cLevel[namedPlayers-human][0] + ' (' + cLevel[namedPlayers-human][1] + ')',0,[]])
			namedPlayers+=1

	starter=random.randrange(0,len(player)) #randomize starting player
	print('\n' + player[starter][0] + ' will start!')

	for x in range(starter): #rearrange player order
		rearrange(player,0)

	person=0
	for card in deck: #deal cards evenly between players
		player[person][2].append(card)
		player[person][1]+=1
		chooseNext()

	for p in player: #list players, number of cards in players' hands
		print(p[0] + ' has ' + str(p[1]) + ' cards.')

	gameOver=False
	person=0
	handNum=0
	hand=[]
	history=[]

	while gameOver==False: #begin play
		print('\nPress Enter to start the next hand.') #player must approve the start of each hand
		if input('Any other entries will end the program. ') != '':
			print('Goodbye!')
			sys.exit()
		else:
			handOver=False
			playCard(person, handNum)
			chooseNext()

			while handOver==False:
				#if the played card requires a slap
				if hand[len(hand)-1][0] not in ['Jack','Queen','King','Ace']: #if a number is played
					playCard(person, handNum)
					chooseNext()
				else: #if a face card is played
					play=0
					played=0
					for x in ['Jack','Queen','King','Ace']: #how many cards the next player must play
						play+=1 #J=1, Q=2, K=3, A=4
						if x==hand[len(hand)-1][0]:
							break
					print(player[person][0] + ' must play ' + str(play) + ' card(s).')

					while played<play: #play the required number of cards
						playCard(person, handNum)
						if hand[len(hand)-1][0] in ['Jack','Queen','King','Ace']: #if a face card is played
							chooseNext()
							break
						else: #if a number is played
							if played==play-1: #if the required number of face cards is reached
								if person-1<0:
									person=len(player)-1
								else:
									person-=1
								print('\n' + player[person][0] + ' wins ' + str(len(hand)) + ' cards this hand!\n')
								for card in hand: #add all cards to winner's hand
									player[person][2].append(card)
								hand=[]
								handNum+=1
								for p in player:
									p[1]=len(p[2])
									print(p[0] + ' has ' + str(p[1]) + ' cards.')
								handOver=True
						played+=1
	"""
#END GAME CODE
