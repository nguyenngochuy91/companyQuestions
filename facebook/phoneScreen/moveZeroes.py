# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:02:38 2019

@author: huyn
"""

#283. Move Zeroes
#
#Given an array nums, write a function to move all 0's to the end of it while 
#maintaining the relative order of the non-zero elements.
from typing import List
def moveZeroes(nums: List[int]) -> None:
    start, stop = 0,0 # 
    while stop<len(nums):
        if nums[stop]!=0: # we hit a non zero number, check if there is any zeroes before that
            while nums[start]!=0 and start<stop: # we scan the start to hit the first 0 and start still less or equal to stop
                start+=1
            # the loop break once nums[start] =0 and start still less than stop or start is equal to stop
            if nums[start]== 0:
                # swap
                nums[start],nums[stop]= nums[stop],nums[start]
            start+=1
        stop+=1
nums =[0,1,0,3,12]
moveZeroes(nums)
print (nums)
