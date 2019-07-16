"""
Egyptian War!
v 2.0 - straight card play, single player, pygame gui
!!!add rules checkboxes
"""

import sys, random, pprint, pygame
pygame.init()

size = width, height = (512, 338)
black = (0, 0, 0)
white = (255, 255, 255)
lgrey = (196,196,196)
dgrey = (128, 128, 128)
red = (224, 0, 0)
orange = (255, 128, 0)
yellow = (224, 224, 0)
green = (0, 224, 0)
cyan = (0, 255, 255)
blue = (0, 0, 224)
purple = (128, 0, 128)
pink = (224, 0, 224)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Egyptian War')
largeFont = pygame.font.Font(None, 60)
mediumFont = pygame.font.Font(None, 40)
smallFont = pygame.font.Font(None, 20)

#BEGIN GUI FUNCTIONS, CLASSES
class Slider:
	global screen, width, height, mouseX, mouseY
	def __init__(self,vals=[1,(1,2),{1:1,2:2}],pos=(0,0),id="Default",active=True):
		self.vals = vals #output value as int,range of values as (min=int,max=int),list of outputs as dict
		(min,max)=(self.vals[1][0],self.vals[1][1])
		self.id = id + ": " + str(self.vals[2].get(self.vals[0])) #slider default caption
		self.active = active #as boolean; allow/disallow user interactivity
		if active == True:
			color = white
		else:
			color = dgrey
		caption = smallFont.render(self.id,1,color)
		(x,y) = (int(pos[0]),int(pos[1]))
		leftEnd = int(x+caption.get_width()+(width/50))
		rightEnd = int(leftEnd+(width/6))
		sldrHt = int(y+(caption.get_height()/2))
		self.pos = [pos,leftEnd,rightEnd,sldrHt,[]] #positional values
		for x in range(max-min+1):
			widthMod = int(x*(rightEnd-leftEnd)/(max-1))
			if x+1 != vals[0]: #values (min to max)
				self.pos[4].append([lgrey,(leftEnd+widthMod,sldrHt),3])
			else:
				self.pos[4].append([green,(leftEnd+widthMod,sldrHt),4])

	def draw(self):
		if self.active == True:
			color = white
		else:
			color = dgrey
		caption = smallFont.render(self.id,1,color) #use this to determine slider height
		(x,y) = (self.pos[0][0],self.pos[0][1])
		(w,h) = (self.pos[2]-self.pos[0][0]+int(width/50),caption.get_height())
		pygame.draw.rect(screen,black,(x,y,w,h)) #set blank rect for slider
		screen.blit(caption,self.pos[0]) #caption
		#slider line, values (min to max) below
		pygame.draw.line(screen,color,(self.pos[1],self.pos[3]),(self.pos[2],self.pos[3]),3)
		for x in range(len(self.pos[4])):
			pygame.draw.circle(screen,self.pos[4][x][0],self.pos[4][x][1],self.pos[4][x][2])
		pygame.display.update((x,y,w,h)) #(re)draw slider

	def click(self):
		area = int(self.pos[4][1][1][0]-self.pos[1])/2
		for x in range(len(self.pos[4])):
			(self.pos[4][x][0],self.pos[4][x][2])=(lgrey,3) #reset circle to lgrey
			#print(self.pos[0])
			if mouseX>self.pos[1] and mouseX<self.pos[1]+area: #minimum
					self.vals[0] = self.vals[1][0]
			elif mouseX>self.pos[2]-area and mouseX<self.pos[2]:
					self.vals[0] = self.vals[1][1]
			elif mouseX>self.pos[4][x][1][0]-area and mouseX<self.pos[4][x][1][0]+area:
					self.vals[0] = x+1
		val = self.vals[0]
		#print(val,mouseX,mouseY)
		(self.pos[4][val-1][0],self.pos[4][val-1][2])=(green,4) #value circle: green
		self.id = self.id.split(":")[0]+": "+str(self.vals[2].get(val)) #set new slider caption
		self.draw()

dictCount = {
	1: 1,
	2: 2,
	3: 3,
	4: 4,
	5: 5,
}

dictDiff = {
	1: "Easy",
	2: "Medium",
	3: "Hard"
}

countVals = [1,(1,5),dictCount]
countPos = (width/18,29*height/100)
countID = "Competitors"
sldrCount = Slider(countVals,countPos,countID,True) #lobby screen
countHeight = (sldrCount.pos[3]-sldrCount.pos[0][1])*2
countBottom = sldrCount.pos[0][1]
hMod = countHeight+height/25
diffVals = [1,(1,3),dictDiff]
diffs = []
for x in range(sldrCount.vals[1][1]):
	diffPos = (width/12,countBottom+(hMod*(x+1)))
	diffID = "Comp "+str(x+1)+" Difficulty"
	if x < sldrCount.vals[0]:
		diffActive = True
	else:
		diffActive = False
	sldrDiff = Slider(diffVals,diffPos,diffID,diffActive) #lobby screen
	diffs.append(sldrDiff)

