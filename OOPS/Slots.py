# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 23:13:11 2016

@author: RITURAJ
"""

class S(object):
    __slots__ = ['val']
    def __init__(self, v):
        self.val = v
        
x = S(42)
print(x.val)
#print(x.__dict__)
x.new = "not possible"

