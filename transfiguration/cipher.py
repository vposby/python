"""
This program will take string input,
run it through all possible shift
ciphers, and output all results
along with their reversed counterparts.
"""

import pprint, sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
prohibited = "()[]<>:;?~`!@#$%^&*_+=,-/\\\"\'"
num = 1
invalid = 0

def transmute(list,num):
    forward = ""
    for word in list:
        for letter in word:
            if alphabet.find(letter)+num > 25:
                forward+=alphabet[alphabet.find(letter)+num-26]
            else:
                forward+=alphabet[alphabet.find(letter)+num]
    backward = forward[::-1]
    return (forward,backward)

ogText = str(input("Please enter the string you wish to analyze: "))
for char in prohibited:
    ogText.replace(char,"")
if ogText.isdigit() == True:
    invalid+=1
    if invalid < 3:
        print("Invalid string! Please enter text with no numbers.")
    elif invalid == 3:
        print("You have made too many invalid entries. Goodbye.")
else:
    ogText = ogText.split(" ")
    for x in range(26):
        fwdNew = bkwdNew = ""
        for word in ogText:
            (fwd,bkwd) = transmute(word,x)
            fwdNew+=fwd+" "
            bkwdNew+=bkwd+" "
        print(str(x)+"-Letter Shift "+" - "+fwdNew.strip()
        +"; Reversed - "+bkwdNew.strip())
