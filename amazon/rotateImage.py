# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:44:05 2020

@author: huyn
"""
from typing import List
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        start,stop = 0, len(m)-1
        for row in range(n//2):
            for col in range(start,stop):
                # we swap all 4
                m[row][col],m[col][n-1-row],m[n-1-row][n-1-col],m[n-1-col][row] = m[n-1-col][row],m[row][col],m[col][n-1-row],m[n-1-row][n-1-col]
            start +=1
            stop -=1