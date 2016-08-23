# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:22:48 2016

@author: RITURAJ
"""

def the_answer(self , *args):
    return 42
    
#manager function
def augument_function(cls):
    cls.the_answer = the_answer
    return cls
 #class 1   
class philospher1:
    pass
augument_function(philospher1)
#class 2
class philospher2:
    pass
augument_function(philospher2)
#class3
class philospher3:
    pass
augument_function(philospher3)
#calling classes
plato = philospher1()
print(plato.the_answer())

kant = philospher2()
print(kant.the_answer())

ramdev = philospher3()
print(ramdev.the_answer())

print('another way to implement manager function is by this way')
@augument_function
class philospher4:
    pass
@augument_function
class philospher5:
    pass

plato1 = philospher4()
print(plato1.the_answer())

kant1 = philospher5()
print(kant1.the_answer())
