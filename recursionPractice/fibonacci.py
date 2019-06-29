"""
Desktop/Software/Python/Sandbox/Recursion_Practice
Create list of user-determined size
containing numbers of Fibonacci series
up to seqEnd. Create another array
containing a subset of only the prime
numbers from the first array.
"""

#fibonacci sequence starters
seq = [0,1]
#prime number starters
seqPrime = [1, 2, 3]

#user input
seqEnd = input("How many fibonacci numbers would you like to see? ")
validInput = False

#validate user input
while validInput!=True:
	if str(seqEnd).lstrip('-+').isdigit() == False:
		seqEnd=input("Invalid input! Please enter a number: ")
	elif int(seqEnd)<10 or int(seqEnd)>100:
		seqEnd=input("Invalid input! Please enter a number between 10 and 100: ")
	else:
		seqEnd=int(seqEnd)
		validInput=True

#create Fibonacci series array
for fibNum in range(seqEnd+1):
	seq.append(seq[fibNum]+seq[fibNum+1])

#output results
print("The first " + str(seqEnd) + " numbers of the Fibonacci series:")
print(seq[2:len(seq)-1])

#below, only print primes if user agrees and seqEnd<40
#eventually, replace below with call for sieve.py
"""
#determine which Fibonacci series numbers are primes
for prime in range(5, len(seq)):
	for numCheck in range(3, seq[prime]):
		#check for prime number
		if seq[prime]%numCheck==0:
			break
		elif numCheck==seq[prime]-1:
			seqPrime.append(seq[prime])

print("The first " + str(len(seqPrime)) + " prime numbers of the Fibonacci series:")
print(seqPrime)
"""
