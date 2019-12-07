# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:02:59 2019

@author: huyn
"""

#750. Number Of Corner Rectangles
#Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
#
#A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
# Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.
from typing import List
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # count corners
        if len(grid) <=1:
            return 0
        row = len(grid)
        col = len(grid[0])
        res = 0
        d = {}
        for i in range(col-1):
            for j in range(i+1,col):
                if grid[0][i] and grid[0][j]:
                    d[(i,j)] = 1
        for r in range(1,row):
            for i in range(col-1):
                for j in range(i+1,col):
                    if grid[r][i] and grid[r][j]:
                        if (i,j) in d:
                            d[(i,j)] +=1
                        else:
                            d[(i,j)] = 1
        for key in d:
            val = d[key]
            res += val*(val-1)//2
        return res