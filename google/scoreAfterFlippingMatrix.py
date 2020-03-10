# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:10:00 2020

@author: huyn
"""

#861. Score After Flipping Matrix
from typing import List
class Solution(object):
    def matrixScore(self, A):
        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans