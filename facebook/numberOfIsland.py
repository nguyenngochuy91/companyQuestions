# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:56:22 2019

@author: huyn
"""
from collections import deque
#Count all the islands in a binary matrix
#You are given a 2D binary matrix as an input. You want to return the number of 
#islands in the binary matrix. You can think of the 0's as the ocean and the 1's as land. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally 
#or vertically. You goal is to return the correct number of islands.
def countIslandDFS(grid):
    if not grid:
        return 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for i in range(row)]
    numIsland = 0  # count the number of island
    # we dfs through our island, and add node to visited 
    def dfs(currentRow,currentCol,row,col):
        # set our directions (4 direction)
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for addRow,addCol in directions:
            newRow,newCol = currentRow+addRow,currentCol+addCol
            # we check if newRow,newCol valid and has not been visited 
            if newRow>=0 and newCol>=0 and newCol<col and newRow<row:
                if not visited[newRow][newCol] and grid[newRow][newCol]=="1":
                    # add to visited
                    visited[newRow][newCol] = True
                    dfs(newRow,newCol,row,col)
    for i in range(row):
        for j in range(col):
            if grid[i][j]=="1" and not visited[i][j]:
                # increment island
                numIsland+=1
                visited[i][j]= True
                dfs(i,j,row,col)
    return numIsland
matrix = [[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[1, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[1, 0, 1, 0, 1]]
#print (countIslandDFS(matrix))

def countIslandBFS(matrix):
    row       = len(matrix)
    col       = len(matrix[0])
    visited   = [[False]*col for i in range(row)]
    numIsland = 0
    for r in range(row):
        for c in range(col):
            if matrix[r][c] and not visited[r][c]:
                numIsland+=1
                visited[r][c]=True
                queue = deque([[r,c]])
                while queue:
                    size = len(queue)
                    for i in range(size):
                        currentRow,currentCol = queue.popleft()
                        direction = [[0,1],[1,0],[0,-1],[-1,0]]
                        for addRow,addCol in direction:
                            newRow,newCol= currentRow+addRow,currentCol+addCol
                            if newRow>=0 and newCol>=0 and newRow<row and newCol<col and not visited[newRow][newCol] and matrix[newRow][newCol]:
                                visited[newRow][newCol] = True
                                queue.append([newRow,newCol])
    return numIsland
#print (countIslandBFS(matrix))