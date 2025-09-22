# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:17:17 2016

@author: ericgrimson
"""

#import numpy as np
import pylab as plt


mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    


# first trial
# plt.figure('linear&Quadr')
# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)
# plt.figure('Cub&Exp')
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)

# second trial
# plt.figure('lin')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.plot(mySamples, myExponential)

# third trial
# plt.figure('lin')
# plt.xlabel('sample points')
# plt.ylabel('linear function')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.plot(mySamples, myExponential)
# plt.figure('quad')                  # call the printed figure before ... 
# plt.ylabel('quadratic function')    # ... before adding a new labe to y-coordinate

# fourth trial
# plt.figure('lin')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.plot(mySamples, myExponential)
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.title('Quadratic')
# plt.figure('cube')
# plt.title('Cubic')
# plt.figure('expo')
# plt.title('Exponential')

# fifth trial
# plt.figure('lin')
# plt.clf()                   #clf: "clear the frame" function, to clear the figures which are previously painted
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.clf()
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.clf()
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.clf()
# plt.plot(mySamples, myExponential)
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.title('Quadratic')
# plt.figure('cube')
# plt.title('Cubic')
# plt.figure('expo')
# plt.title('Exponential')

# sixth trial
# plt.figure('lin')
# plt.clf()
# plt.ylim(0,1000)
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.clf()
# plt.ylim(0,1000)
# plt.plot(mySamples, myQuadratic)
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.title('Quadratic')

# seventh trial
# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube exp')
# plt.clf()
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)
# plt.figure('lin quad')
# plt.title('Linear vs. Quadratic')
# plt.figure('cube exp')
# plt.title('Cubic vs. Exponential')

# eighth trial
# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples, myLinear, label = 'linear')
# plt.plot(mySamples, myQuadratic, label = 'quadratic')
# plt.legend(loc = 'upper center')
# plt.title('Linear vs. Quadratic')
# plt.figure('cube exp')
# plt.clf()
# plt.plot(mySamples, myCubic, label = 'cubic')
# plt.plot(mySamples, myExponential, label = 'exponential')
# plt.legend()
# plt.title('Cubic vs. Exponential')

# ninth trial
#plt.figure('lin quad')
#plt.clf()
#plt.plot(mySamples, myLinear, 'b-', label = 'linear')
#plt.plot(mySamples, myQuadratic,'ro', label = 'quadratic')
#plt.legend(loc = 'upper left')
#plt.title('Linear vs. Quadratic')
#plt.figure('cube exp')
#plt.clf()
#plt.plot(mySamples, myCubic, 'g^', label = 'cubic')
#plt.plot(mySamples, myExponential, 'r--',label = 'exponential')
#plt.legend()
#plt.title('Cubic vs. Exponential')

# tenth trial
# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
# plt.plot(mySamples, myQuadratic,'r', label = 'quadratic', linewidth = 3.0)
# plt.legend(loc = 'upper left')
# plt.title('Linear vs. Quadratic')
# plt.figure('cube exp')
# plt.clf()
# plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 4.0)
# plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 5.0)                 #k is black
# plt.legend()
# plt.title('Cubic vs. Exponential')

# eleventh trial
# plt.figure('lin quad')
# plt.clf()
# plt.subplot(211)                    # arguments "211" here are number of rows, columns and which location to use
# plt.ylim(0, 900)
# plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
# plt.subplot(212)
# plt.ylim(0, 900)
# plt.plot(mySamples, myQuadratic,'r', label = 'quadratic', linewidth = 3.0)
# plt.legend(loc = 'upper left')
# plt.title('Linear vs. Quadratic')
# plt.figure('cube exp')
# plt.clf()
# plt.subplot(122)
# plt.ylim(0, 140000)
# plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 4.0)
# plt.subplot(122)
# plt.ylim(0, 140000)
# plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 5.0)
# plt.legend()
# plt.title('Cubic vs. Exponential')

# twelfth trial
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 4.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')
plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 4.0)
plt.legend()
plt.title('Cubic vs. Exponential')







