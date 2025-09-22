# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:24:32 2020

@author: LIGen
"""
import random

def drawBalls(balls, numTrials):
    '''
    Parameters
    ----------
    balls : list with balls
        
    numTrials : int

    Returns: result of drawing balls
    -------
    '''
    drawsResult = []
    for i in range(numTrials):
        drawsResult.append(random.sample(balls,3))
    return drawsResult
    

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    balls = ['r','r','r', 'g','g','g']
    result = drawBalls(balls, numTrials)
    sameTimes = 0
    for i in range(len(result)):
        if result[i] == ['r','r','r'] or result[i] == ['g','g','g']:
            sameTimes += 1
    pbSame = sameTimes/float(len(result))
    return pbSame

# noReplacementSimulation(6000)