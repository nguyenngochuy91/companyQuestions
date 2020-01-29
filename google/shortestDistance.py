# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:56:50 2020

@author: huyn
"""

#243. Shortest Word Distance
from typing import List
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        res = float("inf")
        start = None
        stop = None
        for i in range(len(words)):
            if words[i] == word1:
                start = i
            if words[i] == word2:
                stop = i
            if start!= None and stop != None:
                res = min(res,abs(stop-start))
        return res