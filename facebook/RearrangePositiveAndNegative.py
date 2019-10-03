# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 00:56:48 2019

@author: huyn
"""

#Given an array of positive and negative numbers, arrange them such that all negative
# integers appear before all the positive integers in the array without using any additional
# data structure like hash table, arrays, etc. The order of appearance should be maintained.
#
#Input:  [12 11 -13 -5 6 -7 5 -3 -6]
#Output: [-13 -5 -7 -3 -6 12 11 6 5]
def rearrangeSlow(array):
    for i in range(1,len(array)):
        if array[i]<0:
            val = array[i]
            j = i -1
            while j>=0 and array[j]>0:
                array[j+1]=array[j]
                j-=1
            array[j+1]= val
    return
    
array = [12 ,11, -13, -5, 6, -7, 5, -3, -6]
#rearrangeSlow(array)
#print (array)
def rearrangeFast(array):
    return