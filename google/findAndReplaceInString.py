# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:32:25 2019

@author: huyn
"""

#Find And Replace in String
#To some string S, we will perform some replacement operations that replace groups of letters with 
#new ones (not necessarily the same size).
#
#Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  
#The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  
#If not, we do nothing.
#
#For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" 
#starts at position 2 in the original string S, we will replace it with "ffff".
#
#Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as 
#another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the 
#original string S[2] = 'c', which doesn't match x[0] = 'e'.
#
#All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: 
#    for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
from typing import List
def findReplaceString(S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
    s= list(S)
    for i in range(len(indexes)):
        index,source,target = indexes[i],sources[i],targets[i]
        check = True
        for j in range(len(source)):
            if s[index+j]!=source[j]:
                check = False
                break
        if check:
            s[index] = target
            for j in range(1,len(source)):
                s[index+j] = ""
    return "".join(s)
    return