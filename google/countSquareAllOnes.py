# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:10:13 2019

@author: huyn
"""

#1277. Count Square Submatrices with All Ones
#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
import random
from typing import List
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        numMatrix = NumMatrix(mat)
        row = len(mat)
        col = len(mat[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j]:
                    m = min(i,j)
                    for k in range(m+1):
                        val = numMatrix.sumRegion(i-k,j-k,i,j)
                        if val**.5 == int(val**.5):
                            count+=1
                        else:
                            break
        return count
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
            for c in range(col):
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
                

for i in range(1):
    mat =[ [random.randint(0,1) for i in range(300)] for j in range(300)]
    print (mat)