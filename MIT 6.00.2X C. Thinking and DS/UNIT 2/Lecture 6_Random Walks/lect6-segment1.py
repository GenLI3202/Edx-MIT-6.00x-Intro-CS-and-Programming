import random

class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are numbers"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    '''
    Thinking of a field as a mapping from drunks to locations.
    Use a Dictionary as a representation of the field
    Unbounded size
    Allows multiple drunks(with no constraints about how they relate to each other)
    
    
    The key design decision embodied in this implementation
    is to make the location of a drunk in a field
    an attribute of the field rather than an attribute of the drunk.
    it allowed us to think more easily about how drunks might relate to 
    one another spatially.
    For example, could two drunks occupy the same location in the field?
         
    '''
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
        # We're not allowing a drunk to be cloned
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
        # Use raise to denfend the programming
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
            # drunk.takestep simply returns a pair
            # of numbers indicating how far the drunk has
            # moved in each of the x and y directions, delta x
            # and delta y.
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    '''
    This class seems so useless? 
    
    We use this class to handel with different drunks,
    such as "usual drunk" (who wanders around at random) or 
    "I hate winter" drunk (who tries to move southward to escape from winter)
    '''
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return 'This drunk is named ' + self.nameself.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

