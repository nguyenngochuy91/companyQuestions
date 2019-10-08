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
    res = [matrix[0][0]]
    currentRow,currentCol = 0,0
    rightDown = [(0,1),(1,0)]
    diagonal  = [(1,-1),(-1,1)]
    isRightDown = True
    indexR    = 0
    indexD    = 0
    count = 0
    while count<row*col-1:
        if isRightDown:
            # we try both at indexR and indexR+1 to see which one works first
            x,y = rightDown[indexR]
            if isValid(row,col,currentRow+x,currentCol+y):
                currentRow,currentCol= currentRow+x,currentCol+y
                res.append(matrix[currentRow][currentCol])
                count+=1
            else:
                x,y = rightDown[(indexR+1)%2]
                currentRow,currentCol= currentRow+x,currentCol+y
                res.append(matrix[currentRow][currentCol])
                count+=1
            indexR = (indexR+1)%2
            isRightDown = False
            
        else:
            x,y = diagonal[indexD]
            if isValid(row,col,currentRow+x,currentCol+y):
                currentRow,currentCol= currentRow+x,currentCol+y
                res.append(matrix[currentRow][currentCol])
                count+=1
            else: # this means we have change isRIghtDown to True
                isRightDown= True
                # we also have to increment indexD
                indexD = (indexD+1)%2
    return res
def isValid(row,col,x,y):
    return x>=0 and y>=0 and x<row and y<col
matrix=[
 [ 1, 2  ],
 [ 4, 5  ],
 [ 7, 8 ],
 [10,11]
]
#print (findDiagonalOrder(matrix))
    
#Given a matrix, return all elements of the matrix in antidiagonal order as shown in the below image.
def antiDiagonalOrder(matrix):
    row = len(matrix)
    col = len(matrix[0])
    res = []
    coordinate = []
    for c in range(col):
        res.append([matrix[0][c]])
        coordinate.append([0,c])
    for r in range(1,row):
        res.append([matrix[r][col-1]])
        coordinate.append([r,col-1])
#    print (res,coordinate)
    for i in range(len(coordinate)):
        currentRow,currentCol = coordinate[i]
        count = 0
        while True:
            nextRow,nextCol = currentRow+1,currentCol-1
            if isValid(row,col,nextRow,nextCol):
                currentRow,currentCol= nextRow,nextCol
                res[i].append(matrix[currentRow][currentCol])
                count+=1
                if count ==10:
                    break
            else:
                break
#        print (item)
    return res

#print (antiDiagonalOrder(matrix))