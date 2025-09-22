# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:31:51 2020

@author: LIGen
"""


##Give an Input
print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = False

##Ask clues and remind wrong input
while guess is not True:
    guessed = (low + high)//2
    print("Is your secret number " + str(guessed) + "?")
    clue = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if clue == 'c':
        guess = True

    elif clue == 'l':
        low = guessed

    elif clue == 'h':
        high = guessed 
        
    else:
        print('Sorry, I did not understand your input.')
    
print('Game over. Your secret number was: ' + str(guessed))
        
        