# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 00:53:02 2020

@author: huyn
"""
from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        d = {}
        def dfs(startRow,startCol,stopRow,stopCol):
            if startRow == stopRow and startCol == stopCol:
                
                node = Node(grid[startRow][startCol],True,None,None,None,None)
                return node
            else:
                node = Node(1,False,None,None,None,None)
                midRow = (startRow+stopRow)//2
                midCol = (startCol+stopCol) // 2
                topLeft = dfs(startRow,startCol,midRow,midCol)
                topRight = dfs(startRow,midCol+1,midRow,stopCol)
                bottomLeft = dfs(midRow+1,startCol,stopRow,midCol)
                bottomRight = dfs(midRow+1,midCol+1,stopRow,stopCol)
                node.topLeft = topLeft
                node.topRight = topRight
                node.bottomLeft = bottomLeft
                node.bottomRight = bottomRight
                return node
        return dfs(0,0,n-1,n-1)