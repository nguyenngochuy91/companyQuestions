# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:25:41 2019

@author: huyn
"""
#An array is monotonic if it is either monotone increasing or monotone decreasing.
#
#An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone 
#decreasing if for all i <= j, A[i] >= A[j].
#
#Return true if and only if the given array A is monotonic.
def isMonotonic(A: list[int]) -> bool:
    if len(A)==1:
        return True
    v = A[1]-A[0]
    if v ==0:
        current = 0
    else:
        current = abs(v)/v
    for i in range(1,len(A)-1):
        val = A[i+1]-A[i]
        if val==0:
            continue
        val = abs(val)/val
        if val!=current and current!=0:
            return False
        elif current == 0:
            current = val
    return True
    