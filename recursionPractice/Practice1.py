"""
Recursion Practice #1

Implement a function product to multiply 2 numbers
recursively using + and - operators only.

Source: https://anandology.com/python-practice-book/
functional-programming.html
"""

def product(num1, num2):
	if num2 == 2:
		return num1 + num1		
	else:
		return num1 + product(num1, num2-1)
			
print("Enter two numbers.")
input1 = int(input("First number: "))
input2 = int(input("Second number: "))
print(str(input1) + "x" + str(input2) + "=" + str(product(input1,input2)))