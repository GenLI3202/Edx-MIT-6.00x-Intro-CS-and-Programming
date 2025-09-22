import random, pylab

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
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the 
       walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))
    
def simWalks(numSteps, numTrials, dClass):
    # Simulation Walks
    """Assumes 
        numSteps an int >= 0, 
        numTrials an int > 0, 
                (# trial:  a test of the performance, qualities, or suitability of someone or something)
        dClass a subclass of Drunk
         # We use the "dClass"(drunkClass) do this so that we can use the same code
         # to simulate walks of as many different kinds of drunks
         # as we care to create.
         
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial"""
    Homer = dClass()        # Homer --- a comic character: Homer Simpson --- https://zh.wikipedia.org/wiki/%E9%9C%8D%E9%BB%98%C2%B7%E8%BE%9B%E6%99%AE%E6%A3%AE
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        # test "numTrials" times, and note down the results in
        # the list "distances"
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
            # distances is a list, within which are the different 
            # results of walks (i.e. the distances to the origin point
            # after the walk)
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """Assumes 
        walkLengths a sequence of ints >= 0
        numTrials an int > 0, 
        dClass a subclass of Drunk
         
       For each number of steps in walkLengths, runs simWalks with
       numTrials walks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
            # Remind: distances is a list of numbers
        print(' Max =', max(distances), 'Min =', min(distances))
       
random.seed(0)
drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)



class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,0.9), (0.0,-1.1),
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def simAll(drunkKinds, walkLengths, numTrials):
    '''
    to simulate all kinds of drunks

    '''
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

# drunkTest((10, 1000, 1000, 10000), 100, ColdDrunk)        
# random.seed(0)
simAll((UsualDrunk, ColdDrunk),
        (1, 10, 100, 1000, 10000), 100)
