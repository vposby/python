"""
Desktop/Software/Python/Sandbox/Card_Games
Egyptian War!
version 1.0 - no slaps, straight card play
work on card play code
"""

import sys
import random
import pprint

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
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 1 and 6.')
				invalid+=1
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
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 0 and ' + str(6-human) + '.')
				invalid+=1
			elif human + int(computer) == 1: #if there is only one human player
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 1 and ' + str(6-human) + '.')
				invalid+=1
			else:
				computer = int(computer)
				if computer != 0: #choose computer player difficulty (slap speed in seconds)
					for x in range(computer):
						level = str(input('\n' + 'Choose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
						if level.isdigit() == False or int(level) < 1 or int(level) > 3: #if input has letters or is too small or large
							print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
							print('Please enter a digit between 1 and 3.')
							invalid+=1
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
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter your name.')
				invalid+=1
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

	x = 0

	for card in deck: #deal cards evenly between players
		player[x][2].append(card)
		player[x][1]+=1
		if x+1 < len(player):
			x+=1
		else:
			x = 0

	for y in player: #list players, number of cards in players' hands
		print('\n' + y[0] + ' has ' + str(y[1]) + ' cards.')
	
	gameOver = False
	
	while gameOver == False: #begin play
		
		for y in player:
			y[1] = len(y[2])
			if y[1] == 52: #if one player has all 52 cards, the game ends
				print('\n' + 'Congratulations, ' + y[0] + '! You won the game!')
				print('Goodbye!')
				gameOver = True

		#player must approve the start of each hand
		print('\n' + 'Press Enter to start the next hand.')
		if input('Any other entries will end the program. ') != '':
			print('Goodbye!')
			sys.exit()
		else:
			pprint.pprint(player) #verify each hand is played accurately
			handOver = False
			person = order = 0
			hand = [player[person][2][0]] #first card played
			print('\n' + player[person][0] + ' played the ' + hand[order][0] + ' of ' + hand[order][1])
			player[person][2].pop(0)
			person = order = 1

			while handOver == False:
				if hand[order-1][0] not in ['Jack','Queen','King','Ace']:
					hand.append(player[person][2][0])
					player[person][2].pop(0)
					print('\n' + player[person][0] + ' played the ' + hand[order][0] + ' of ' + hand[order][1])				
					order+=1
					if person+1==len(player):
						person = 0
					else:
						person = person+1
				else: #if a face card is played
					play = 0
					for y in ['Jack','Queen','King','Ace']: #how many cards the next player must play
						play+=1 #J=1, Q=2, K=3, A=4
						if y == hand[order-1][0]:
							break
					print(player[person][0] + ' must play ' + str(play) + ' card(s).')
					for y in range(play):
						if player[person][2][0] == '':
							print(player[person][0] + ', you are out of cards! Goodbye!')
							player.pop(person)
						else:
							hand.append(player[person][2][0])
							player[person][2].pop(0)
							print('\n' + player[person][0] + ' played the ' + hand[order][0] + ' of ' + hand[order][1])
							order+=1
							if hand[order-1][0] not in ['Jack','Queen','King','Ace']: #if the card played is a number
								if y == play-1: #if the last card played is a number
									if person-1<0:
										winner = len(player)-1
									else:
										winner = person-1
									print('\n' + player[winner][0] + ' wins ' + str(len(hand)) + ' cards this hand!')
									for card in hand:
										player[winner][2].append(card)
									handOver = True
							else: #if a face card or the maximum number of numbers is played
								hand.append(player[person][2][0])
								player[person][2].pop(0)
								print('\n' + player[person][0] + ' played the ' + hand[order][0] + ' of ' + hand[order][1])
								order+=1								
								break