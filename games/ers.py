"""
Egyptian War!
v 2.0 - straight card play, single player, pygame gui
!!!make playPause button switch back to Lobby screen
!!!add .hide() to all objects
"""

import sys,random,pprint,pygame
pygame.init()

size=width,height=(512,338)
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

screen=pygame.display.set_mode(size)
pygame.display.set_caption('Egyptian War')
largeFont=pygame.font.Font(None,50)
mediumFont=pygame.font.Font(None,28)
smallFont=pygame.font.Font(None,20)
tinyFont=pygame.font.Font(None,14)

#BEGIN GUI FUNCTIONS, CLASSES
class Slider:
	global screen, width, height, mouseX, mouseY
	def __init__(self,vals=[1,(1,2),{1:1,2:2}],pos=(0,0),id='Default'):
		self.vals=vals #output as int, val range as (min=int,max=int), output list as dict
		#NOTE!!! output list dictionary must have integers as keys
		(min,max)=self.vals[1]
		self.id=id+': '+ str(self.vals[2].get(self.vals[0])) #caption
		self.active=True #as boolean; allow/disallow user interactivity
		color=white if self.active else dgrey
		caption=smallFont.render(self.id,1,color)
		key=maxLen=0
		for item in vals[2]: #find longest possible output
			key=item if len(str(vals[2][item]))>maxLen else key
		(x,y)=(int(pos[0]),int(pos[1]))
		leftEnd=int(x+vals[2][key].get_width()+(width/50)) #length of the longest item
		rightEnd=int(leftEnd+(width/6))
		sldrHt=int(y+(vals[2][key].get_height()/2))
		self.pos=[pos,leftEnd,rightEnd,sldrHt] #where the slider line goes
		self.points=[]
		for x in range(max-min+1):
			xMod=int(x*(rightEnd-leftEnd)/(max-min))
			ptPos=(leftEnd+xMod,sldrHt)
			ptVals=[lgrey,ptPos,3] if x+min != vals[0] else [green,ptPos,4]
			self.points.append(ptVals) #where the slider value indicators go

	def draw(self):
		color=white if self.active else dgrey
		caption=smallFont.render(self.id,1,color)
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
		self.id=self.id.split(':')[0]+': '+str(self.vals[2].get(val)) #update slider caption
		self.draw() #redraw slider to reflect changes

	def hover(self) :#implement later
		#add tooltip dictionary, search by object type, id/caption value
		if 'Competitor' in self.id:
			text='Number of opposing players'
		elif 'Difficulty' in self.id:
			text='corresponding computer difficulty' #change
		else:
			text='Default ToolTip'
		caption=tinyFont.render(text,1,lgrey)
		(x,y)=(mouseX+5,mouseY+5)
		(w,h)=(caption.get_width(),caption.get_height())
		screen.blit(caption,(x,y))
		pygame.display.update((x,y,w,h))

class Label:
	global screen, width, height
	def __init__(self,pos,color,text,font,centered=False):
		self.pos=pos #as (x,y)
		self.color=color #as (r,g,b)
		self.text=text #as string
		caption=font.render(text,1,color)
		height=caption.get_height()
		self.font=(font,caption,height) #as font
		self.centered=centered #as boolean
		self.visible=True #as boolean; default True

	def draw(self):
		w=self.font[1].get_width()+15
		h=self.font[1].get_height()+15
		lblRect = (self.pos[0],self.pos[1],w,h)
		ctrPos=self.font[1].get_rect(center=(self.pos))
		pos=ctrPos if self.centered else self.pos
		screen.blit(self.font[1],pos)
		pygame.display.update(lblRect)

	def hide(self):
		w=self.font[1].get_width()+15
		h=self.font[1].get_height()+15
		lblRect = (self.pos[0],self.pos[1],w,h)
		pygame.draw.rect(screen,black,lblRect)

