# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:34:55 2019

@author: huyn
"""

#Amazing Number
#Define amazing number as: its value is less than or equal to its index. Given a 
#circular array, find the starting position, such that the total number of amazing numbers in the array is maximized.
#Example 1: 0, 1, 2, 3
#Ouptut: 0. When starting point at position 0, all the elements in the array are equal to 
#its index. So all the numbers are amazing number.
#Example 2: 1, 0 , 0
#Output: 1. When starting point at position 1, the array becomes 0, 0, 1. All the elements are amazing number.
#If there are multiple positions, return the smallest one.
#
#should get a solution with time complexity less than O(N^2)
def getAmazingNumberNaive(arr):
    size = len(arr)
    maxCount = 0
    for i in range(size):
        starting =i
        count = 0
        for j in range(size):
#            print (starting,j)
            if j>=arr[starting%size]:
#                print ("index:",j, "num:",arr[starting%size])
                count+=1
            starting+=1
        maxCount= max(maxCount,count)
    return maxCount
arr =[0,1,2,3]

print (getAmazingNumberNaive(arr))
#arr=[3,2,1,0]
#
#print (getAmazingNumberNaive(arr))
#arr = [4]
#print (getAmazingNumberNaive(arr))