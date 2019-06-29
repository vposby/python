"""
Recursion Practice #8

Write a function count_change to count the number of
ways to change any given amount. Available coins are
also passed as argument to the function.

Source: https://anandology.com/python-practice-book/
functional-programming.html
"""

#comment this out to finish dev;remove after dev is complete
import sys
sys.exit()

#recursive function
def count_change(amount, coins):
	if not coins:
		return 0
	else:
		return count_change(amount, coins[1:])+count_change(amount-coins[0],coins)

#user-dependent code
keepopen = True
invalid = 0
print("This program tells you the number of ways to change any given amount.")
while keepopen == True:
	print("Enter the amount for which you want change (as int):")
	valid1 = False

	#choose amount
	while valid1 == False:
		input1 = str(input())
		#Error: input1 is not numeric
		if input1.isdigit() == False:
			invalid+=1
			if invalid == 3:
				print("You have made too many invalid entries. Please restart the program.")
				keepopen = False
			else:
				print("Invalid entry! Please enter a number between 1 and 5.")
				print("You have " + str(3 - invalid) + "attempts left.")
		#Error: input1 is less than 3
		elif int(input1) < 5 or int(input1) > 100:
			invalid+=1
			if invalid == 3:
				print("You have made too many invalid entries. Please restart the program.")
				keepopen = False
			else:
				print("Invalid entry! Please enter a number between 5 and 100.")
		#Valid amount:
		else:
			input1 = int(input1)
			valid1 = True
			input2 = []

	if invalid > 0:
		print("Your invalid entries have been reset.")
	invalid = 0
	print("You can choose up to five integer values for denominations.")
	print("How many would you like to choose?")
	valid2 = False
	
	#choose number of coin denominations
	while valid2 == False:
		cointypes = str(input())
		if cointypes.isdigit() == False:
			#Error: cointypes is not numeric
			invalid+=1
			if invalid == 3:
				print("You have made too many invalid entries. Please restart the program.")
				keepopen = False
			else:
				print("Invalid entry! Please enter a number between 1 and 5.")
				print("You have " + str(3 - invalid) + "attempts left.")
		elif int(cointypes) <= 1 or int(cointypes) >=5:
			#Error: cointypes is too small or large
			invalid+=1
			if invalid == 3:
				print("You have made too many invalid entries. Please restart the program.")
				keepopen = False
			else:
				print("Invalid entry! Please enter a number between 1 and 5.")
				print("You have " + str(3 - invalid) + "attempts left.")
		#Valid cointype:
		else:
			cointypes = int(cointypes)
			input2.append("1")
			while len(input2) < cointypes:
				input2.append("")
			valid2 = True

	if invalid > 0:
		print("Your invalid entries have been reset.")
	invalid = 0
	valid3 = 1
	print("Denomination number 1 is 1-cent coins.")
	
	#build coin denomination list
	while valid3 < cointypes:
		for ind in range(1, cointypes):
			denomination = str(input("Enter denomination number " + str(ind + 1) + ": "))
			#Error: denomination is not numeric
			if denomination.isdigit() == False:
				invalid+=1
				if invalid == 3:
					print("You have made too many invalid entries. Please restart the program.")
					keepopen = False
				else:
					print("Invalid entry! Please enter a number.")
					print("You have " + str(3 - invalid) + "attempts left.")
			#Error: denomination is too large
			elif denomination > input1:
				invalid+=1
				if invalid == 3:
					print("You have made too many invalid entries. Please restart the program.")
					keepopen = False
				else:
					print("Invalid entry! Please enter a number lower than the amount. ")
					print("You have " + str(3 - invalid) + "attempts left.")
			#Error: denomination is a duplicate
			elif denomination == input2[ind - 1]:
				invalid+=1
				if invalid == 3:
					print("You have made too many invalid entries. Please restart the program.")
					keepopen = False
				else:
					print("Invalid entry! Please enter a number that isn't already on the list.")
					print("You have " + str(3 - invalid) + "attempts left.")
			#Valid denomination:
			else:
				input2[denomination] = int(input2[denomination])
				valid3+=1
	#final output
	input2.sort()
	print(count_change(input1, input2))
	keepopen = False
		
	
	