# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:45:56 2019

@author: huyn
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        res = []
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        index = 0
        start  = [0,0]
        for i in range(row*col):
            x,y = start
            res.append(matrix[x][y])
            matrix[x][y] = 0
            # try to see we can walk in same direction
            potentialX,potentialY = x+direction[index][0], y+direction[index][1]
            if potentialX>=0 and potentialX <row and potentialY>=0 and potentialY <col:
                if matrix[potentialX][potentialY] != 0:
                    start = potentialX,potentialY
                    continue
            # if potential is not good, change direction
            index = (index+1)%4
            start = x+direction[index][0], y+direction[index][1]
        return res