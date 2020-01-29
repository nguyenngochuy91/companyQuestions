# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:06:06 2020

@author: huyn
"""

#293. Flip Game
from typing import List
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                string = s[:i]+"--"+s[i+2:]
                res.append(string)
        return res