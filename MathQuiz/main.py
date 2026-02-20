#Title: Math Quiz
#Author: Dominic Corneliusen
#Date Last Modified: 2/19/2026

#Imports
import random
from tokenize import String

#Variable
isFinished = False
#Method
def addition_quiz():
    number1 = random.randint(1, 999)
    number2 = random.randint(1, 999)
    total = number1 + number2
    print("      ", number1)
    print("   +   ", number2)
    print("-----------")
    answer = int(input("="))
    if answer != total:
        print("Wrong answer. The correct answer is", total)
    else:
        print("Correct!")
#while loop
while not isFinished:
    addition_quiz()
    doesUserWantMoreMath = str(input("Would you like to do more math? (y/n)"))
    if doesUserWantMoreMath == "yes" or doesUserWantMoreMath == "y":
        pass
    else:
        isFinished = True
#Final print statement
print("Thank you for testing your addition skills!")