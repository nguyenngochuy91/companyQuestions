# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:35:20 2019

@author: huyn
"""

#370. Range Addition
#Assume you have an array of length n initialized with all 0's and are given k update operations.
#
#Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each 
#element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
#
#Return the modified array after all k operations were executed.
from typing import List
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0]*(length+1)
        for x,y,k in updates:
            arr[x]+=k
            arr[y+1]-=k
        for i in range(1,length):
            arr[i]+=arr[i-1]
        return arr[:length]