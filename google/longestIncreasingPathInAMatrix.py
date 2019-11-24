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
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        self.length = 0
        dp = {}
        def dfs(x,y,lastNum):
            temp = [(1,0),(0,1),(-1,0),(0,-1)]
#            print (22,x,y)
            res = 1
            for a,b in temp:
                X,Y = a+x,b+y
                if X>=0 and Y>=0 and X<row and Y<col:
                    if matrix[X][Y]!=-1:
                        val = matrix[X][Y]
                        if val > lastNum:
                            if (X,Y) in dp:
                                res = max(res,1+dp[(X,Y)])
                            else:
                                matrix[X][Y] = -1
                                res = max(dfs(X,Y,val)+1,res)
                                matrix[X][Y] = val
            dp[(x,y)] = res
#            print (37,res,x,y)
            self.length = max(self.length,res)
            return res
        for r in range(row):
            for c in range(col):
#                print (40,r,c)
                val = matrix[r][c]
                matrix[r][c] = -1
                dfs(r,c,val)
                matrix[r][c] = val
#        print (dp,matrix)
        return self.length
        

solution = Solution()

nums = [  [9,9,4],  [6,6,8],  [2,1,1]] 
print (solution.longestIncreasingPath(nums))
nums = [  [3,4,5],  [3,2,6],  [2,2,1]] 
print (solution.longestIncreasingPath(nums))