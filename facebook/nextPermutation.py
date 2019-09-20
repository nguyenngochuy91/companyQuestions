# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:29:47 2019

@author: Huy Nguyen
"""
import random
#31. Next Permutation
#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
#If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
#The replacement must be in-place and use only constant extra memory.
#
#Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
def nextPermutation(nums):

    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            # found the place to change
            # going back from this end, check the number to the right of i so that 
            # it is greater than nums[i-1], the right most, and the minimum
            rightmostIndex = None
            currentMin     = float("inf")
            for j in range(len(nums)-1,i-1,-1):
                if nums[j]>nums[i-1] and currentMin>nums[j] :
                    rightmostIndex= j
                    currentMin = nums[j]
            print (rightmostIndex,nums[rightmostIndex],i-1,nums[i-1])
            temp = nums[i-1]
            nums[i-1]= nums[rightmostIndex]
            nums[rightmostIndex]=temp
            nums[i:]=sorted(nums[i:])
            return nums
            
    nums.sort()
    return nums
#for j in range(20):
#    print ([int(i) for i in str(random.randint(1,10000000000000000000000000000000000000000000))])
