# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:29:25 2016

@author: RITURAJ
"""

import numpy as np
import matplotlib.pyplot as plt
'''
ax = plt.gca()
ax.plot([1, 2, 3, 4])
ax.legend(['A simple line (I am legend)'])
'''

'''
x = np.linspace(0, 25, 10000)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, '-b', label='sine')
plt.plot(x, y2, '-r', label='cosine')
plt.legend(loc='upper left')
plt.ylim(-1.5, 2.0)
plt.show()
'''

X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
F1 = np.sin(0.5*X)
F2 = -3 * np.cos(0.8*X)
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
plt.plot(X, F1, label="$sin(0.5x)$")
plt.plot(X, F2, label="$-3 cos(0.8x)$")
plt.legend(loc='best')
plt.show()