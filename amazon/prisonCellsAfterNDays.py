# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:52:39 2019

@author: huyn
"""
"""
957. Prison Cells After N Days"""
class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        newCells = []
        d = []
        for i in range(N):
            if cells not in d:
                d.append(cells)
            else:
                start = d.index(cells)
                d = d[start:]
                return d[(N-i)%(len(d))]
            newCells.append(0)
            for i in range(1,7):
                val = cells[i-1]*cells[i+1] + (1-cells[i-1])*(1-cells[i+1])
                newCells.append(val)
            newCells.append(0)
            cells = newCells
            newCells = []
        return cells
        