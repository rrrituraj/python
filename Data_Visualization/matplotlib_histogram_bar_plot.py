# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:45:46 2016

@author: RITURAJ
"""
import matplotlib.pyplot as plt
import numpy as np
years = ('2010', '2011', '2012', '2013', '2014')
visitors = (1241, 50927, 162242, 222093, 296665 / 8 * 12)
index = np.arange(len(visitors))
bar_width = 1.0
plt.bar(index, visitors, bar_width,  color="green")
plt.xticks(index + bar_width / 2, years) # labels get centered
plt.show()