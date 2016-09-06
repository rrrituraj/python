# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:30:04 2016

@author: RITURAJ
"""

import numpy as np
import matplotlib.pyplot as plt
xlist = np.linspace(-3.0, 3.0, 2000)
ylist = np.linspace(-3.0, 3.0, 2000)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
plt.figure()
cp = plt.contourf(X, Y, Z)
plt.colorbar(cp)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()