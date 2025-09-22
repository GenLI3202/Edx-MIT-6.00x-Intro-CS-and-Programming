# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:25:20 2016

@author: ericgrimson
"""

def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
    # "func_c(func_a)" calls func_c, takes one parameter, anotherfunction

print("     //that's very confused//     ")

def func_d(x):
    print('inside func_d')
    return x
print(func_d(func_c(func_a)))
print(func_d(func_c))
print(func_d('happy'))

def h(x):
    x += 1

x = 5
h(x)
print(x)