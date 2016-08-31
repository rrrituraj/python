# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:57:36 2016

@author: RITURAJ
"""
'''
#remove comment and run this part of code only
#here i have created a subplot of 3*2 where 1 plot spanned complete
import  matplotlib.pyplot as plt
X = [ (1,2,1), (3,2,2), (3,2,4), (3,2,6) ]
for nrows, ncols, plot_number in X:
    plt.subplot(nrows, ncols, plot_number)
'''
import matplotlib.pyplot as plt
import numpy as np
from numpy import e, pi, sin, exp, cos
def f(t):
    return exp(-t) * cos(2*pi*t)
def fp(t):
    return -2*pi * exp(-t) * sin(2*pi*t) - e**(-t)*cos(2*pi*t)
def g(t):
    return sin(t) * cos(1/(t+0.1))
def gp(t):
    return sin(t) * cos(1/(t))
#python_course_green = '#476042'
fig = plt.figure(figsize=(7,6))
#plt.subplot(221)
t = np.arange(-5.0, 1.0, 0.1)
sub1 = fig.add_subplot(221) # equivalent to: plt.subplot(2, 2, 1)
sub1.set_title('The function f') # non OOP: plt.title('The function f')
sub1.plot(t, f(t))
'''
sub1.text(0.5, # x coordinate, 0 leftmost positioned, 1 rightmost
         0.5, # y coordinate, 0 topmost positioned, 1 bottommost
         'subplot(2,2,1)', # the text which will be printed
         horizontalalignment='right', # shortcut 'ha' 
         verticalalignment='center', # shortcut 'va'
         fontsize=20, # can be named 'font' as well
         alpha=.5 # float (0.0 transparent through 1.0 opaque)
         )
         ''' 
sub2 = fig.add_subplot(222, axisbg="lightgrey")         
sub2.set_title('fp, the derivation of f')
sub2.plot(t, fp(t))
'''
plt.text(0.5, 0.5, 
         'subplot(2,2,2)', 
         ha='center', va='center',
         fontsize=20, 
         color="k")
'''         
'''
we don't need to the ticks on the axes         
plt.xticks(())
plt.yticks(())
'''   
t = np.arange(-3.0, 2.0, 0.02)      
sub3 = fig.add_subplot(223)
sub3.set_title('The function g')
sub3.plot(t, g(t))
'''
plt.text(0.5, 0.5, 
         'subplot(2,2,3)', 
         ha='center', va='center',
         fontsize=20, 
         color="g")
#we don't need to the ticks on the axes         
plt.xticks(())
plt.yticks(())
'''   
t = np.arange(-0.2, 0.2, 0.001)      
sub4 = fig.add_subplot(224, axisbg='lightgrey')
sub4.set_title("function of gp")
sub4.plot(t, gp(t))
'''
plt.text(0.5, 0.5, 
         'subplot(2,2,4)', 
         ha='center', va='center',
         fontsize=20, 
         color="y")
#we don't need to the ticks on the axes         
plt.xticks(())
plt.yticks(())
'''         
plt.show()
