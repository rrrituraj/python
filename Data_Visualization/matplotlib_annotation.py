# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:41:46 2016

@author: RITURAJ
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 3 * np.pi, 70, endpoint=True)
F1 = np.sin(X)
F2 = 3 * np.sin(X)
# get the current axes, creating them if necessary:
ax = plt.gca()
# making the top and right spine invisible:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# moving bottom spine up to y=0 position:
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
# moving left spine to the right to position x == 0:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -2, -1, 0, 1, 2, 3])
x = 3 * np.pi / 4
plt.scatter([x,],[3 * np.sin(x),], 30, color ='blue')
plt.annotate(r'$(3\sin(\frac{3\pi}{4}),\frac{3}{\sqrt{2}})$',
         xy=(x, 3 * np.sin(x)), 
         xycoords='data',
         xytext=(+20, +20), 
         textcoords='offset points', 
         fontsize=16,
         arrowprops=dict(facecolor='blue'))
plt.plot(X, F1, label="$sin(x)$")
plt.plot(X, F2, label="$3 sin(x)$")
plt.legend(loc='lower left')
plt.show()