"""
Desktop/Software/Python/Sandbox/Card_Games
Egyptian War!
version 1.0 - no slaps, straight card play
"""

import sys
import random
import pprint

def rearrange(listInput,index):
	listInput.append(listInput[index])
	listInput.pop(index)

def printInvalid(message):
	global invalid
	invalid+=1
	if invalid < 4:
		print('Invalid entry! You have ' + str(4-invalid) + ' attempt(s) before the program closes.')
		print(message)
	
def checkInvalid():
	global invalid
	if invalid == 4:
		print("You have made too many invalid entries. The program will now close.")
		sys.exit()

def playCard(playerIndex):
	hand.append(player[playerIndex][2][0])
	print('\n' + player[playerIndex][0] + ' played the ' + hand[len(hand)-1][0] + ' of ' + hand[len(hand)-1][1])
	player[playerIndex][2].pop(0)

def chooseNext():
	global person
	if person+1>=len(player):
		person = 0
	else:
		person+=1

def removePlayer(playerIndex):
	print('\n' + 'Sorry, ' + player[playerIndex][0] + ', you\'re out of cards! Goodbye!')
	player.pop(playerIndex)

values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['Hearts','Diamonds','Clubs','Spades']
deck = []
for suit in suits: #create cards
	for value in values:
		deck.append([value,suit])

for x in range(random.randrange(5,11)): #shuffle cards
	for y in range(len(deck)):
		rearrange(deck,random.randrange(0,len(deck)))

print('Welcome to ERS! Up to six (6) players can participate.')

while 1: #begin game code
	human = 0
	computer = 0
	players = human + computer 
	hChosen = cChosen = False #numbers of players
	invalid = 0 #count number of invalid entries
	while hChosen == False: #how many human players? (1-6)
		checkInvalid()
		human = str(input('\n' + 'How many human players will there be? '))
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
		computer = str(input('\n' + 'How many computer players will there be? '))
		cLevel = []
		if computer.isdigit() == False or int(computer) < 0 or int(computer) > 6-human: #if input has letters or is too small or large
			printInvalid('Please enter a digit between 0 and ' + str(6-human) + '.')
		elif human + int(computer) == 1: #if there is only one human player
			printInvalid('Please enter a digit between 1 and ' + str(6-human) + '.')
		else:
			computer = int(computer)
			if computer != 0: #choose computer player difficulty (slap likelihood, speed in seconds)
				for x in range(computer):
					level = str(input('\n' + 'Choose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
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
			playerName = str(input('\n' + 'Player ' + str(namedPlayers+1) + ', what is your name? '))
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
	hand = []
	person = 0

	while gameOver == False: #begin play
		print('\n Press Enter to start the next hand.') #player must approve the start of each hand
		if input('Any other entries will end the program. ') != '':
			print('Goodbye!')
			sys.exit()
		else:
			if len(player) == 1: #if there is only one player left
				print('\n Congratulations, ' + player[0] + '! You won the game!')
				print('Goodbye!')
				sys.exit()

			handOver = False
			playCard(person)
			chooseNext()
			
			while handOver == False:
				if player[person][1] == 0: #if a player runs out of cards
					removePlayer(person)
					chooseNext()
				#if the played card requires a slap
				elif hand[len(hand)-1][0] not in ['Jack','Queen','King','Ace']: #if a number is played
					playCard(person)
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
						if player[person][1] == 0: #if a player runs out of cards
							removePlayer(person)
							if person == len(player): #if last player exits game, first player is next
								person = 0
						else:
							playCard(person)
							if hand[len(hand)-1][0] not in ['Jack','Queen','King','Ace']: #if a number is played
								if played == play-1: #if the required number of face cards is reached
									if person-1<0:
										person = len(player)-1
									else:
										person-=1
									print('\n' + player[person][0] + ' wins ' + str(len(hand)) + ' cards this hand!')
									for card in hand: #add all cards to winner's hand
										player[person][2].append(card)
									hand = []
									handOver = True
							else: #if a face card is played
								chooseNext()
								break
							played+=1
				for p in player: #maintain accurate count of cards
					p[1] = len(p[2])
				for p in player: #list players, player card counts
					print(p[0] + ' has ' + str(p[1]) + ' cards.')