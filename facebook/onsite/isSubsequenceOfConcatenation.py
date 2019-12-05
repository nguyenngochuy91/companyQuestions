# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:45:26 2019

@author: Huy Nguyen
"""
"""
Given two strings a and b, find if a can be subsequence of b or by concatenating b.
Input:
a = jaja
b = baj
Output:
True
Explanation:
baj | baj | baj
"baj" can be concatenated three times to get "jaja". 

Follow-up:
Find the minimum number of concatenations. Optimize it further from O(n * m)"""

def isSubsequence(a,b):
    return