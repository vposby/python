"""
This program will take string input, check
for numbers, and output the associated number
(as long as the associated number is under
thirty digits long)
"""

#!!!write fix for magnitude not populating if zero in one's place

import pprint
import sys

numRef = open("numberTest.txt") #address of number/string reference file
numInfo = {} #empty dictionary

#empty lists to hold program output
numDigit = []
numText = []

mode = "text" #what type of input?
invalid = 0 #invalid entry counter
modeChosen = False #mode chosen?
outputGiven = False #input given?

#prohibited characters
prohibited = "()[]<>:;?~`!@#$%^&*_+=,-/\\\"\'"
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Type \"exit\" at any time to close the program.")

while modeChosen == False:
	print("Type \"1\" to convert from text to digits.")
	print("Type \"2\" to convert from digits to text.")
	mode = str(input())

	#remove prohibited characters
	for char in prohibited:
		mode.replace(char,"")

	#pull reference file contents into dictionary
	if mode.isdigit() == True:
		if int(mode) == 1:
			#user input is text, key is text, val is number
			mode = "text"
			for line in numRef.readlines():
				if line[0].isdigit() == True or line[0] == ".":
					(val, key) = line.split()
					numInfo[key] = val
			numRef.close
			modeChosen = True
		elif int(mode) == 2:
			#user input is digits, key is digits, val is text
			mode = "digits"
			for line in numRef.readlines():
				if line[0].isdigit() == True or line[0] == ".":
					(key, val) = line.split()
					numInfo[key] = val
			numRef.close
			modeChosen = True
		else:
			invalid+=1
			if invalid < 3:
				print("Invalid mode! Please enter a \"1\" or a \"2\".")
			elif invalid == 3:
				print("You have made too many invalid entries. The program will now close.")
				numRef.close
				sys.exit()			
	elif mode == "exit":
		numRef.close
		sys.exit()
	else:
		invalid+=1
		if invalid < 3:
			print("Invalid mode! Please enter a number or type \"exit\".")
		elif invalid == 3:
			print("You have made too many invalid entries. The program will now close.")
			numRef.close
			sys.exit()

#reset invalid entry counter
invalid = 0

