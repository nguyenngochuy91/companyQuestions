# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:22:14 2019

@author: huyn
"""

#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
S = "ab#c"
T = "ad#c"
def backspaceCompare(S: str, T: str) -> bool:
    stackS = []
    for l in S:
        if l=="#":
            if stackS:
                stackS.pop()
        else:
            stackS.append(l)
    stackT = []
    for l in T:
        if l=="#":
            if stackT:
                stackT.pop()
        else:
            stackT.append(l)        
    return stackT == stackS