# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:41:51 2019

@author: huyn
"""

#861. Score After Flipping Matrix
#We have a two dimensional matrix A where each value is 0 or 1.
#
#A move consists of choosing any row or column, and toggling each value in that row or column: 
#    changing all 0s to 1s, and all 1s to 0s.
#
#After making any number of moves, every row of this matrix is interpreted as a binary number, 
#and the score of the matrix is the sum of these numbers.
#
#Return the highest possible score.

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        return