# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:54:45 2016

@author: RITURAJ
"""

l = ["Python", "Java", "C++", "Perl"]
print l
print str(l)
print repr(l)
import datetime
today = datetime.datetime.now()
str_s = str(today)
repr_s = repr(today)
print today
print str_s
#today == eval(str_s) #will throgh SyntaxError: invalid token
print today == eval(repr_s)