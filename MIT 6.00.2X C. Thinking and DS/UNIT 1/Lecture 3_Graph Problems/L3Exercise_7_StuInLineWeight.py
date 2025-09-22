# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:48:46 2020

@author: LIGen
"""



# Write a WeightedEdge class that extends 
# Edge. Its constructor requires a weight 
# parameter, as well as the parameters from 
# Edge. You should additionally include a 
# getWeight method. The string value of a 
# WeightedEdge from node A to B with a 
# weight of 3 should be "A->B (3)".


# Resources Before
# =============================================================================

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
# =============================================================================

# My Answer
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return self.src.getName() + '->' + \
                self.dest.getName() + \
                   '(' + str(self.getWeight()) + ')' 
# =============================================================================
# Test
# a = Node('a')
# b = Node('b')
# testEdge = WeightedEdge(a, b, 3)
# =============================================================================

# Sample Answer
class Sample_WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"