class Label:
	global screen, width, height
	def __init__(self,x,y,color,caption,font,centered=False):
		self.x = x #as integer
		self.y = y #as integer
		self.color = color #as (r,g,b)
		self.caption = caption #as string
		self.font = font #as font
		self.centered = centered #as boolean

	def draw(self):
		text = self.font.render(self.caption,1,self.color)
		if self.centered==False:
			pos = (self.x,self.y)
		else:
			pos = text.get_rect(center=(self.x,self.y))
		screen.blit(text,pos)

lblTitle = Label(width/2,height/12,white,"Egyptian War",largeFont,True) #lobby screen
lblPlayer = Label(width/4,23*height/100,white,"Player Options",mediumFont,True) #lobby screen

def screenChange(screenName):
	screen.fill(black)
	if screenName == 'Lobby': #game setting selection
		#render order (comment placeholders)
		lblTitle.draw() #game title
		pygame.draw.line(screen,white,(width/18,height/6),(17*width/18,height/6),2)
		pygame.draw.line(screen,white,(3*width/5,height/6),(3*width/5,19*height/20),2)
		lblPlayer.draw() #player options label
		sldrCount.draw() #competitor count slider
		for diff in diffs:
			diff.draw()
		#competitor difficulty sliders
		#rules label
		#slaps checkbox
		#rules checkboxes
		#new game button
		#continue game button
		#placeholder = largeFont.render("Under Construction",1,orange)
		#position = placeholder.get_rect(center=(width/2,height/2))
		#screen.blit(placeholder,position)

	elif screenName=='Game': #actual game
		#render order (comment placeholders)
		#play/pause button
		#playerOrbit (invisible ellipse to guide player "hands")
		#for person in player:
			#cardBack.jpg
			#player name
			#number of cards
		#last played card (displayed larger than player hands, centered)
		#list of events
		placeholder = largeFont.render("Under Construction",1,orange)
		position = placeholder.get_rect(center=(width/2,height/2))
		screen.blit(placeholder,position)
	pygame.display.update()

#END GUI FUNCTIONS

#BEGIN GAMEPLAY FUNCTIONS
def rearrange(listInput, index):
	listInput.append(listInput[index])
	listInput.pop(index)

def printInvalid(message):
	global invalid
	invalid += 1
	if invalid < 4:
		print('Invalid entry! You have ' + str(4-invalid) + ' attempt(s) before the program closes.')
		print(message)

def checkInvalid():
	global invalid
	if invalid == 4:
		print('You have made too many invalid entries. The program will now close.')
		sys.exit()

def playCard(playerIndex, handIndex):
	hand.append(player[playerIndex][2][0])
	history.append([])
	history[handIndex].append([player[playerIndex][0],[hand[len(hand)-1][0],hand[len(hand)-1][1]]])
	print('\n' + player[playerIndex][0] + ' played the ' + hand[len(hand)-1][0] + ' of ' + hand[len(hand)-1][1])
	player[playerIndex][2].pop(0)
	player[playerIndex][1] = len(player[playerIndex][2])

	if player[playerIndex][1] == 0:
		removePlayer(playerIndex)

	if len(player) == 1: #if there is only one player left
		print('\nCongratulations, ' + player[0][0] + '! You won the game!')
		print('Goodbye!')
		pprint.pprint(history)
		sys.exit()

def chooseNext():
	global person
	if person + 1 >= len(player):
		person = 0
	else:
		person+=1

def removePlayer(playerIndex):
	print('\nSorry, ' + player[playerIndex][0] + ', you\'re out of cards! Goodbye!')
	player.pop(playerIndex)
#END GAMEPLAY FUNCTIONS

values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['Hearts','Diamonds','Clubs','Spades']
deck = []
for suit in suits: #create deck
	for value in values:
		deck.append([value, suit])

for x in range(random.randrange(5, 11)): #shuffle cards
	for y in range(len(deck)):
		rearrange(deck,random.randrange(0, len(deck)))

screen.fill(black)
scrName = 'Lobby'
screenChange(scrName)

