# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:58:13 2019

@author: huyn
"""

#702. Search in a Sorted Array of Unknown Size
#Given an integer array sorted in ascending order, write a function to search target in nums.  
#If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. 
#You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the 
#array at index k (0-indexed).
#
#You may assume all integers in the array are less than 10000, and if you access the array out of bounds, 
#ArrayReader.get will return 2147483647.

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        stop = 1
        size = 0
        while abs(reader.get(stop))<10000:
            stop*=2
        while size+1<stop:
            mid = (size+stop) // 2
            val = reader.get(mid)
            if abs(val)>=10000:
                stop = mid
            else:
                size = mid
        start,stop = 0,size

        while start +1 <stop:
            mid = (start+stop)//2
            val = reader.get(mid)
            if val== target:
                return mid
            elif val > target:
                stop = mid
            else:
                start = mid
        if reader.get(start) == target:
            return start
        if reader.get(stop) == target:
            return stop
        return -1