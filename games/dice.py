"""
	This program is meant to simulate dice rolls.
	The user chooses one of seven types of dice:
	d4, d6, d8, d10, d12, d20, or d100.
	The program then outputs the resulting number(s).
"""

from random import *
import pprint, sys

rollResults = []
attempted = invalid = 0
result = rules = dice = ''
dieType = [4,6,8,10,12,20,100]
for die in dieType:
	if die != dieType[len(dieType)-1]:
		dice = dice + str(die) + '-, '
	else:
		dice = dice + 'or ' + str(die) + '-'
rules = 'You can roll a ' + dice + 'sided die.'

def invalidResponse():
	global invalid
	invalid += 1
	remaining = ''
	if invalid < 3:
		remaining = str(3-invalid) + ' more invalid attempt(s).'
	else:
		remaining = 'the next invalid attempt.'
	print('\nInvalid entry! Please enter a valid number of sides as an integer. ' + rules)
	print('\nThe program will close after ' + remaining)

print('\nWelcome! '+ rules + ' Type q to quit at any time.')
while invalid < 4: #begin roll code
	print('\nWhat type of die would you like to roll?')
	dieChoice = input('(Input the number of sides on the die.) ')
	if dieChoice == 'q' or dieChoice == 'Q':
		if len(rollResults)>0: #print result summary
			print('\nBelow is a summary of your results:')
			pprint.pprint(rollResults)
		sys.exit() #exit program
	elif dieChoice.isdigit() == False:
		invalidResponse()
	elif int(dieChoice) not in dieType:
		invalidResponse()
	else:
		attempted+=1
		result = str(randint(1,int(dieChoice)))
		rollResults.append('Roll ' + str(attempted) + ' (D' + dieChoice + '): ' + result) #notify user of roll result
		print('\nYou rolled a(n) ' + result + '.') #end roll code
print('\nYou have made too many invalid entries. The program will now close.')
sys.exit()