while 1: #begin game code
	(mouseX,mouseY) = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			if scrName == 'Lobby': #all clickable objects in Lobby
				if mouseY>sldrCount.pos[0][1] \
				and mouseY<sldrCount.pos[0][1]+sldrCount.pos[3] \
				and mouseX>sldrCount.pos[0][0] \
				and mouseX<sldrCount.pos[2]: #no else
					sldrCount.click()
					for ind,diff in enumerate(diffs):
						if ind < sldrCount.vals[0]:
							diff.active = True
						else:
							diff.active = False
						diff.draw()

	#PRESERVE GAMEPLAY CODE BELOW
	"""
	human = 0
	computer = 0
	players = human + computer

	hChosen = cChosen = False #numbers of players
	invalid = 0 #count number of invalid entries
	while hChosen == False: #how many human players? (1-6)
		checkInvalid()
		human = str(input('\nHow many human players will there be? '))
		if human.isdigit() == False or int(human) < 1 or int(human) > 6: #if input has letters or is too small or large
			printInvalid('Please enter a digit between 1 and 6.')
		else:
			human = int(human)
			if human == 6: #skip computer player code
				players = human + computer
				cChosen = True
			hChosen = True

	invalid = 0	#reset invalid counter
	while cChosen == False: #how many computer players? (0-5)
		checkInvalid()
		computer = str(input('\nHow many computer players will there be? '))
		cLevel = []
		if computer.isdigit() == False or int(computer) < 0 or int(computer) > 6-human: #if input has letters or is too small or large
			printInvalid('Please enter a digit between 0 and ' + str(6-human) + '.')
		elif human + int(computer) == 1: #if there is only one human player
			printInvalid('Please enter a digit between 1 and ' + str(6-human) + '.')
		else:
			computer = int(computer)
			if computer != 0: #choose computer player difficulty (slap likelihood, speed in seconds)
				for x in range(computer):
					level = str(input('\nChoose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
					if level.isdigit() == False or int(level) < 1 or int(level) > 3: #if input has letters or is too small or large
						printInvalid('Please enter a digit between 1 and 3.')
					else:
						if int(level) == 1: #1.5 to 2 seconds, 66% chance to slap
							cLevel.append(['Computer ' + str(x+1),'Easy'])
						elif int(level) == 2: #1 to 1.5 seconds, 75% chance to slap
							cLevel.append(['Computer ' + str(x+1),'Medium'])
						else: #0.5 to 1 seconds, 100% chance to slap
							cLevel.append(['Computer ' + str(x+1),'Hard'])
			players = human + computer
			cChosen = True

	player = [] #player name, number of cards, cards in hand as list
	namedPlayers = 0
	while namedPlayers < players:
		checkInvalid()
		if namedPlayers < human:
			invalid = 0
			playerName = str(input('\nPlayer ' + str(namedPlayers+1) + ', what is your name? '))
			if playerName == '':
				printInvalid('Please enter your name.')
			else:
				player.append([playerName,0,[]])
				namedPlayers+=1
		else:
			player.append([cLevel[namedPlayers-human][0] + ' (' + cLevel[namedPlayers-human][1] + ')',0,[]])
			namedPlayers+=1

	starter = random.randrange(0,len(player)) #randomize starting player
	print('\n' + player[starter][0] + ' will start!')

	for x in range(starter): #rearrange player order
		rearrange(player,0)

	person = 0
	for card in deck: #deal cards evenly between players
		player[person][2].append(card)
		player[person][1]+=1
		chooseNext()

	for p in player: #list players, number of cards in players' hands
		print(p[0] + ' has ' + str(p[1]) + ' cards.')

	gameOver = False
	person = 0
	handNum = 0
	hand = []
	history = []

	while gameOver == False: #begin play
		print('\nPress Enter to start the next hand.') #player must approve the start of each hand
		if input('Any other entries will end the program. ') != '':
			print('Goodbye!')
			sys.exit()
		else:
			handOver = False
			playCard(person, handNum)
			chooseNext()

			while handOver == False:
				#if the played card requires a slap
				if hand[len(hand)-1][0] not in ['Jack','Queen','King','Ace']: #if a number is played
					playCard(person, handNum)
					chooseNext()
				else: #if a face card is played
					play = 0
					played = 0
					for x in ['Jack','Queen','King','Ace']: #how many cards the next player must play
						play+=1 #J=1, Q=2, K=3, A=4
						if x == hand[len(hand)-1][0]:
							break
					print(player[person][0] + ' must play ' + str(play) + ' card(s).')

					while played < play: #play the required number of cards
						playCard(person, handNum)
						if hand[len(hand)-1][0] in ['Jack','Queen','King','Ace']: #if a face card is played
							chooseNext()
							break
						else: #if a number is played
							if played == play-1: #if the required number of face cards is reached
								if person-1<0:
									person = len(player)-1
								else:
									person-=1
								print('\n' + player[person][0] + ' wins ' + str(len(hand)) + ' cards this hand!\n')
								for card in hand: #add all cards to winner's hand
									player[person][2].append(card)
								hand = []
								handNum+=1
								for p in player:
									p[1] = len(p[2])
									print(p[0] + ' has ' + str(p[1]) + ' cards.')
								handOver = True
						played+=1
	"""
