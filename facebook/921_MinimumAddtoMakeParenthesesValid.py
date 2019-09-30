# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:47:22 2019

@author: Huy Nguyen
"""
import random
#921. Minimum Add to Make Parentheses Valid
#Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so t
#hat the resulting parentheses string is valid.
#
#Formally, a parentheses string is valid if and only if:
#
#It is the empty string, or
#It can be written as AB (A concatenated with B), where A and B are valid strings, or
#It can be written as (A), where A is a valid string.
#Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
def minAddToMakeValid(self, S: str) -> int:
    countL = 0
    res = 0
    for item in S:
        if item =="(":
            countL+=1
        else:
            if countL==0:
                res+=1
            else:
                countL-=1
    return res+countL
def generateString(n):
    string = ""
    for i in range(n):
        string+=random.choices("()")[0]
    return string
string =generateString(100)
print (string)
print (minAddToMakeValid(string))