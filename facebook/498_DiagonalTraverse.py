# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:46:17 2019

@author: huyn
"""

#498. Diagonal Traverse
#Given a matrix of M x N elements (M rows, N columns), return all elements of the 
#matrix in diagonal order as shown in the below image.
from typing import List
def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    row = len(matrix)
    if row ==0 or matrix== [[]]:
        return []
    col = len(matrix[0])
    res = []
    currentRow,currentCol = 0,0
    for time in range(col*row):
        res.append(matrix[currentRow][currentCol])
        
    return res

matrix=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10,11,12]
]
print (findDiagonalOrder(matrix))