while outputGiven == False:
	#if number is entered as digits
	if mode == "digits":
		#ask for user input
		numDigit = str(input("Enter a number as " + mode + ". ")).lower()

		#remove prohibited characters
		for char in prohibited:
			numDigit = numDigit.replace(char,"")

		#if input is "exit", exit program
		if numDigit == "exit":
			sys.exit()
		#if user enters text, reject input, add to invalid counter
		elif numDigit.isdigit() == False:
			invalid+=1
			if invalid < 3:
				numDigit = str(input("Invalid entry! Please enter your input as " + mode + ". ")).lower()
			elif invalid == 3:
				print("You have made too many invalid entries. The program will now close.")
				sys.exit()
			
		else:
			#add letters and whitespace to prohibited character list
			prohibited = prohibited + alphabet + " " + alphabet.upper()

			#remove prohibited characters
			for char in prohibited:
				numDigit = numDigit.replace(char,"")

			#trim any leading zeros
			numDigit = str(int(numDigit))

			#start digit to text conversion code
			numDigit = list(numDigit)
			if len(numDigit) > 31:
				invalid+=1
				print("This number is " + str(len(numDigit)) + " digits - too large for this program to convert!")
				if invalid == 3:
					print("You have made too many invalid entries.")
					sys.exit()
			else:
				#pull corresponding words from dictionary
				ind = 0
				word = 0
				while ind < len(numDigit):
					#numbers in the ten's place of a triad
					if (len(numDigit)-ind)%3 == 2:
						if int(numDigit[ind]) == 0:
							#move to the next number
							ind+=1
						elif int(numDigit[ind]) == 1:
							#find the corresponding teen
							numText.append(numInfo.get(numDigit[ind] + numDigit[ind + 1]," "))
							word+=1
							#find the number of digits following the number
							magnitude = "1"
							for x in range(len(numDigit)-ind-2):
								magnitude = magnitude + "0"
							numText[word-1] = numText[word-1] + " " + numInfo.get(magnitude," ") + " "
							numText[word-1] = numText[word-1].lstrip()
							#move to the next number
							ind+=2
						else:
							numText.append(numInfo.get(numDigit[ind] + "0"," ") + " ")
							numText[word] = numText[word].lstrip()
							word+=1
							ind+=1
					#numbers in the one's place of a triad
					elif (len(numDigit)-ind)%3 == 1:
						if int(numDigit[ind]) == 0:
							ind+=1
						else:
							numText.append(numInfo.get(numDigit[ind]," "))
							word+=1
							if len(numDigit)-ind != 1:
								#find the number of digits following the number
								magnitude = "1"
								for x in range(len(numDigit)-ind-1):
									magnitude = magnitude + "0"
								numText[word-1] = numText[word-1] + " " + numInfo.get(magnitude," ") + " "
								numText[word-1] = numText[word-1].lstrip()
							ind+=1
					#numbers in the hundred's place of a triad
					elif (len(numDigit)-ind)%3 == 0:
						if int(numDigit[ind]) == 0:
							ind+=1
						else:
							numText.append(numInfo.get(numDigit[ind]," ") + " hundred ")
							numText[word] = numText[word].lstrip()
							word+=1
							ind+=1
				print("".join(numText))
				outputGiven = True
			#end digit to text conversion code
		
	#if number is entered as text
	else:
		#ask for user input
		numText = str(input("Enter a number as " + mode + ". ")).lower()

		#remove prohibited characters
		for char in prohibited:
			numText = numText.replace(char,"")

		#if input is "exit", exit program
		if numText == "exit":
			sys.exit()
		else:
			#add numbers to prohibited character list
			prohibited = prohibited + "1234567890"

			#remove prohibited characters
			for char in prohibited:
				numText = numText.replace(char,"")

			#remove "ands"
			numText = numText.replace("and","")

			#trim any leading and trailing spaces
			numText = numText.strip()

			#start text to digit conversion code
			numText = numText.split()
			if len(numText) >= 49:
				invalid+=1
				print("This number has " + str(len(numText)) + " words - too large for this program to convert!")
				if invalid == 3:
					print("You have made too many invalid entries.")
					sys.exit()
			else:
				ind = 0
				inputError = []
				misspell = 0
				while ind < len(numText):
					#count the number of errors
					for pos, val in enumerate(numText):
						if numInfo.get(val,"Invalid") == "Invalid":
							#log error index and value
							inputError.append(str(misspell) + ", " + str(pos) + ": " + val)
							misspell+=1
					#look for spelling errors
					while misspell > 0:
						print("The existing spelling errors are as follows:")
						print(inputError) #remove this line after testing is complete
						for x in range(misspell):
							(pos, val) = inputError[x].split(",")
							(loc, val) = val.split(":")
							pos = int(pos.strip())
							loc = int(loc.strip())
							val = val.strip()
							#prompt user for corrective input
							print("Error: word number " + str(loc + 1) + " (" + val + ") is spelled incorrectly!")
							numText[loc] = str(input("Please enter the word using the correct spelling: "))
							#if the replacement is valid, notify the user of the change
							if numText[loc] == "exit":
								sys.exit()
							elif numInfo.get(numText[loc],"Invalid") != "Invalid":
								print("Word number " + str(loc + 1) + " is now " + numText[loc] + ".")
								print(inputError) #use this to check what inputError looks like after each loop
								misspell-=1
							else:
								(prefix, err) = inputError[x].split(":")
								inputError[x] = prefix + ": " + numText[loc]
								print(inputError)
					#pull corresponding digits from dictionary
					for word in numText:
						numDigit.append(numInfo.get(word))
						ind+=1
				numComponent = 0
				numOutput = 0
				for num in numDigit:
					if int(num)<100:
						numComponent+=int(num)
						print("numComponent: " + str(numComponent))
					elif int(num)==100:
						numComponent=(numComponent * int(num))
						print("numComponent: " + str(numComponent))
					else:
						numOutput+=(numComponent * int(num))
						print("numOutput: " + str(numOutput))
						numComponent = 0
				numOutput+=numComponent
				print(numOutput)
				outputGiven = True