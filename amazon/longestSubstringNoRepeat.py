# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:31:40 2020

@author: huyn
"""

#Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        d = {}
        maxLength = 0
        for index, letter in enumerate(s):
            while letter in d:
                firstLetter = s[i]
                d[firstLetter]-=1
                if d[firstLetter] == 0:
                    d.pop(firstLetter)
                i+=1
            d[letter] = 1
            maxLength = max(maxLength,len(d))
        return maxLength