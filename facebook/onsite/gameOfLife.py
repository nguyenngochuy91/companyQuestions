# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:27:13 2019

@author: huyn
"""
"""
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a 
cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following 
four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
 The next state is created by applying the above rules simultaneously to every cell in the current state,
 where births and deaths occur simultaneously."""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        changes = set()
        row = len(board)
        col = len(board[0])
        
        for r in range(row):
            for c in range(col):
                count = 0
                potential = [(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1)]
                for x,y in potential:
                    X, Y = r + x, c + y
                    if X >= 0 and Y >= 0 and X < row and Y < col:
                        count += board[X][Y]
                if count < 2 and board[r][c]:
#                    print (45,r,c)
                    changes.add((r,c))
                if count > 3 and board[r][c]:
#                    print (48,r,c)
                    changes.add((r,c))
                if count == 3 and not board[r][c]:
#                    print (51,r,c)
                    changes.add((r,c))
        for r,c in changes:
            board[r][c] = 1 - board[r][c]
                        
board =[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution = Solution()
solution.gameOfLife(board)