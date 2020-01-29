# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:42:32 2020

@author: huyn
"""
#1287. Element Appearing More Than 25% In Sorted Array
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        currentCount = 0
        num = None
        count = 1
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                count+=1
            else:
                if currentCount<count:
                    currentCount = count
                    num = arr[i]
                count = 1
        if currentCount<count:
            return arr[-1]
        return num