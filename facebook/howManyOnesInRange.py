# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:29:56 2019

@author: huyn
"""
import time

#You have a huge array of integers containing only 0's and 1's. Write an algorithm
# that finds the number of 1's found in the array in a specific range.
def naiveCountOne(arr,start,stop):
    count = 0
    for i in range(start,stop+1):
        if arr[i]:
            count+=1
    return count

# unmuttable array, we do processing first
def process(arr):
    newArr =[]
    count = 0
    for num in arr:
        if num==1:
            count+=1
        newArr.append(count)
    return newArr
def countOneFromProcessedArr(arr,start,stop):
    if start ==0:
        return arr[stop]
    return arr[stop]-arr[start-1]

arr= [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
start =time.time()
print (naiveCountOne(arr,3,50))
stop  = time.time()
print (stop-start)
arr1= process(arr)
start =time.time()
print (countOneFromProcessedArr(arr1,3,50))
stop  = time.time()
print (stop-start)

#307. Range Sum Query - Mutable
class NumArray:
    def __init__(self, nums):
        return
    def update(self, i: int, val: int) -> None:
        return

    def sumRange(self, i: int, j: int) -> int:
        return None