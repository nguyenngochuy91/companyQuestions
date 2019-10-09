# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:48:40 2019

@author: Huy Nguyen
"""
import random
#longest valid parenthheses substring
def findLongestValid(string):
    count =0
    length = 0
    leftParenthese = 0
    for item in string:
#        print (leftParenthese)
        if item =="(":
            leftParenthese+=1
        else:
            if leftParenthese:
                length+=2
                leftParenthese-=1
            else:
                count = max(count,length) 
                length=0
        
    return max(count,length)
def generateString(n):
    string = ""
    for i in range(n):
        string+=random.choices("()")[0]
    return string

string = "()()(((())"
print (findLongestValid(string))
