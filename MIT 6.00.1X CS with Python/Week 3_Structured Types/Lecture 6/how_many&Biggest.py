# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:28:07 2020

@author: LIGen
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    number = 0
    for key in aDict:
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        number += len(aDict[key])
    return number

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxNum = 0
    for key in aDict:
        if len(aDict[key]) >= maxNum:
            maxNum = len(aDict[key])
            maxKey = key
    return maxKey