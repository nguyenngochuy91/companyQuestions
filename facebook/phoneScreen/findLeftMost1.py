# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:59:10 2019

@author: huyn
"""

#Leftmost column index of 1
#In a binary matrix (all elements are 0 and 1), every row is sorted in ascending 
#order (0 to the left of 1). Find the leftmost column index with a 1 in it.
arr = [[0, 0, 0, 1],
 [0, 1, 1, 1],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
def findLeftMostBST(arr):
    row = len(arr)
    col = len(arr[0])
    stop = col-1
    myMin = None
    for r in range(row):
        if myMin==None:
            stop = leftMost(arr[r],col-1)
#            print (stop)
        else:
            stop = leftMost(arr[r],myMin)
#            print (stop)
        if stop!=-1:
            myMin = stop
    return myMin
def leftMost(nums,stop):
    start =0
#    print (nums)
    while start+1<stop:
        mid = (start+stop)//2
        if nums[mid]==1:
            stop = mid
#            print (stop)
        else:
            start = mid
    if nums[start]==1:
        return start
    if nums[stop]==1:
        return stop
    return -1

#print (findLeftMostBST(arr))
def findLeftMostPointers(arr):
    row = len(arr)
    col = len(arr[0])
    r   = 0
    c   = col-1
    myMin = -1
    while r<row and c>=0:
        val =arr[r][c]
        if val==0: # we can ignore this row
            r+=1
        else:
            myMin = c
            c-=1
    return myMin
print (findLeftMostPointers(arr))
