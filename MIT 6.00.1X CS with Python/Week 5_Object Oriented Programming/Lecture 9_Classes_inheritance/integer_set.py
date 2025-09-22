class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

#MY answer
#    1. Define an intersect method that returns a new intSet containing elements 
#       that appear in both sets. In other words,
#       s1.intersect(s2) would return a new intSet of integers 
#       that appear in both s1 and s2. 
#       Think carefully - what should happen if s1 and s2 have no elements in common?
    def intersect(self, other):
        '''
       s1.intersect(s2) 
       would return a new intSet of integers that appear in both s1 and s2. 
        '''
        NewS = intSet()
        for e in other.vals:
            if e in self.vals:
                NewS.vals.append(e)
        return NewS
    def __len__(self):
        count = 0
        for i in self.vals:
            count += 1
        return count
#Sample Solution
# =============================================================================
#     def intersect(self, other):
#         """Assumes other is an intSet
#            Returns a new intSet containing elements that appear in both sets."""
#         # Initialize a new intSet    
#         commonValueSet = intSet()
#         # Go through the values in this set
#         for val in self.vals:
#             # Check if each value is a member of the other set    
#             if other.member(val):
#                 commonValueSet.insert(val)
#         return commonValueSet
# 
#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'
# 
#     def __len__(self):
#         """Returns the length of the set.
#            This method is called by the `len` built-in function."""
#         return len(self.vals)
# =============================================================================




#s = intSet()
#print(s)
#s.insert(3)
#s.insert(4)
#s.insert(3)
#print(s)
#s.member(3)
#s.member(5)
#s.insert(6)
#print(s)
#s.remove(3)
#print(s)
##s.remove(3)
