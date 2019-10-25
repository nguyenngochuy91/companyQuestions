# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 03:40:59 2019

@author: huyn
"""

def findPeakElement(arr):

    start ,stop = 0, len(arr)-1
    while start+1<stop:
        mid = (start+stop)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
            start = mid
        else:
            stop = mid
    if arr[start]<arr[stop]:
        return stop
    else:
        return start