# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:23:13 2016

@author: RITURAJ
"""
#observing the order
class A(object):
    def m(self):
           print('m of B called')

class B(A):
    pass
        
class C(A):
    def m(self):
        print('m of C called')

class D(C , B):
    pass

x = D()
print(x.m())
#observing method
class A():
    def m(self):
        print('m of A called')

class B():
    def m(self):
        print('m of B called')    
        
class C():
    def m(self):
        print('m of C called')

class D(C , B):
    def m(self):
        print('m of D called')
        
x = D()
print(B.m(x)) 

#one way to solve the diamond problem is to use super() method
class A:
    def m(self):
        print("m of A called")
class B(A):
    def m(self):
        print("m of B called")
        super().m()
class C(A):
    def m(self):
        print("m of C called")
        super().m()
class D(B,C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
print(x.m())
#mro() method used to create linearization list
print(D.mro())