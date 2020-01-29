# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:05:34 2020

@author: huyn
"""
#1099. Two Sum Less Than K
from typing import List
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i, j = 0 ,len(A)-1
        res = -1
        while i<j:
            num = A[i]+A[j]
            if num <K:
                res = max(num,res)
                i+=1
            else:
                j-=1
        return res