# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 00:44:38 2019

@author: huyn
"""

#67. Add Binary
def addBinary(self, a: str, b: str) -> str:
    remainder = 0
    res = []
    i,j =len(a)-1,len(b)-1
    while i>=0 and j>=0:
        valA = int(a[i])
        valB = int(b[j])
        if valA+valB+remainder==3:
            res.append("1")
            remainder = 1
        elif valA+valB+remainder ==2:
            res.append("0")
            remainder = 1
        else:
            res.append(str(valA+valB+remainder))
            remainder = 0
        i-=1
        j-=1
    while i>=0:
        valA = int(a[i])
        if valA+remainder==2:
            res.append("0")
            remainder = 1   
        else:
            res.append(str(valA+remainder))
            remainder = 0
        i-=1
    while j>=0:
        valB = int(b[j])
        if valB+remainder==2:
            res.append("0")
            remainder = 1   
        else:
            res.append(str(valB+remainder))
            remainder = 0
        j-=1

    if remainder:
        res.append("1")
    return "".join(res[::-1])