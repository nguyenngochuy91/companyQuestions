# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:49:16 2019

@author: huyn
"""
def romanToInt(s: str) -> int:
    d= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if not s:
        return 0
    current = d[s[0]]
    accumulate = d[s[0]]
    for i in range(len(s)-1):
        v = d[s[i+1]]
        if v>current:
            accumulate= accumulate-current+v-current
        else:
            accumulate+=v
        current=v
    return accumulate