# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 03:21:44 2019

@author: huyn
"""

#Count subsets
#Input:
#
#Given an array A of
#-positive
#-sorted
#-no duplicate
#-integer
#
#A positive integer k
#
#Output:
#
#Count of all such subsets of A,
#Such that for any such subset S,
#Min(S) + Max(S) = k
#subset should contain atleast two elements
def countSubsets(array,k):
    d = {}
    # we map index to index
    count = 0
    for index,num in enumerate(array):
        d[num]= index
    for index1,num in enumerate(array):
        val = k-num
        index2 = d[val]# since they are unique, index2 and index1 only equal if 2*num == k
        if index1>index2:
            break
        if index1!=index2:
            size =index2-index1-1
            count+=2**(size)
    return count
array =[1,2,3,4,5]
k = 5
#print (countSubsets(array,k))