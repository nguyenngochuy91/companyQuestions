# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:32:39 2019

@author: huyn
"""

#Rotate Image
#You are given an n x n 2D matrix representing an image.
#
#Rotate the image by 90 degrees (clockwise).
#
#Note:
#
#You have to rotate the image in-place, which means you have to modify the input
# 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
from typing import List
def rotate(m: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(m)
    start,stop = 0, len(m)-1
    for row in range(n//2):
        for col in range(start,stop):
            # we swap all 4
            m[row][col],m[col][n-1-row],m[n-1-row][n-1-col],m[n-1-col][n-1-row] = m[n-1-col][n-1-row],m[row][col],m[col][n-1-row],m[n-1-row][n-1-col]
        start +=1
        stop -=1
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
print (matrix)
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(matrix)
print (matrix)