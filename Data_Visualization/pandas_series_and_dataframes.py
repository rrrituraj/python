# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:43:31 2016

@author: RITURAJ
"""
'''remove multicomment from each block one by one and enjoy'''
import numpy as np
from pandas import Series, DataFrame
'''
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
print(obj)
print('#calling reindexing on this object')
obj2 = obj.reindex(['a','b','c','d','e'], fill_value = 0)
print(obj2)
obj3 = Series(['blue','purple','yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))
'''

'''
frame = DataFrame(np.arange(9).reshape(3, 3), index=['a','c','d'],
                  columns=['ohio','texas','california'])
print(frame)
print("\nreindexing by ['a','b','c','d'], method='ffill\n")                  
frame2 = frame.reindex(['a','b','c','d'], method='ffill')
print(frame2)
print("\nreindexing by columns=['texas','utah','california']\n")                             
frame3 = frame.reindex(columns=['texas','utah','california'])
print(frame3)
'''
"""
print("\ndroping entries from an axis")
obj = Series(np.arange(5), index=['a','b','c','d','e'])
print(obj)
\"""print("\n")
new_obj = obj.drop('c')
print(new_obj)\"""
print(obj['b'])
print(obj[1])
print("slicing and assigning them to 5")
obj['b':'c']=5
print(obj)
"""
print("\noperation between dataframe and series")
frame = DataFrame(np.arange(12.).reshape(4, 3), columns=list('bde'),
                  index=['utah','ohio','texas','oregon'])
print(frame)                  
series = frame.ix[0]                  
print(series)
print(frame - series)
