# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:57:36 2016

@author: RITURAJ
"""

import matplotlib.pyplot as plt
python_course_green = '#476042'
#plt.figure(figsize=(6,4))
plt.subplot(221)
plt.text(0.5, # x coordinate, 0 leftmost positioned, 1 rightmost
         0.5, # y coordinate, 0 topmost positioned, 1 bottommost
         'subplot(2,2,1)', # the text which will be printed
         horizontalalignment='center', # shortcut 'ha' 
         verticalalignment='center', # shortcut 'va'
         fontsize=20, # can be named 'font' as well
         alpha=.5 # float (0.0 transparent through 1.0 opaque)
         )
plt.subplot(222)
plt.text(0.5, 0.5, 
         'subplot(2,2,2)', 
         ha='center', va='center',
         fontsize=20, 
         color="k")
plt.subplot(223)
plt.text(0.5, 0.5, 
         'subplot(2,2,3)', 
         ha='center', va='center',
         fontsize=20, 
         color="g")
plt.subplot(224, axisbg=python_course_green)
plt.text(0.5, 0.5, 
         'subplot(2,2,4)', 
         ha='center', va='center',
         fontsize=20, 
         color="y")
plt.show()