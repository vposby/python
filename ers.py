"""
Desktop/Software/Python/Sandbox/Early_Work
Egyptian War!
version 1.0 - no slaps, straight card play
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
suits = ['Hearts','Diamonds','Clubs','Spades']
deck = [] #value, suit, player, position
for suit in suits:
	for value in range(13):
		if value == 0:
			deck.append(['Ace',suit,'',0])
		elif value == 10:
			deck.append(['Jack',suit,'',0])
		elif value == 11:
			deck.append(['Queen',suit,'',0])
		elif value == 12:
			deck.append(['King',suit,'',0])
		else:
			deck.append([str(value+1),suit,'',0])

#shuffle cards
for x in range(5):
	for x in range(len(deck)):
		move = random.randrange(0,len(deck))
		deck.append(deck[move])
		deck.pop(move)

print('Welcome to ERS! Up to six (6) players can participate.')

while invalid < 4:
	if invalid == 3:
		print("You have made too many invalid entries. The program will now close.")
		sys.exit()
	while players == 0:
		hChosen = cChosen = False
		#how many human players? (1-6)
		while hChosen == False:
			human = str(input('How many human players will there be? '))
			if human.isdigit() == False:
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 1 and 6.')
				invalid+=1
			elif int(human) < 1 or int(human) > 6:
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 1 and 6.')
				invalid+=1
			else:
				human = int(human)
				if human == 6:
					players = human + computer
					cChosen = True
				hChosen = True
				
		invalid = 0
		#how many computer players? (0-5)
		while cChosen == False:
			computer = str(input('How many computer players will there be? '))
			cLevel = 0
			if computer.isdigit() == False:
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 0 and ' + str(6-human) + '.')
				invalid+=1
			elif int(computer) < 0 or int(computer) > 6-human:
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 0 and ' + str(6-human) + '.')
				invalid+=1
			elif human + int(computer) == 1:
				print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
				print('Please enter a digit between 1 and ' + str(6-human) + '.')
				invalid+=1
			else:
				players = human + int(computer)
				computer = int(computer)

				#choose computer player difficulty (slap speed in seconds)
				if computer != 0:
					cLevel = str(input('Choose computer player difficulty (1=Easy, 2=Medium, 3=Hard): '))
					if cLevel.isdigit() == False:
						print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
						print('Please enter a digit between 1 and 3.')
						invalid+=1
					elif int(cLevel) < 1 or int(cLevel) > 3:
						print('Invalid entry! You have ' + str(3-invalid) + ' attempt(s) before the program closes.')
						print('Please enter a digit between 1 and 3.')
						invalid+=1
					else:
						cLevel = [int(cLevel),''] #do this for each computer player later
						if cLevel[0] == 1:
							cLevel[1] = 'Easy' #2 seconds
						elif cLevel[0] == 2:
							cLevel[1] = 'Medium' #1.5 seconds
						else:
							cLevel[1] = 'Hard' #1 second
				cChosen = True
	
	print('Human Players: ' + str(human))
	if computer != 0:
		print('Computer Players: ' + str(computer) + ' (Difficulty: ' + cLevel[1] + ')')
	print('Total Players: ' + str(players))

	player = []

	for x in range(players):
		if x < human:
			player.append([str(input('Player ' + str(x+1) + ', what is your name? ')),x,0])
		else:
			player.append(['Computer ' + str(x-human+1),x,0])

	#deal cards evenly between players
	order = 1
	dealt = 1
	person = 0

	for card in deck:
		card[2] = player[person][0]
		card[3] = order
		player[person][2]+=1
		dealt+=1
		if person+1 < len(player):
			person+=1
		else:
			person = 0
			order+=1
	
	#randomize starting player
	starter = random.randrange(0,len(player))
	print(player[starter][0] + ' will start!')
	print(player)

	#rearrange player order
	for x in range(starter):
		player.append(player[0])
		player.pop(0)
		player[len(player)-1][1] = x

	#begin play
	gameOver = False
	handOver = False

	while gameOver == False:
		order = 1
		while handOver == False:
			play = 1
			for x in range(len(player)):
				for card in deck:
					if card[2] == player[x][0] and card[3] == order:
						card[2] = 'in play'
						card[3] = play
						play+=1
						if card[0] == 'Jack':
							if x+1>len(player):

							else:

						elif card[0] == 'Queen':
							if x+1>len(player):
							else:

						elif card[0] == 'King':
							if x+1>len(player):
							else:

						elif card[0] == 'Ace':
							if x+1>len(player):
							else:

						else:

	#if number, go to next player
	#if face card, next player puts down required cards
	#if required cards max number reached, face card player collects
	#if one player has all 52 cards, game ends
	#player x wins message
print('Goodbye!')
sys.exit()

