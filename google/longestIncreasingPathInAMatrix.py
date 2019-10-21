# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:35:01 2019

@author: huyn
"""

#Longest Increasing Path in a Matrix
#Given an integer matrix, find the length of the longest increasing path.
#
#From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
from typing import List
nums = [  [9,9,4],  [6,6,8],  [2,1,1]] 
nums = [  [3,4,5],  [3,2,6],  [2,2,1]] 
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    visited = set()
    row = len(matrix)
    col = len(matrix[0])
    def dfs(currentRow,currentCol,row,col):
        
    return
def isNotFinal(currentRow,currentCol,row,col,visited):
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    check = 
    for addX,addY in directions:
        X,Y = currentRow+addX, currentCol + Y
        if X >=0 and Y >= 0 and X <row and Y  < col:
            if (X,Y) not in visited:
                