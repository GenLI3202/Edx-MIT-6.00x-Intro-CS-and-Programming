# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:43:55 2020

@author: LIGen
"""


# MY ANSWER
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        c = a
    else:
        c = b
    for i in range(c, 0, -1):
        if a%i == 0 and b%i == 0 and i > 1:
            break
    return i

#Sample SOl.
def gcdIter_samp(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue

#MY ANSWER
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    minm = min(a, b)
    maxm = max(a, b)
    if minm == 0:
        return maxm
    else:
        return gcdRecur(minm, maxm%minm)
    ###: Actually you don't need the 'minm' and 'maxm', 
    ###  'return gcdRecur(b, a % b)' will switch the position of 'a&b' to 
    ###  the right 'min&max' order
    
#Sample Sol.
    
def gcdRecur_samp(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur_samp(b, a % b)
