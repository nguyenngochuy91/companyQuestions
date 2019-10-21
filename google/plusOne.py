# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:01:49 2019

@author: huyn
"""
#Plus One
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    remainder = 1
    for i in range(len(digits)-1,-1,-1):
        val = remainder +digits[i]
        digits[i]= val%10
        remainder = val//10
    if remainder:
        digits.insert(0,1)
    return digits