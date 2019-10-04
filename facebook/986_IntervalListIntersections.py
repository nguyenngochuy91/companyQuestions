# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 02:02:59 2019

@author: huyn
"""
from typing import List
#Given 2 disjoint sets of intervals, find the intersections
#986. Interval List Intersections
#Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
#Return the intersection of these two interval lists.
#
#(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers 
#x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers
# that is either empty, or can be represented as a closed interval.  
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
def intervalIntersection( A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    res = []
    i,j = 0,0
    while i<len(A) and j<len(B):
        startA,stopA = A[i]
        startB,stopB = B[j]
        low = max(startA,startB)
        high = min(stopA,stopB)
        if low<=high:
            res.append([low,high])

        if stopA>stopB:
            j+=1
        else:
            i+=1
    return res
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print (intervalIntersection(A,B))