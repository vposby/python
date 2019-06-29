"""
	This is a random number guessing game. First, a 
	random number is chosen. Then, the user guesses
	a number. If their guess is correct, the program
	prints a success message. If not, the program
	tells the user if their guess was too high or
	too low and prompts them to guess again. The
	process continues until the user guesses the
	correct number.
"""

import random

#set default values for lower and upper
lower = 1
upper = 10

#ask for user input for lower and upper
lower = input("What is the lowest number I can choose? " )
if str(lower).lstrip('-+').isdigit() == False:
	print("You didn't choose a number! Default lower bound (1) selected.")
	lower = 1
else:
	lower = int(lower)

upper = input("What is the highest number I can choose? " )
if str(upper).lstrip('-+').isdigit() == False:
	print("You didn't choose a number! Default upper bound (10) selected.")
	upper = 10
else:
	upper = int(upper)

answer = random.randrange(lower,upper + 1)

guess = str(input("Guess a number. " ))

if guess.lstrip('-+').isdigit() == True:
	while int(guess) != answer:
		if int(guess) > answer:
			guess = str(input("Guess lower! "))
		if int(guess) < answer:
			guess = str(input("Guess higher! "))
	print("You got it!")
else:
	print("Please enter a number.")
