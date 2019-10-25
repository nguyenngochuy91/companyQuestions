# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:03:39 2019

@author: Huy Nguyen
"""

#Remove Duplicates from Sorted Array
#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<=1:
        return len(nums)
    count=1 # count how many differences number
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            count+=1
            # do something to swap the good up
            # the number of count also indicate where the new number is (index i), and where we should put this number at (at index count-1)
            nums[count-1]= nums[i]
    return count