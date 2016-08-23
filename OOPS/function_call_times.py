# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:24:44 2016

@author: RITURAJ
"""

def call_counter(fn):
    def helper(*args, **kwargs):
        helper.calls+=1
        return fn(*args, **kwargs)
    helper.calls = 0
    helper.__name__ = fn.__name__
    return helper
    
@call_counter
def f():
    pass
print(f.calls)
for _ in range (10):
    f()
print(f.calls)