# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:12:51 2019

@author: huyn
"""
"""
1167. Minimum Cost to Connect Sticks
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y. 
You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way."""
from typing import List
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks:
            return 0
        if len(sticks)<=2:
            return sum(sticks)
        heapq.heapify(sticks)
        res = 0
        while len(sticks)!=1:
            first,second = heapq.heappop(sticks),heapq.heappop(sticks)
            val = first + second
            res += val
            heapq.heappush(sticks,val)
        return res