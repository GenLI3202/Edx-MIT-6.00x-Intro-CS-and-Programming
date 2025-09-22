# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:09:36 2016

@author: guttag
"""
import random
 
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
 
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

# testRoll(5)







# random.seed(0)
# =============================================================================
# Since I'm using the same "seed" every time I run this program,
# I'll get the same answer.
# This, by the way, is incredibly useful
# when you are debugging your program
# because it allows you to have it do the same thing every time.
# =============================================================================

def runSim(goal, numTrials):
    '''
    a goal is For example five consecutive 1s, and the number 
    of trials for example, try it 1,000 times.
    firstly initialize total to 0. And then, for i in range 
    number of trials, throw the dice len(goal) number of times,
    check whether the result matches the goal.
    If it does, I'll add 1 to my total.
    If it doesn't, I won't change the total.
    '''
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('actual probability =',
          round(1/(6**len(goal)), 8)) 
        # Theoratical probability
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability  =',
          round(estProbability, 8))
    
# runSim('11111', 10000)

# =============================================================================
# So there's a lesson here.
# If you try only a small number of trials,
# and you're looking at a very rare event,
# then you're likely to get the wrong answer out.
# =============================================================================



def fracBoxCars(numTests):
    '''
    a double 6 when you roll dice is called a boxcar.
    '''
    numBoxCars = 0.0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
    
print('Frequency of double 6 =',
      str(fracBoxCars(100000)*100) + '%')












