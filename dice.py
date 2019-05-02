"""
	This program is meant to simulate dice rolls.
	The user chooses one of seven types of dice:
	d4, d6, d8, d10, d12, d20, or d100.
	The program then outputs the resulting number(s).
"""

from random import *
import pprint
import sys

#counter of invalid entries
invalid = 0
#record of roll results: output at end of dialog
rollResults = []
#default number of times user will roll
attempts = 1
#counter of user rolls
attempted = 0
#default value of result
result = "Invalid entry!"


print("Welcome! You can roll up to 6 times.")
while invalid < 4:
	#exit program after too many invalid entries
	if invalid == 3:
		print("You have made too many invalid entries. The program will now close.")
		sys.exit()
	#user chooses between 1 and 6 attempts (inclusive)
	attempts = str(input('How many times would you like to roll? '))
	if attempts.isdigit() == True:
		attempts = int(attempts)
		if attempts >=1 and attempts <= 6:
			while attempted < attempts:
				#kludge-y but will probably work?
				#exit program after too many invalid entries
				if invalid == 3:
					print("You have made too many invalid entries. The program will now close.")
					sys.exit()
				
				#begin roll code
				print('What type of die would you like to roll?')
				dieChoice = str(input('(Input the number of sides on the die.) '))

				if dieChoice.isdigit() == True:
					#roll the dice!
					dieType = {
						4: randint(1,4),
						6: randint(1,6),
						8: randint(1,8),
						10: randint(1,10),
						12: randint(1,12),
						20: randint(1,20),
						100: randint(1,100)
					}
					#record roll based on die choice
					result = str(dieType.get(int(dieChoice), "Invalid entry!"))
					if result.isdigit() == True:
						attempted+=1
						#add to result summary
						rollResults.append("Roll " + str(attempted) + " (D" + dieChoice + "): " + result)
						#notify user of roll result
						print("You rolled a " + result + ". You have " + str(attempts - attempted) + " rolls left.")
					else:
						#invalid number entered?
						invalid+=1
						print(result + " You can roll a 4-, 6-, 8-, 10-, 12-, 20-, or 100-sided die.")
						print("You have " + str(3-invalid) + " attempt(s) before the program closes.")
						#end roll code
				else:
					#user input has letters/symbols?
					invalid+=1
					print("Invalid entry! Please enter the number of sides as digits.")
					print("You have " + str(3-invalid) + " attempt(s) before the program closes.")
			#print result summary
			print("Below is a summary of your results:")
			pprint.pprint(rollResults)
			#exit program
			sys.exit()

		else:
			invalid+=1
			print("Invalid entry! Please enter the number of attempts as a digit between 1 and 6.")
			print("You have " + str(3-invalid) + " attempt(s) before the program closes.")
	else:
		invalid+=1
		print("Invalid entry! Please enter the number of attempts as digits.")
		print("You have " + str(3-invalid) + " attempt(s) before the program closes.")

