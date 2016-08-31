# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:13:33 2016

@author: RITURAJ
"""
'''
remove the comment quotes and see the magic
'''

#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
'''
plt.plot([-1, -4.5, 16, 23], 'dk')
plt.show()
'''


'''
# our X values:
days = list(range(0, 22, 3))
print(days)
# our Y values:
celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
plt.plot(days, celsius_values)
plt.show()
'''

'''
days = list(range(1,9))
celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
plt.plot(days, celsius_min,
         days, celsius_min, "oy",
         days, celsius_max, 
         days, celsius_max, "or")
print("The current limits for the axes are:")        
print(plt.axis())
print("We set the axes to the following values:")
xmin, xmax, ymin, ymax = 0, 10, 14, 45
print(xmin, xmax, ymin, ymax)
plt.xlabel('Day')
plt.ylabel('Degree Celsius')
plt.axis([xmin, xmax, ymin, ymax])
plt.show(
)'''

'''
X = np.linspace(-2*np.pi, 2*np.pi, endpoint= True)
F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)
F4 = np.cos(X)
F= np.sin(X)
#print(X,)
#print(F,)
plt.plot(X, F1, color="blue", linewidth=2, linestyle="-.")
plt.plot(X, F2, color="red", linewidth=1.5, linestyle="--")
plt.plot(X, F3, color="green", linewidth=2, linestyle=":")
plt.plot(X, F4, color="grey", linewidth=2, linestyle="-.")
startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -3, 3
plt.axis([startx, endx, starty, endy])
plt.show()
'''

#fill_between function use
n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)
plt.plot (X, Y, color='blue', alpha=0.6)
plt.fill_between(X, 0, Y, color='blue', alpha=0.1)
plt.show()