# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:13:26 2016

@author: RITURAJ
"""

import matplotlib.pyplot as plt
import numpy as np
gaussian_numbers = np.random.normal(size=10000)
n, bins, patches = plt.hist(gaussian_numbers, bins=100, normed=True, stacked=True, 
         edgecolor="#6A9662",
         color="#DDFFDD",
         #cumulative=True
         )
print("bins: ", bins)
for i in range(len(bins)-1):
    print(bins[i+1] -bins[i])
print('\n\n')
print("n: ", n, sum(n))
print("patches: ", patches)
print(patches[1])
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
#print(len(gaussian_numbers))
