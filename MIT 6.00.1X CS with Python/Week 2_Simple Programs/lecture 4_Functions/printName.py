# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:14:30 2016

@author: ericgrimson
"""

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

def n_1(x):
    if x == 1:
        return x
    else:
        return x * n_1(x-1)
    
def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return (base * recurPower(base, exp-1))
    
def iterPower1(base, exp):
    result = 1
    for i in range(0,exp):
        result *= base
    return result