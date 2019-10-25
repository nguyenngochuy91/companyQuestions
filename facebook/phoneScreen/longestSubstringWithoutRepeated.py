# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:15:52 2019

@author: huyn
"""
def lengthOfLongestSubstring(s: str) -> int:
    mySet = set()
    start,stop = 0,0
    maxLength =0
    currentLength = 0
    while stop<len(s):
        letter = s[stop]
        if letter not in mySet:
            currentLength+=1
            mySet.add(letter)
        else:
            maxLength = max(maxLength,currentLength)
            while start<stop and s[start]!=letter:
                lastLetter = s[start]
                currentLength-=1
                mySet.remove(lastLetter)
                start+=1
            if s[start]==letter:
                mySet.remove(letter)
                currentLength-=1
                start+=1
            mySet.add(letter)
            currentLength+=1
        stop+=1
    return max(maxLength,currentLength)