# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:19:51 2016

@author: RITURAJ
"""

'''
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))
G = gridspec.GridSpec(3,3)
axes1 = plt.subplot(G[0,:])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)
axes_2 = plt.subplot(G[1, :2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)
axes_3 = plt.subplot(G[1:, -1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)
axes_4 = plt.subplot(G[-1, 0])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)
axes_5 = plt.subplot(G[-1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=.5)
plt.show()
'''

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(6, 4))
G = gridspec.GridSpec(3, 3)
X = np.linspace(0, 2 * np.pi, 50, endpoint=True)
F1 = 2.8 * np.cos(X)
F2 = 5 * np.sin(X)
F3 = 0.3 * np.sin(X)
axes_1 = plt.subplot(G[0, :])
axes_1.plot(X, F1, 'r-', X, F2)
axes_2 = plt.subplot(G[1, :-1])
axes_2.plot(X, F3)
axes_3 = plt.subplot(G[1:, -1])
axes_3.plot([1,2,3,4], [1,10,100,1000], 'b-')
axes_4 = plt.subplot(G[-1, 0])
axes_4.plot([1,2,3,4], [47, 11, 42, 60], 'r-')
axes_5 = plt.subplot(G[-1, -2])
axes_5.plot([1,2,3,4], [7, 5, 4, 3.8])
plt.tight_layout()
plt.show()