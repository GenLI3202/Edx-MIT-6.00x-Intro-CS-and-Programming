# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:58:04 2020

@author: LIGen
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return None
    sumLength = 0
    for s in L:
        sumLength += len(s)
    mean = sumLength/float(len(L))
    print('sum of length is :' + str(sumLength) +"\n mean is: " + str(mean))
    tot = 0.0
    for i in range(len(L)):
        tot += (len(L[i]) - mean)**2
    std = (tot/len(L))**0.5 
    return std


# Answers by others

import statistics
import math
import time
import random
import string

def generateRandomList(size: int):
    return ["".join(random.choices(string.ascii_letters,
                                    k=random.randint(1,len(string.ascii_letters)))) for i in range(size)]

def stdDevOfLengths(s):
    """
    s: a List of sample inputs
    returns a float, the sandard deviation of the lengths of strings in list,
    NaN if L is empty.
    """
    # time.sleep(0.01)
    if not s:
        return float('nan')
    # make list of individual sample lenght
    lengths = ([len(inds) for inds in s])
    # compute mean
    mean = sum(lengths)/len(lengths)
    # compute sum of individual variance
    tot = sum([(length-mean)**2 for length in lengths])
    # compute deviation
    return (tot/len(lengths))**0.5  # standard deviation


def stdDevOfLengthsGenerator(s):
    """
    s: a List of sample inputs
    returns a float, the sandard deviation of the lengths of strings in list,
    NaN if L is empty.
    """
    # time.sleep(0.01)
    if not s:
        return float('nan')
    # make generator of individual sample lenghts
    lengths = (len(inds) for inds in s)
    # compute mean
    mean = sum(lengths)/len(s)
    # compute sum of individual variance
    tot = sum((length-mean)**2 for length in lengths)
    # compute deviation
    return (tot/len(s))**0.5  # standard deviation


def stdUsingMath(s):
    """s: a List of sample inputs
    returns a float, the sandard deviation of the lengths of strings in list,
    NaN if L is empty. Using math lib
    """
    # time.sleep(0.01)
    if not s:
        return math.nan
    return statistics.pstdev([len(i) for i in s])


timelist = []
timegenerator = []
timemat = []

random.seed(0)
sample = generateRandomList(100)

for i in range(100000):
    start = time.time()
    stdDevOfLengths(sample)
    timelist.append(time.time()-start)
    start = time.time()
    stdDevOfLengthsGenerator(sample)
    timegenerator.append(time.time()-start)
    start = time.time()
    stdUsingMath(sample)
    timemat.append(time.time()-start)

print("-----------------")
print(f"time list: {sum(timelist)/len(timelist)}")
print(f"time gen: {sum(timegenerator)/len(timelist)}")
print(f"time math: {sum(timemat)/len(timemat)}")