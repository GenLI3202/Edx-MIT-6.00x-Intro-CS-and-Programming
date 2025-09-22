# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:30:07 2020

@author: LIGen
"""





def genPrimes():
    Prim_dic = {1:2, 2:3} # Prim_dic
    key_Pdic = 2
    
    #Test Function is right
    def PrimeTest(x):
        for Prime in Prim_dic.values():
            if (x % Prime) != 0:        #Test if (x % p) != 0 for all earlier primes p
                test = True
            else:
                test = False
                break
        return test
    # Test if (x % p) != 0 for all earlier primes p
    x = 5    
    while x >= (Prim_dic[key_Pdic]+1):
        if PrimeTest(x) == True:
            key_Pdic += 1
            Prim_dic[key_Pdic] = x
            x += 1
            yield Prim_dic[key_Pdic]
        else:
            x += 1


#Sample Solution
# =============================================================================
# # Note that our solution makes use of the for/else clause, which 
# # you can read more about here:
# # http://docs.python.org/release/1.5/tut/node23.html 
# 
# def genPrimes():
#     primes = []   # primes generated so far
#     last = 1      # last number tried
#     while True:
#         last += 1
#         for p in primes:
#             if last % p == 0:
#                 break
#         else:
#             primes.append(last)
#             yield last
#     
# =============================================================================
    
    
    
    
    
    
# =============================================================================
# def genFib():
#     fibn_1 = 1 #fib(n-1)
#     fibn_2 = 0 #fib(n-2)
#     while True:
#         # fib(n) = fib(n-1) + fib(n-2)
#         next = fibn_1 + fibn_2
#         yield next
#         fibn_2 = fibn_1
#         fibn_1 = next
# =============================================================================
