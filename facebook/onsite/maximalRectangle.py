# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:17:36 2019

@author: huyn
"""
"""
85. Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area."""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
input = [["1","0","1","0","0"],  ["1","0","1","1","1"],  ["1","1","1","1","1"], ["1","0","0","1","0"]]