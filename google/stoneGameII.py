#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:54:20 2020

@author: huynguyen
"""


# 1140. Stone Game II
# Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, 
# and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. 
#  Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {} 
        def dfs(index,M):
            if index+2*M>=len(piles):
                return sum(piles[index:])
            else:
                if (index,M) in dp:
                    return dp[(index,M)]
                else:
                    val = 0
                    s = sum(piles[index:])
                    for i in range(1,2*M):
                        val = max(val,sum(piles[index:index+i])+s-dfs(index+i,max(M,i)))
                    dp[(index,M)] = val
                    return val
        dfs(0,1)
        print (dp)
        return dp[(0,1)]