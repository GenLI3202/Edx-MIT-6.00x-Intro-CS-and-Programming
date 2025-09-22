# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:46:42 2020

@author: LIGen
"""

# Assume "s" is a string of lower case characters.

# Write a program that prints the longest substring of "s" in which the letters occur 
# in alphabetical order. For example, if " s = 'azcbobobegghakl' ", then your program 
# should print:
    
# =============================================================================
# Longest substring in alphabetical order is: beggh
# =============================================================================

# In the case of ties, print the first substring. For example, if "s = 'abcbcd' ", then 
# your program should print:
    
# =============================================================================
# Longest substring in alphabetical order is: abc
# =============================================================================




# Note: This problem may be challenging. We encourage you to work smart. If you've 
# spent more than a few hours on this problem, we suggest that you move on to a 
# different part of the course. If you have time, come back to this problem after 
# you've had a break and cleared your head.




#Input
# s = 'dabcdefiigl'
# s = 'azcbobobegghakl'
# s = 'abcbcd'
# s = 'abcdefghijklmnopqrstuvwxyz'
# s = 'zaqwgianjcj'
s = 'phniffdqt'

SubStrResult = ''
SubStrTemp = s[0]

#Process
for i in range(0,len(s)-1):
    if s[i] <= s[i+1]:
        SubStrTemp += s[i+1]
    if len(SubStrResult) < len(SubStrTemp):
        SubStrResult = SubStrTemp
    if s[i] > s[i+1]:    
        SubStrTemp = s[i+1]

# Result
print('Longest substring in alphabetical order is: ', SubStrResult)
            
                
            










