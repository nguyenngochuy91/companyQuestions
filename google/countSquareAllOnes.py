# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:10:13 2019

@author: huyn
"""

#1277. Count Square Submatrices with All Ones
#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        return