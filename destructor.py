# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 00:36:24 2016

@author: RITURAJ
"""

class Robot:
    def __init__(self , name):
        print name , " has been created!"
    def __del__(self):
        print 'robot has been destroyed'
if __name__ == "__main__":
    x = Robot('Tik Tok')
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y