# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:23:19 2019

@author: huyn
"""

#723. Candy Crush
#This question is about implementing a basic elimination algorithm for Candy Crush.
#
#Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] 
#represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. 
#The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:
#
#If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - 
#these positions become empty.
#After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these 
#candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
#After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
#If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
#You need to perform the above rules until the board becomes stable, then return the current board.

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        # function to find coordinate to set to 0
        row = len(board)
        col = len(board[0])
        coordinates = self.setToZero(board,row,col)
        while any(coordinates):
            for (r,c) in coordinates:
                board[r][c] = 0

            self.moveDown(board,row,col)

            coordinates = self.setToZero(board,row,col)
        return board
    def setToZero(self,board,row,col):

        coordinates = set()
        # check row to collapse 
        for r in range(row):
            count = 1
            for c in range(col-1):
                if board[r][c] == board[r][c+1] and board[r][c]!=0:

                    count+=1
                else:
                    if count>=3: # we can crush from i back to i-count

                        for i in range(count):
                            coordinates.add((r,c-i))
                    count = 1

            # now we check if count >=3 still
            if count>=3: # we can crush from i back to i-count

                for i in range(count):
                    coordinates.add((r,col-1-i))

        # check col to collapse
        for c in range(col):
            count = 1
            for r in range(row-1):
                if board[r][c] == board[r+1][c] and board[r][c]!=0:
                    count+=1
                else:
                    if count>=3: # we can crush from i back to i-count

                        for i in range(count):
                            item = (r-i,c)
                            coordinates.add(item)
                    count = 1
            # now we check if count >=3 still
            if count>=3: # we can crush from i back to i-count

                for i in range(count):
                    item = (row-1-i,c)
                    coordinates.add(item)
        return coordinates
    def moveDown(self,board,row,col):
        for c in range(col):
            count0 =0 
            for r in range(row-1,-1,-1):
                if board[r][c]:
                    if count0:
                        board[r+count0][c] = board[r][c]
                else:
                    count0+=1
            for r in range(count0):
                board[r][c] = 0
        
    
                        
            