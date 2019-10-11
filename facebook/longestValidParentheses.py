# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:48:40 2019

@author: Huy Nguyen
"""
import random
#longest valid parenthheses substring
def findLongestValid(string):
    return
def generateString(n):
    string = ""
    for i in range(n):
        string+=random.choices("()")[0]
    return string

string = "()()(((())"
print (findLongestValid(string))
