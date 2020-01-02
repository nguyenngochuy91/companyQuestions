# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:12:52 2020

@author: huyn
"""

#Container With Most Water
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0 ,len(height)-1
        maxA = 0
        while i <j:
            maxA = max(maxA,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxA