# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 10:47:42 2016

@author: RITURAJ
"""

class Person:
    
    def __init__(self , first , last):
        self.firstname = first
        self.lastname = last
        
    '''def Name(self):
        return self.firstname + ' ' + self.lastname'''
        
    #better to use __str__ method
    def __str__(self):
        return self.firstname + ' ' + self.lastname

#inheritence
class Employee(Person):
    
    def __init__(self , first , last , staffnum):
        super().__init__(first , last)
        '''
        Or we can use 
        Person.__init__(self , first , last)
        '''
        self.staffnumber = staffnum
        
        '''
        We could have written
        "super(Employee, self).__init__(first, last, age)" 
        which still works in Python3 and is compatible with Python2.
        '''
    
    '''def GetEmployee(self):
        return self.Name() + "," + self.staffnumber'''
    #better to use __str__ method , here for child class
    def __str__(self):
         return super().__str__() + "," + self.staffnumber

x = Person("Rituaj", "Gupta")
y = Employee("Bittu", "Gupta", "1007")
print(x)
print(y)













