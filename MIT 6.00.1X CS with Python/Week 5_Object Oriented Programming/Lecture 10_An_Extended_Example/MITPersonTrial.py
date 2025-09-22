# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:10:59 2016

@author: ericgrimson
"""

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)
    def getBirthday(self):
        return self.birthday

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    # other methods

    def __str__(self):
        """return self's name"""
        return self.name


class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
        
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
        

# example usage

# =============================================================================
# m3 = MITPerson('Mark Zuckerberg')
# Person.setBirthday(m3,5,14,84)
# m2 = MITPerson('Drew Houston')
# Person.setBirthday(m2,3,4,83)
# m1 = MITPerson('Bill Gates')
# Person.setBirthday(m1,10,28,55)
# 
# 
# 
# MITPersonList = [m1, m2, m3]
# 
# 
# for e in MITPersonList:
#     print(e)
#     
# MITPersonList.sort()
# 
# print()
# 
# for e in MITPersonList:
#     print(e)
# 
# =============================================================================


'''
#p1 = MITPerson('Eric')
#p2 = MITPerson('John')
#p3 = MITPerson('John')
#p4 = Person('John')
#p1<p2


#p1<p4
# =============================================================================
# This will cause error, because Python reads the codes "p1" firstly and then
# generates function "p1.__lt__(p4)", which is under the class of "MITPerson". 
# "p4" however just belongs to the "Person" class and doesn't have the MITIdNum,
# couldn't be compared with "p1" from class of MITPerson, so it causes AttributeError
# 
# =============================================================================

#p4<p1
# =============================================================================
# But! This will generate ''False'', because this code generates:
# p4.__lt__(p1). Both p4 and p1 belong to the class of "Person", could be compared
# with each other.
# =============================================================================

'''


'''
#Undergraduate
class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

#Graduate
class Grad(MITPerson):
    pass

class TransferStudent(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)
'''


class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year
        
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)
   