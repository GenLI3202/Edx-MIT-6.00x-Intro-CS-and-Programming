# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:16:26 2020

@author: LIGen
"""


#Prob 1_test Num of Vowels
s = 'asfdbobobobeerewrvobob'
numVowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'u':
        numVowels += 1
print('Number of vowels: '+str(numVowels))


#Prob 2_test Num of 'bob'
numBobs = 0
for i in range(0,len(s)-2):
    if s[i:i+3] == 'bob':
        numBobs += 1
print('Number of times bob occurs is: ' + str(numBobs))







#Solution by others for NumVowels
print("Number of vowels:", str(len([i for i in s if i in "aeiou"])))

#Solution by others for NumBobs
print("Number of times bob occurs is:", str(len([i for i in range(len(s) - 2) if s[i:i + 3] == "bob"])))