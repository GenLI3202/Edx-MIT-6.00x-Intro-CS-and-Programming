# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:32:43 2020

@author: LIGen
"""

import math

def polysum(n, s):
    '''
    A regular polygon has 
    'n': number of sides. 
    's': length of each side.
    
    return: Sum of 'area' and 'square of the perimeter' of the polygon
    '''
    #numerator
    Nume = 0.25*n*(s**2)
    #denominator
    Deno = math.tan(math.pi/n)
    Area = Nume/Deno
    SqPeri = (n*s)**2
    Sum = Area + SqPeri
    return round(Sum,4)

