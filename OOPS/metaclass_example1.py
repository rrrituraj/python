# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:12:52 2016

@author: RITURAJ
"""

def the_answer(self , *args):
    return 42

class EssentialAnswers(type):
    def __init__(cls, clsname, superclasses, attributedict):
        cls.the_answer= the_answer
        
class philosophi1(metaclass=EssentialAnswers):
    pass

class philosophi2(metaclass= EssentialAnswers):
    pass

class philosophi3(metaclass=EssentialAnswers):
    pass

plato = philosophi1()
print(plato.the_answer())

kant = philosophi2()
print(kant.the_answer())

ramdev = philosophi3()
print(ramdev.the_answer())
