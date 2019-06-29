"""
Splat Calculator
Given an object's mass and distance from the ground,
calculate the time it would take for the object
to reach the ground.
"""

import sys

gravity = 9.8 #at 1g, gravity pulls at 9.8m/s^2

def chooseUnits():
	print("What units would you prefer to use?")
	units = str(input("Choose between oz, lb, g, and kg. "))
	checkInput(units)
	if units=="oz" or units=="lb" or units=="g" or units=="kg":
		chooseMass(units)
	else:
		print("Invalid entry! Please enter either \'oz\', \'lb\', \'g\', or \'kg\'.")

def checkInput(userInput):
	if userInput=="exit":
		sys.exit()

def convertMass(units):
	global mass
	if units=="oz":
		#convert to g
	elif units=="lb":
		#convert to g
	elif units=="kg":
		mass=mass/10