class TextButton:
	global screen, width, height
	def __init__(self,pos,caption='Default'):
		self.caption=caption #as string
		(x,y)=pos #as (x,y)
		captionText=mediumFont.render(caption,1,white)
		(w,h)=(captionText.get_width()+15,captionText.get_height()+15)
		self.pos=[x,y,(w,h)] #list form so x and y can change as needed
		self.active=True #as boolean; default=True

	def draw(self):
		(x,y,(w,h))=self.pos
		captionText=mediumFont.render(self.caption,1,white)
		captionPos=captionText.get_rect(center=(x+(w/2),y+(h/2)))
		color=lgrey if self.active else dgrey
		pygame.draw.rect(screen,color,(x,y,w,h))
		screen.blit(captionText,captionPos)

	def click(self):
		if self.caption=='New Game':
			#set up new game using player inputs
			#look for save file in relevant directory
			#if none exists, create one
			#if one exists, overwrite
			#for rule in rules:
			#if rule[1]:
			#add rule to save file
			#add rule to gameplay dictionary
			print('start new game')
		elif self.caption=='Continue Game':
			#set up game using save file
			#open save file
			#for rule in rules:
			#if rule[1]:
			#add rule to gameplay dictionary
			print('continue saved game')
		#confirm button selection choice
		screenChange(2) #change to game screen

class PlayPause: #draw menu screen icon
	global screen, width, height
	def __init__(self,pos,size):
		self.pos=pos #as (x,y)
		self.size=size #as int (because square)
		self.paused=False #as boolean; default "Pause"; pause icon shows

	def draw(self):
		(x,y,z)=(self.pos[0],self.pos[1],self.size)
		bounds=(x,y,z,z)
		if self.paused: #play icon
			pygame.draw.rect(screen,green,bounds)
			pointList=[]
			pointList.append((x+(z/4),y+(z/4)))
			pointList.append((x+(3*z/4),y+(z/2)))
			pointList.append((x+(z/4),y+(3*z/4)))
			pygame.draw.polygon(screen,white,pointList)
		else: #pause icon
			pygame.draw.rect(screen,red,bounds)
			v=z/7
			w=z/6
			rect1=(x+(1*v),y+w,2*v,4*w)
			rect2=(x+(4*v),y+w,2*v,4*w)
			pygame.draw.rect(screen,white,rect1)
			pygame.draw.rect(screen,white,rect2)
		pygame.display.update(bounds)

	def click(self):
		if self.paused:
			print('play game') #placeholder
		else:
			print('pause game')
			#open dialog box
			#START DIALOG BOX CODE
			#return to lobby? yes no
			#if yes, return to lobby
				#screenChange(1) #lobby
			#if no, close dialog box
				#self.mode="Play"
			#END DIALOG BOX CODE
		self.paused=not self.paused #toggle
		self.draw()
		(x,y) = (width/2,height/2)
		for i in range(3):
			pygame.time.wait(100)
			a = largeFont.render(str(i+1),1,white)
			(w,h) = (a.get_width(),a.get_height())
			b = a.get_rect(center=(x,y))
			pygame.draw.rect(screen,black,(x,y,w,h))
			screen.blit(a,b)
			pygame.display.update((x,y,w,h))
		screenChange(1) #change to lobby screen

class Checkbox:
	global screen, width, height
	def __init__(self,pos,caption):
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
		if self.val:
			pointList=[(x,y+(h/4)),(x+(h/4),y+(h/2)),(x+(h/2),y)]
			pygame.draw.lines(screen,color,False,pointList,2) #if true, check box
		(x,y)=(x+h,y)
		screen.blit(cbText,(x,y)) #caption
		pygame.display.update(self.pos)

	def click(self):
		self.val=not self.val #toggle value
		self.draw()
#END GUI FUNCTIONS, CLASSES

#Begin Lobby screen items
lblTitle=Label((width/2,height/10),white,'Egyptian War',largeFont,True)
newY=lblTitle.pos[1]+(lblTitle.font[2]/2)+(height/20)
lblPlayer=Label((width/18,newY),white,'Player Options',mediumFont,False)

#slider dictionaries
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

