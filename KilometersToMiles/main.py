#Title: Kilometer Converter
#Author: Dominic Corneliusen
#Date Last Modified: 2/17/2026

#Function
def convert_kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles
userInput = int(input("Enter a distance in Kilometers."))
kilometersAsMiles = convert_kilometers_to_miles(userInput)
print(kilometersAsMiles)