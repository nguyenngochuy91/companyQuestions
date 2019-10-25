# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:38:29 2019

@author: huyn
"""

#1004. Max Consecutive Ones III
#Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
#Return the length of the longest (contiguous) subarray that contains only 1s. 
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        