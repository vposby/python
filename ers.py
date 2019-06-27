"""
Egyptian War!
version 1.0 - no slaps, straight card play
"""

import sys
import random

invalid = 0 #count number of invalid entries

human = 0
computer = 0
players = human + computer #numbers of players

values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['Hearts','Diamonds','Clubs','Spades']
deck = []
for suit in suits: #create cards
	for value in values:
		deck.append([value,suit])

for x in range(5): #shuffle cards
	for x in range(len(deck)):
		move = random.randrange(0,len(deck))
		deck.append(deck[move])
		deck.pop(move)

def playCard(playerIndex):
	hand.append(player[playerIndex][2][0])
	print('\n' + player[playerIndex][0] + ' played the ' + hand[len(hand)-1][0] + ' of ' + hand[len(hand)-1][1])
	player[playerIndex][2].pop(0)
	order+=1

def removePlayer(playerIndex):
	print('\n' + 'Sorry, ' + player[playerIndex][0] + ', you\'re out of cards! Goodbye!')
	player.pop(playerIndex)

def chooseNext(playerIndex):
	if playerIndex+1>=len(player):
		playerIndex = 0
	else:
		playerIndex+=1

def printInvalid(errorCount):
	print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
	invalid+=1

print('Welcome to ERS! Up to six (6) players can participate.')

while 1: #begin game code
	if invalid == 3:
		print("You have made too many invalid entries. The program will now close.")
		sys.exit()

	while players == 0: #choose players
		hChosen = cChosen = False
		while hChosen == False: #how many human players? (1-6)
			human = str(input('\n' + 'How many human players will there be? '))
			if human.isdigit() == False or int(human) < 1 or int(human) > 6: #if input has letters or is too small or large
				printInvalid(invalid)
				print('Please enter a digit between 1 and 6.')
			else:
				human = int(human)
				if human == 6: #skip computer player code
					players = human + computer
					cChosen = True
				hChosen = True
				
		invalid = 0
		while cChosen == False: #how many computer players? (0-5)
			computer = str(input('\n' + 'How many computer players will there be? '))
			cLevel = []
			if computer.isdigit() == False or int(computer) < 0 or int(computer) > 6-human: #if input has letters or is too small or large
				printInvalid(invalid)
				print('Please enter a digit between 0 and ' + str(6-human) + '.')
			elif human + int(computer) == 1: #if there is only one human player
				printInvalid(invalid)
				print('Please enter a digit between 1 and ' + str(6-human) + '.')
			else:
				computer = int(computer)
				if computer != 0: #choose computer player difficulty (slap speed in seconds)
					for x in range(computer):
						level = str(input('\n' + 'Choose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
						if level.isdigit() == False or int(level) < 1 or int(level) > 3: #if input has letters or is too small or large
							printInvalid(invalid)
							print('Please enter a digit between 1 and 3.')
						else:
							if int(level) == 1:
								cLevel.append(['Computer ' + str(x+1),'Easy']) #2 seconds
							elif int(level) == 2:
								cLevel.append(['Computer ' + str(x+1),'Medium']) #1.5 seconds
							else:
								cLevel.append(['Computer ' + str(x+1),'Hard']) #1 second
				players = human + computer
				cChosen = True

	player = [] #player name, number of cards, cards in hand as list
	namedPlayers = 0
	while namedPlayers < players:
		if namedPlayers < human:
			invalid = 0
			playerName = str(input('\n' + 'Player ' + str(namedPlayers+1) + ', what is your name? '))
			if playerName == '':
				printInvalid(invalid)
				print('Please enter your name.')
			else:
				player.append([playerName,0,[]])
				namedPlayers+=1
		else:
			player.append([cLevel[namedPlayers-human][0] + ' (' + cLevel[namedPlayers-human][1] + ')',0,[]])
			namedPlayers+=1
	
	starter = random.randrange(0,len(player)) #randomize starting player
	print('\n' + player[starter][0] + ' will start!')

	for x in range(starter): #rearrange player order
		player.append(player[0])
		player.pop(0)

	person = 0

	for card in deck: #deal cards evenly between players
		player[person][2].append(card)
		player[person][1]+=1
		chooseNext(person)

	for person in player: #list players, number of cards in players' hands
		print('\n' + person[0] + ' has ' + str(person[1]) + ' cards.')
	
	gameOver = False
	winner = ''
	hand = []
	
	while gameOver == False: #begin play
		print('\n' + 'Press Enter to start the next hand.') #player must approve the start of each hand
		if input('Any other entries will end the program. ') != '':
			print('Goodbye!')
			sys.exit()
		else:
			if len(player) == 1: #if there is only one player left
				print('\n' + 'Congratulations, ' + player[0] + '! You won the game!')
				print('Goodbye!')
				sys.exit()

			handOver = False
			order = 0

			if winner == '': #decide who starts the hand
				person = 0
			else:
				if winning>=len(player):
					person = len(player)-1
				else:
					person = winning

			playCard(person)
			chooseNext(person)
			
			while handOver == False:
				if len(player[person][2]) == 0: #if a player runs out of cards
					removePlayer(person)
					chooseNext(person)
				elif hand[order-1][0] not in ['Jack','Queen','King','Ace']:
					playCard(person)
					chooseNext(person)
				else: #if a face card is played
					play = 0
					played = 0
					for x in ['Jack','Queen','King','Ace']: #how many cards the next player must play
						play+=1 #J=1, Q=2, K=3, A=4
						if x == hand[order-1][0]:
							break
					print(player[person][0] + ' must play ' + str(play) + ' card(s).')
					
					while played < play: #play the required number of cards
						if len(player[person][2]) == 0: #if a player runs out of cards
							removePlayer(person)
							if person == len(player): #if last player exits game, first player is next
								person = 0
						else:
							playCard(person)
							if hand[order-1][0] not in ['Jack','Queen','King','Ace']: #if the card played is a number
								if played == play-1:
									if person-1<0:
										winning = len(player)-1
									else:
										winning = person-1
									winner = player[winning][0]
									print('\n' + winner + ' wins ' + str(len(hand)) + ' cards this hand!')
									for card in hand:
										player[winning][2].append(card)
									hand = []
									handOver = True
							else: #if a face card or the maximum number of numbers is played
								chooseNext(person)
								break
							played+=1
				for person in player: #maintain accurate count of cards
					person[1] = len(person[2])