# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:02:17 2019

@author: huyn
"""

#Longest Substring with At Most Two Distinct Characters
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    myMax = 0
    start, stop = 0, 0
    d = {}
    while stop<len(s):
        currentLetter = s[stop]
        if currentLetter not in d:
            myMax = max(myMax,stop-start)
            while len(d)==2:
                first = s[start]
                d[first]-=1
                if d[first] == 0 :
                    d.pop(first)
                start  += 1
            d[currentLetter] = 0
        d[currentLetter] +=1
    stop += 1
    return max(myMax, stop -start)