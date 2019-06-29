"""
Desktop/Software/Python/Sandbox/Recursion_Practice
Sieve of Eratosthenes
This program takes a number input and
outputs a list of all of the prime
numbers less than or equal to that number.
Because the inputs will likely be rather
large, the program will take a seg-
mented approach rather than tackling the
entire set of numbers.
"""

"""
the final product will not prompt for input;
sieve will be called by fibonacci.py (and
possibly other programs in the future!)
"""

import math
import time

startTime = time.time()
#remove input dialog after testing!
validInput=False
upperLim=input("Please enter a number: ")
while validInput==False:
	if str(upperLim).lstrip('-+').isdigit()==False:
		upperLim=input("Please enter a number in digit form: ")
	elif int(upperLim)<4:
		upperLim=input("Please enter a number greater than 4: ")
	elif int(upperLim)>100001:
		upperLim=input("Please enter a number less than 100000: ")
	elif "." in str(upperLim):
		upperLim=input("Please enter a whole number: ")
	else:
		upperLim=int(upperLim)
		validInput=True

"""
divide the range 3 through upperLim into
segments of segmentSize
"""
segmentSize = math.floor(math.sqrt(upperLim))-1
segBegin = 4
segEnd = segBegin+segmentSize
primes = [1,2,3]
primeMults = []

for segment in range(1,segmentSize+2):
	#determine segment lower and upper bounds
	if segment>1:
		segBegin=segEnd+1

	if segment==segmentSize+1:
		segEnd=upperLim
	else:
		segEnd=segBegin+segmentSize
	
	#num=segBegin
	#while num<segEnd:
		#check if num is a multiple of any of the contents of the primes list

	#not efficient with billions/trillions; revise
	for num in range(segBegin, segEnd+1):
		for numCheck in range(2, num):
			#check for prime number
			if num%numCheck==0:
				break
			elif numCheck==num-1:
				primes.append(num)

print("Time elapsed: " + str(time.time()-startTime))
print("All " + str(len(primes)) + " prime numbers smaller than " + str(upperLim) + ":")
print(primes)