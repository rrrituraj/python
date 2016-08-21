# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 01:38:10 2016

@author: RITURAJ
"""
class Employee:
    def __init__(self , first , last):
        self.first = first
        self.last = last
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first , self.last)
    #getter    
    @property
    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    #Setter
    @fullname.setter
    def fullname(self , name):
        first , last = name.split(' ')
        self.first = first
        self.last = last
    #deleter
    @fullname.deleter
    def fullname(self):
        print('deleting Name')
        self.first = None
        self.last = None

emp_l = Employee('Rituraj','Gupta')
print(emp_l.fullname + ' \'from Rituraj Gupta\'')
emp_l.fullname = 'Kaju Gupta'
print(emp_l.first)
print(emp_l.email)
print(emp_l.fullname + ' \'from Kaju Gupta\'')
del emp_l.fullname
print(emp_l.fullname + ' \'after deleting\'')
