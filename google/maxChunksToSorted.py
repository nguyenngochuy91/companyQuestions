# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:51:47 2020

@author: huyn
"""
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        numBlock = 0
        start = 0
        stop = 0
        for index,num in enumerate(arr):
            stop = max(stop,num)
            if stop == index:
                numBlock +=1
        return numBlock