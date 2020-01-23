# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:42:27 2019

@author: huyn
"""

#304. Range Sum Query 2D - Immutable
#Given a 2D matrix matrix, find the sum of the elements inside the rectangle 
#defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
class NumMatrix:

    def __init__(self, matrix):
        self.arr = []
        if matrix==[[[]]] or not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        temp =[]
        for c in range(col):
            if temp:
                temp.append(temp[-1]+matrix[0][c])
            else:
                temp.append(matrix[0][c])
        self.arr.append(temp)
        for r in range(1,row):
            temp =[]
            for c in range(1,col):
                if not temp:
                    temp.append(matrix[r][c]+self.arr[r-1][c])
                else:
                    temp.append(temp[c-1]+self.arr[r-1][c]-self.arr[r-1][c-1]+matrix[r][c])
            self.arr.append(temp)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 ==0:
            if row1==0:
                return self.arr[row2][col2]
            else:
                return self.arr[row2][col2]- self.arr[row1-1][col2]
        else:
            if row1==0:
                return self.arr[row2][col2]-self.arr[row2][col1-1]
            else:
                return self.arr[row2][col2]- self.arr[row2][col1-1]-self.arr[row1-1][col2]+self.arr[row1-1][col1-1]      
        return

matrix = [[1,2,3],[4,5,6],[7,8,9]]
num = NumMatrix(matrix)