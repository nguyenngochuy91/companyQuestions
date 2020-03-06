# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:51:19 2020

@author: huyn
"""

class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        s = set()
        maxLength = ""
        for i in range(len(S)):
            for j in range(i,len(S)):
                string = S[i:j+1]
                if string not in s:
                    s.add(string)
                else:
                    if len(string)>len(maxLength):
                        maxLength = string
        return len(maxLength)