# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:46:44 2019

@author: huyn
"""
"""
1187. Make Array Strictly Increasing
Given two integer arrays arr1 and arr2, return the minimum number of operations 
(possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length 
and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.
"""

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
solution = Solution()
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
print (solution.makeArrayIncreasing(arr1,arr2))
arr1 = [1,5,3,6,7]
arr2 = [4,3,1]
print (solution.makeArrayIncreasing(arr1,arr2))
arr1 = [1,5,3,6,7]
arr2 = [1,6,3,3]
print (solution.makeArrayIncreasing(arr1,arr2))