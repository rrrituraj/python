# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:57:10 2016

@author: RITURAJ
"""

class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
x = Robot()
x.say_hi()
y = Robot("Rituraj")
y.say_hi()