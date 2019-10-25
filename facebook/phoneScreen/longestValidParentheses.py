# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:48:40 2019

@author: Huy Nguyen
"""
import random
#longest valid parenthheses substring
def findLongestValid(string):
    left = 0
    d= {0:[-1]}
    maxLength = 0
    for index,item in enumerate(string):
        if item == "(":
            left+=1
            if left in d:
                firstIndex = d[left].append(index)
            else:
                d[left]= [index]
        else:
            if left >0:
                left-=1
                if left in d:
                    firstIndex = d[left][0]
                    # we have to check whether we have a "(" before our index 
                    if left ==0:
                        maxLength= max(maxLength,index-firstIndex)
                    else:
                        # ()((())
                        # we have to minus the index where we have a positive (
                        lastIndex = d[left][-1]
                        maxLength= max(maxLength,index-lastIndex)
                else:
                    d[left]= [index]
            else:
                d= {0:[index]}
#        print (index,item,d,maxLength)
                
        
    return maxLength
def generateString(n):
    string = ""
    for i in range(n):
        string+=random.choice("()")[0]
    return string

#string = "()()(((())"
#print (findLongestValid(string))
#string = "(()"
#print (findLongestValid(string))
string = "())()((())"
#print (string)
print (findLongestValid(string))