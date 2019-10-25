# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:48:53 2019

@author: huyn
"""

#34. Find First and Last Position of Element in Sorted Array
def searchRange(nums,target):
    start,stop = findLeftMost(nums,target),findRightMost(nums,target)
    return [start,stop]
def findLeftMost(nums,target):
    start,stop = 0,len(nums)-1
    while start+1<stop:
        mid = (start+stop)//2
        if nums[mid]>=target:
            stop=mid
        else:
            start = mid
    if nums[start]==target:
        return start
    if nums[stop]==target:
        return stop
    return -1
    
def findRightMost(nums,target):
    start,stop = 0,len(nums)-1
    while start+1<stop:
        mid = (start+stop)//2
        if nums[mid]<=target:
            start=mid
        else:
            stop = mid
    if nums[stop]==target:
        return stop
    if nums[start]==target:
        return start
    return -1