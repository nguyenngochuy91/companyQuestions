# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:30:37 2019

@author: huyn
"""
"""
659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it 
into 1 or more subsequences such that each subsequence consists 
of consecutive integers and has length at least 3.
"""


from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        