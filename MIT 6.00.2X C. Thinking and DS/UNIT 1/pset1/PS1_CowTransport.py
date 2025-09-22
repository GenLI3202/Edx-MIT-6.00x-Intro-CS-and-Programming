###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
# =============================================================================
# Pseudo Code
#
# 1. Sort the Cows by their weights
# 2. When the Cows_List is not umpty, Do the greedy (loadCows):
#    2.1. Compare TotalWeights and limit
#    2.2. Update TotalWeights
#    2.3. Update Result
#    2.4  pop (delete) the Cows which is trasported
# 3. Add the Ships Arrangements to the final result
# =============================================================================
    # TODO: Your code here
    start = time.time()
    CowsCopy = sorted(cows, key = cows.get, reverse = True)  # Cows sorted by weights
    result = []
    def LoadCows(CowsCopy, limit):
        CowsInShip = []
        LimitTotal = 0
        for i in range(len(CowsCopy)):
            if (LimitTotal + cows.get(CowsCopy[i]) <= limit):
                CowsInShip.append(CowsCopy[i])
                LimitTotal += cows.get(CowsCopy[i])
        for cow in CowsInShip:
            CowsCopy.remove(cow)
        return CowsInShip
    while len(CowsCopy) > 0:
        result.append(LoadCows(CowsCopy, limit))
    end = time.time()
    print(end - start)
    return result



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
# =============================================================================
# Pseudo Code
# 1. Get the Partitions of CowsCopy
# 2. For each Partition, check:
#     2.1 each subset's totalweight
#     2.2 choose the first Partition which satisfied the constraints
# =============================================================================
    # TODO: Your code here
    start = time.time()
    CowsCopy = sorted(cows.keys())
    # Result = []
    # pick a partition(Transport Plan) of Cows
    for CowsPart in (get_partitions(CowsCopy)):     
        #pick each ship in the plan to check    
        for i in range(len(CowsPart)):      # i: ShipIndex; len(CowsPart): the amount of ships in this plan
            SumWeight = 0
            # calculate the sum weights of cows in i_th ship
            for j in range(len(CowsPart[i])):       #  j: CowsIndex; len(CowsPart[i]): the amount of cows in the i_th ship.
                SumWeight += cows.get(CowsPart[i][j])
            if SumWeight > limit:       # If the plan is overweight, abandon    
                break
            if i == len(CowsPart)-1:    # If the last Ship is checked and OK, and the result
                end = time.time()
                print(end - start)
                return CowsPart
        
                
                
            
            


        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    ## code to be timed
    end = time.time()
    print(end - start)
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
# print(cows)
# cows_test = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}

print('Use Greedy: ', greedy_cow_transport(cows, limit))
print('')
print('')
print('Use Brute Force: ', brute_force_cow_transport(cows, limit))


