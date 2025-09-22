# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:31:50 2020

@author: LIGen
"""

# Credit Card Payment

# Problem 1

# def BalanceMon(balance, annualInterestRate, monthlyPaymentRate):
#     Mon_InRate = annualInterestRate/12.0
#     for i in range(12):
#         # print("The initial balance is: ", balance)
#         Min_MonPay = monthlyPaymentRate*balance
#         Mon_unpaidBalance = balance - Min_MonPay
#         balance = Mon_unpaidBalance + (Mon_InRate*Mon_unpaidBalance)
#         # print("The updated balance is: ", round(balance,2))
#     print("Remaining balance: ", round(balance, 2))

# BalanceMon(42, 0.2, 0.04)


# Problem 2
def PaymentFixed(balance, annualInterestRate,):
    Mon_InRate = annualInterestRate/12.0
    InitialBalance = balance
    FixedPay = 0
    while balance > 0:
        balance = InitialBalance
        FixedPay += 10
        for i in range(12):
            # print("The initial balance is: ", balance)
            Mon_unpaidBalance = balance - FixedPay
            balance = Mon_unpaidBalance + (Mon_InRate*Mon_unpaidBalance)
    print("Lowest Payment: ", round(FixedPay,2))

PaymentFixed(3329, 0.2)
    
def PayFixedBisec(balance, annualInterestRate,):
    Mon_InRate = annualInterestRate/12.0
    InitialBalance = balance
    lowPay = balance/12.0
    upperPay = (balance*(1 + Mon_InRate)**12) / 12.0    
    while abs(balance) > 0.01:
        balance = InitialBalance
        Pay = (lowPay + upperPay)/2        
        for i in range(12):
            # print("The initial balance is: ", balance)
            Mon_unpaidBalance = balance - Pay
            balance = Mon_unpaidBalance + (Mon_InRate*Mon_unpaidBalance)
        if balance > 0:
            lowPay = Pay
        else:
            upperPay = Pay
    print("Lowest Payment: ", round(Pay, 2))


PayFixedBisec(999999, 0.18)








