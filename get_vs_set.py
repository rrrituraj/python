# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:44:05 2016

@author: RITURAJ

"""
class Robot(name , by):
    '''def __init__(self , name=None , build_year = None):
        self.name = name
        self.build_year = build_year'''
    def say_hi(self):
        if self.name:
            print 'hi, I am ' , self.name
        else:
            print("Hi, I am a robot without a name")
    def set_name(self , name):
        self.name = name
    def get_name(self):
        return self.name
    '''Adding Build Year using get and set functions'''
    def set_build_year(self , by):
        self.build_year = by
    def get_build_year(self):
        return self.build_year

x = Robot("Rituraj", 2008)
y = Robot()
y.set_name(x.get_name())
y.set_build_year(x.get_build_year())
print(x.get_name(), x.get_build_year())
print(y.get_name(), y.get_build_year())