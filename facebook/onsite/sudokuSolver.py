# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 05:08:47 2019

@author: Huy Nguyen
"""
"""
37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'."""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # search for all blank
        blanks = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    blanks.append((i,j))
        possibles = {}
        for row,col in blanks:
            # we find the choices we can have
            unavailables = set()
            for j in range(9):
                if board[row][j] != ".":
                    unavailables.add(board[row][j])

            for i in range(9):
                if board[i][col] != ".":
                    unavailables.add(board[i][col])

            # find the square it belongs to, and base on the first starting coordinate
            startRow,startCol = (row//3)*3,(col //3)*3
            for i in range(3):
                for j in range(3):
                    currentRow,currentCol = startRow + i, startCol +j
#                    if row == 0 and col ==5:
#                        print (currentRow,currentCol)
                    if board[currentRow][currentCol] != ".":
#                        if row == 0 and col ==5:
#                            print (board[currentRow][currentCol])
                        unavailables.add(board[currentRow][currentCol])
#            if row == 0 and col ==5:
#                print (unavailables)
            possibles[(row,col)] = set("123456789")-unavailables

#        for x,y in blanks:
#            print (x,y,possibles[(x,y)])
        # we have an isValid to check a given state of board is valid
        def isValid():
#            print (board)
            # check row
            for i in range(9):
                checkRow = set()
                for j in range(9):
                    val = board[i][j]
                    if val != ".":
                        if val in checkRow:
#                            print ("row:",i)
                            return False
                        checkRow.add(val)
            # check col
            for j in range(9):
                checkCol = set()
                for i in range(9):
                    val = board[i][j]
                    if val != ".":
                        if val in checkCol:
#                            print ("col:",i)
                            return False
                        checkCol.add(val) 
            for i in range(3):
                for j in range(3):
                    startRow,startCol = i*3,j*3
                    checkSquare = set()
                    for addRow in range(3):
                        for addCol in range(3):
                            val = board[startRow+addRow][startCol+addCol]
                            if val != ".":
                                if val in checkSquare:
#                                    print ("square:",startRow,startCol)
                                    return False
                                checkSquare.add(val) 
            return True
        # backtracking dfs part to go through our possibles and fill
        def dfs(index):
            if index == len(blanks):
                return True
            else:
                row,col = blanks[index]
                choices = possibles[(row,col)]
                for choice in choices:
                    board[row][col] = choice
#                    print ("checking row,col",row,col)
                    if isValid():
                        check = dfs(index+1)
                        if check:
                            return True
                    board[row][col] = "." # actually does not need even this part because the next item in for replace it
                return False
        isSolved = dfs(0)
        return isSolved
board =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
solution = Solution()
print (solution.solveSudoku(board))
print (board)