# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:17:41 2016

@author: WELG
"""



# Exercise 2
# How would you randomly generate an even number x, 0 <= x < 100? 
# Fill out the definition for the function genEven(). Please 
# generate a uniform distribution over the even numbers between 
# 0 and 100 (not including 100).

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)


# =============================================================================
# # There are many good answers to this problem, some easier than others :)
# def genEven():
#     return random.randrange(0, 100, 2)
# 
# def genEven():
#     return random.choice(range(0, 100, 2))
# 
# def genEven():
#     return int(random.random() * 50)*2
# 
# def genEven():
#     return random.choice(range(0, 50))*2
# 
# def genEven():
#     x = random.randint(0, 98)
#     while x % 2 != 0:
#         x = random.randint(0, 98)
#     return x
# 
# =============================================================================



# Exercise 3-1
# Write a deterministic program, deterministicNumber, that 
# returns an even number between 9 and 21.

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    random.seed(2)
    return random.choice(range(10,21,2))
    
#Sample Answers
# Possible solutions:

# =============================================================================
# def deterministicNumber():
#     return 10 # or 12 or 14 or 16 or 18 or 20
# 
# # or
# 
# def deterministicNumber():
#     random.seed(0) # This will be discussed in the video "Drunken Simulations"
#     return 2 * random.randint(5, 10)
# =============================================================================


# =============================================================================
# Are the following two distributions equivalent?
# 1:
# def dist1():
#     return random.random() * 2 - 1
# 
# 2:
# def dist2():
#     if random.random() > 0.5:
#         return random.random()
#     else:
#         return random.random() - 1 
#     

# Answer: Yes!
# The random.random() distribution is uniform, so both dist1 
# and dist2 are a uniform distribution over [-1.0, 1.0).
# 
# Notice: dist2 is different from dist 3:
# def dist3():
    # n = random.random()
    # if n > 0.5:
    #     return n
    # else:
    #     return n - 1 
# =============================================================================
# 




# =============================================================================
# Are the following two distributions equivalent?

# import random
# def dist5():
#     return int(random.random() * 10)

# def dist6():
#     return random.randint(0, 10)
#
#
#
#
#
# Answer: No
# 
# 
# Explanation:
# 
# The random.random() distribution is uniform, and so is the random.randint() distribution. However unlike random.randrange(start, end), random.randint(start, end) returns a distribution that is inclusive of both the given start and end points.
# 
# Thus dist5 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], but dist6 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# 
# You can code a simple simulation to see what a distribution looks like using dictionaries:
# 
# d1 = {}
# for i in range(10000):
#     x = random.randrange(10) 
#     d1[x] = d1.get(x, 0) + 1
# d2 = {}
# for i in range(10000):
#     x = int(random.random()*10)
#     d2[x] = d2.get(x, 0) + 1
# d3 = {}
# for i in range(10000):
#     x = random.randint(0, 10)
#     d3[x] = d3.get(x, 0) + 1
# Examine the values of the three dictionaries to see what sort of distribution results!
# 
# Question to ponder: Should all the values of the dictionaries be equal? That is, should d1[x] == d1[y] for all values of x and y, where x != y and both x and y are values in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?

# =============================================================================





def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
        print(result)





