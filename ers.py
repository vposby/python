"""
Egyptian War!
version 1.0 - no slaps, straight card play
work on card play code
"""

import pprint
import sys
import random

#count number of invalid entries
invalid = 0

#numbers of players
human = 0
computer = 0
players = human + computer

#create cards
values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['Hearts','Diamonds','Clubs','Spades']
deck = []
for suit in suits:
	for value in values:
		deck.append([value,suit])

#shuffle cards
for x in range(5): 
	for x in range(len(deck)):
		move = random.randrange(0,len(deck))
		deck.append(deck[move])
		deck.pop(move)

print('Welcome to ERS! Up to six (6) players can participate.')

#begin game code
while invalid < 4:
	if invalid == 3:
		print("You have made too many invalid entries. The program will now close.")
		sys.exit()

	#choose players
	while players == 0:
		hChosen = cChosen = False
		while hChosen == False: #how many human players? (1-6)
			human = str(input('How many human players will there be? '))
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
			computer = str(input('How many computer players will there be? '))
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
						level = str(input('Choose Computer ' + str(x+1) + ' difficulty (1=Easy, 2=Medium, 3=Hard): '))
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

	player = []

	for x in range(players):
		if x < human:
			invalid = 0
			playerName = str(input('Player ' + str(x+1) + ', what is your name? '))
			if playerName == '':
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 1 and 3.')
				invalid+=1
			else:
				player.append([playerName,x,0,[]])
		else:
			player.append(['Computer ' + str(x-human+1) + ' (' + cLevel[x-human][1] + ')',x,0,[]])
	
	#randomize starting player
	starter = random.randrange(0,len(player))
	print(player[starter][0] + ' will start!')

	#rearrange player order
	for x in range(starter):
		player.append(player[0])
		player.pop(0)
		player[len(player)-1][1] = x

	#deal cards evenly between players
	order = 1
	dealt = 1
	person = 0

	for card in deck:
		player[person][3].append(card)
		player[person][2]+=1
		dealt+=1
		if person+1 < len(player):
			person+=1
		else:
			person = 0
			order+=1

	#begin play
	gameOver = False
	handOver = False
	
	while gameOver == False:
		order = 0
		hand = []
		pprint.PrettyPrinter().pprint(player)

		#if one player has all 52 cards, the game ends
		for x in range(len(player)):
			if len(player[x][3]) == 52:
				print('Congratulations, ' + player[x][0] + '! You won the game!')
				print('Goodbye!')
				sys.exit()
			elif len(player[x][3]) == 0:
				print(player[x][0] + ', you are out of cards! Goodbye!')
				player.pop(x)

		#player must approve the start of each hand
		print('Press Enter to play the next hand.')
		if input('Any other entries will end the program. ') != '':
			print('Goodbye!')
			sys.exit()
		else:
			while handOver == False:
				for x in range(len(player)):
					print('Press Enter to play the next card.')
					if input('Any other entries will end the program. ') != '':
						print('Goodbye!')
						sys.exit()
					else:
						if x+1>len(player):
							nextPerson = 0
						else:
							nextPerson = x+1

						if player[x][3][0][0] in ['Jack','Queen','King','Ace']: #next player places one card
							hand.append(player[x][3][0])
							player[x][3].pop(0)
							play = 0
							for y in ['Jack','Queen','King','Ace']:
								play+=1 #J=1, Q=2, K=3, A=4
								if y == player[x][3][0][0]:
									break
							for y in range(play):
								if player[nextPerson][3][0] == '':
									print(player[x][0] + ', you are out of cards! Goodbye!')
									player.pop(x)
								else:
									hand.append(player[nextPerson][3][0])
									player[nextPerson][3].pop(0)
									if player[nextPerson][3][0][0] not in ['Jack','Queen','King','Ace'] and y == play:
										print(player[x][0] + ' wins ' + str(len(hand)) + ' cards this hand!')
										for card in hand:
											player[x][3].append(card)
										handOver = True
									else:
										hand.append(player[nextPerson][3][0])
										player[nextPerson][3].pop(0)
						else: #play continues as usual
							hand.append(player[x][3][0])
							player[x][3].pop(0)
						pprint.PrettyPrinter().pprint(hand)