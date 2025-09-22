# -*- coding: utf-8 -*-
"""
Created on Tue May 10 08:18:02 2016

@author: WELG
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
# Answer    
    def __eq__(self, other):
       # return self.getX == other.getX and self.getY == other.getY
       # line 29 calls a RecursionError: maximum recursion depth exceeded in comparison
       # because the '()' is missed in self.getX
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate' + '(' + str(self.getX()) + ',' + str(self.getY()) +')'


    
#Sample Solution
# =============================================================================
#     def __eq__(self, other):
#         # First make sure `other` is of the same type 
#         assert type(other) == type(self)
#         # Since `other` is the same type, test if coordinates are equal
#         return self.getX() == other.getX() and self.getY() == other.getY()
# 
#     def __repr__(self):
#         return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'  
# 
# =============================================================================
c = Coordinate(3,4)
origin = Coordinate(0,0)