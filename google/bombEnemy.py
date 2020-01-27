#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:58:37 2020

@author: huynguyen
"""

from typing import List
# 361 bomb enemy
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        matrix = [[0]* col for i in range(row)]
        # for each grid, find the number of enemy it can kill on the same row
        for i in range(row):
            # left traverse
            leftWall = 0
            numEnemy = 0
            for j in range(col):
                
                if grid[i][j] == "W":
                    rightWall = j
                    for cell in range(leftWall,rightWall):
                        if grid[i][cell] =="0":
                            matrix[i][cell]+=numEnemy
                    leftWall = j
                    numEnemy = 0
                elif grid[i][j] == "E":
                    numEnemy +=1
            for cell in range(leftWall,col):
                if grid[i][cell] =="0":
                    matrix[i][cell]+=numEnemy    
            
 
        for j in range(col):
            # left traverse
            topWall = 0
            numEnemy = 0
            for i in range(row):
                
                if grid[i][j] == "W":
                    botWall = i
                    for cell in range(topWall,botWall):
                        if grid[cell][j] =="0":
                            matrix[cell][j]+=numEnemy
                    topWall = i
                    numEnemy = 0
                elif grid[i][j] == "E":
                    numEnemy +=1
            for cell in range(topWall,row):
                if grid[cell][j] =="0":
                    matrix[cell][j]+=numEnemy  
        currentMax = 0
        for i in range(row):
            for j in range(col):
                currentMax = max(currentMax,matrix[i][j])
        print (matrix)
        return currentMax
# grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# solution = Solution()
# print (solution.maxKilledEnemies(grid))
# grid = [["0","W","E","0","0","E","0","W","E","W","0","E"]]
# solution = Solution()

# print (solution.maxKilledEnemies(grid))