dictRules={
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
sldrCount=Slider(countVals,countPos,countID) #competitor slider
sldrCount.active=True
countHeight=int((sldrCount.pos[3]-sldrCount.pos[0][1])*2)
countBottom=int(sldrCount.pos[0][1])
yMod=countHeight+int(height/25)
diffVals=[1,(1,3),dictDiff]
diffs=[]
for x in range(sldrCount.vals[1][1]):
	diffPos=(width/18,countBottom+(yMod*(x+1)))
	diffID='Comp '+str(x+1)+' Difficulty'
	sldrDiff=Slider(diffVals,diffPos,diffID) #computer difficulty slider
	sldrDiff.active=True if x<sldrCount.vals[0] else False
	diffs.append(sldrDiff)

#button creation
ng=TextButton((0,0),'New Game') #new game
cg=TextButton((0,0),'Continue Game') #continue game
cg.active=False #set as false to begin with; set as true if save file exists
btnWidth=int(ng.pos[2][0]+(width/50)+cg.pos[2][0])
ng.pos[0]=int((width-btnWidth)/2) #change ng x coord
cg.pos[0]=int(ng.pos[0]+(btnWidth-cg.pos[2][0])) #change cg x coord
ng.pos[1]=cg.pos[1]=int(countBottom+(yMod*(sldrCount.vals[1][1]+1.75))) #change y coord

#checkbox creation
newX=diffs[len(diffs)-1].pos[2]+(width/25)
newY=lblTitle.pos[1]+(lblTitle.font[2]/2)+(height/20)
lblRules=Label((newX,newY),white,'Gameplay Rules',mediumFont,False)
newY=lblRules.pos[1]+(lblRules.font[2]/2)+(height/20)
cbSlap=Checkbox((newX,newY),'Slaps?') #master checkbox
cbSlap.active=True
newX+=width/25
yMod=smallFont.render(cbSlap.caption,1,white).get_height()
rules=[]
for x in range(len(dictRules)):
	newY+=yMod
	cbRule=Checkbox((newX,newY),dictRules[x+1]) #individual rule checkbox
	cbRule.active=False
	rules.append(cbRule)
#End Lobby screen items

#Game Screen items
playPause=PlayPause((17*width/20,height/20),width/11) #play/pause button

def screenChange(screenNum):
	screen.fill(black)
	if screenNum==1: #game setting selection
		lblTitle.draw() #game title
		lblPlayer.draw() #player options label
		oldY=lblTitle.pos[1]+(lblTitle.font[2]/5)+(height/20)
		pygame.draw.line(screen,white,(width/18,oldY),(17*width/18,oldY),2)
		sldrCount.draw() #competitor count slider
		for diff in diffs:
			diff.draw() #competitor difficulty sliders
		newX=diffs[len(diffs)-1].pos[2]+(width/50)
		diffHeight=int((diffs[len(diffs)-1].pos[3]-diffs[len(diffs)-1].pos[0][1])*2)
		diffBottom=int(diffs[len(diffs)-1].pos[0][1])
		yMod=diffHeight+int(height/33)
		newY=diffBottom+yMod
		pygame.draw.line(screen,white,(newX,oldY),(newX,newY),2)
		lblRules.draw() #rules label
		cbSlap.draw()
		for rule in rules:
			rule.draw() #rules checkboxes
		ng.draw() #new game button
		cg.draw() #continue game button

	elif screenNum==2: #actual game
		#render order (comment placeholders)
		playPause.draw() #play/pause button
		#playerOrbit (invisible ellipse to guide player "hands")
		#for person in player:
			#cardBack.jpg
			#player name
			#number of cards
		#last played card (displayed larger than player hands, centered)
		#list of events
		placeholder=largeFont.render('Under Construction',1,orange)
		position=placeholder.get_rect(center=(width/2,height/2))
		screen.blit(placeholder,position)
	pygame.display.update()
	return scrName #update scrName for more accurate reference
#END GUI FUNCTIONS

#BEGIN GAMEPLAY FUNCTIONS
def rearrange(listInput, index):
	listInput.append(listInput[index])
	listInput.pop(index)

def playCard(playerIndex, handIndex):
	hand.append(player[playerIndex][2][0])
	history.append([])
	history[handIndex].append([player[playerIndex][0],[hand[len(hand)-1][0],hand[len(hand)-1][1]]])
	print('\n' + player[playerIndex][0] + ' played the ' + hand[len(hand)-1][0] + ' of ' + hand[len(hand)-1][1])
	player[playerIndex][2].pop(0)
	player[playerIndex][1]=len(player[playerIndex][2])

	if player[playerIndex][1]==0:
		removePlayer(playerIndex)

	if len(player)==1: #if there is only one player left
		print('\nCongratulations, ' + player[0][0] + '! You won the game!')
		print('Goodbye!')
		pprint.pprint(history)
		sys.exit()

def chooseNext():
	global person
	if person + 1 >= len(player):
		person=0
	else:
		person+=1

def removePlayer(playerIndex):
	print('\nSorry, ' + player[playerIndex][0] + ', you\'re out of cards! Goodbye!')
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

screen.fill(black)
scrName='Lobby'
screenChange(1)
clicked=scrolling=False

while 1: #begin game code
	(mouseX,mouseY)=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
			clicked=True
		if clicked:
			if scrName='Lobby': #all clickable objects on Lobby screen
				if sldrCount.pos[0][0]<mouseX<sldrCount.pos[2] \
				and sldrCount.pos[3]-15<mouseY<sldrCount.pos[3]+15:
					sldrCount.click() #update master slider
					for ind,diff in enumerate(diffs):
						diff.active=True if ind<sldrCount.vals[0] else False
						diff.draw() #activate indicated sliders, update all
				for diff in diffs:
					if diff.active \
					and diff.pos[0][0]<mouseX<diff.pos[2] \
					and diff.pos[3]-15<mouseY<diff.pos[3]+15:
						diff.click() #update individual sliders
				if cbSlap.pos[0]<mouseX<cbSlap.pos[0]+cbSlap.pos[2] \
				and cbSlap.pos[1]<mouseY<cbSlap.pos[1]+cbSlap.pos[3]:
					cbSlap.click() #update master checkbox
					for rule in rules:
						rule.active=True if cbSlap.val else False
						rule.draw() #update all checkboxes
				for rule in rules:
					if rule.active \
					and rule.pos[0]<mouseX<rule.pos[0]+rule.pos[2] \
					and rule.pos[1]<mouseY<rule.pos[1]+rule.pos[3]:
						rule.click() #update individual checkboxes
				if ng.pos[0]<mouseX<ng.pos[0]+ng.pos[2][0] \
				and ng.pos[1]<mouseY<ng.pos[1]+ng.pos[2][1]:
					ng.click()
				if cg.active \
				and cg.pos[0]<mouseX<cg.pos[0]+cg.pos[2][0] \
				and cg.pos[1]<mouseY<cg.pos[1]+cg.pos[2][1]:
					cg.click()
			elif scrName=='Game': #all clickable objects on Game screen
				if playPause.pos[0]<mouseX<playPause.pos[0]+playPause.size \
				and playPause.pos[1]<mouseY<playPause.pos[1]+playPause.size:
					print('update playPause')
					playPause.click()
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
		if human.isdigit()==False or int(human)<1 or int(human)>6: #if input has letters or is too small or large
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
		if computer.isdigit()==False or int(computer)<0 or int(computer)>6-human: #if input has letters or is too small or large
			printInvalid('Please enter a digit between 0 and ' + str(6-human) + '.')
		elif human + int(computer)==1: #if there is only one human player
			printInvalid('Please enter a digit between 1 and ' + str(6-human) + '.')
		else:
			computer=int(computer)
			if computer != 0: #choose computer player difficulty (slap likelihood, speed in seconds)
				for x in range(computer):
					level=str(input('\nChoose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
					if level.isdigit()==False or int(level)<1 or int(level)>3: #if input has letters or is too small or large
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
