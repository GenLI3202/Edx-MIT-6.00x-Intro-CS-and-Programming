# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:21:27 2020

@author: LIGen
"""


#  use the idea of bisection search to determine if a character is in a string, 
#  so long as the string is sorted in alphabetical order.

#by iteration

def isIn_Iter(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
#determine how to bisect the length 
    Start = 0
    End = len(aStr)
    Dist = (End - Start)
    while Dist > 1:
        CheckP = (Start+End)//2
        if char == aStr[CheckP]:
            return True
        elif char < aStr[CheckP]:
            End = CheckP
        elif char > aStr[CheckP]:
            Start = CheckP
        Dist = (End - Start)
    return False

#determine how to bisect the length by Recursion
    
#by Recursion
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
#determine how to bisect the length by iteration
    Start = 0
    End = len(aStr)
    CheckP = (Start+End)//2
    # Begin with the special case: BE CAREFUL! When the len(aStr) <= 1
    if len(aStr) == 1:
        if char == aStr:
            return True
        # line 52-53 could be written as: return char == aStr
    elif char <= aStr[CheckP]:
        return True
    elif char < aStr[CheckP]:
        return isIn(char, aStr[Start : CheckP])
    elif char > aStr[CheckP]:
        return isIn(char, aStr[CheckP : End])
    return False



###Sample Sol.
def isIn_Sample(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn_Sample(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn_Sample(char, aStr[midIndex+1:])






















