# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:30:58 2020

@author: huyn
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        d= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        current = d[s[0]]
        s = d[s[0]]
        for letter in s[1:]:
            currentVal = d[letter]
            if currentVal<= current:
                s+=currentVal
                current = currentVal
            else:
                s-=2*current
                s+=currentVal
                current = currentVal
        return s