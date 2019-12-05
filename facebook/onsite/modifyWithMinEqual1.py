# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:50:45 2019

@author: Huy Nguyen
"""
"""
You are given an array A of distinct integers, you have to return another array B which transforms the first array such that the minimum 
element in the new array is 1 and all the other elements maintain their relative ordering i.e.
 if A[i] > A[j] then it should also be that B[i] > B[j] and similarly for other elements. Better explanation of this question can be found here.
Input: [4, 2, 3, 7] 
Output: [3, 1, 2, 4]

Input: [-4, -2, -3, -7] 
Output: [2, 4, 3, 1]"""
def modify(arr):
    newArr = []
    myMin = min(arr)
    dif = myMin-1
    for item in arr:
        newArr.append(item-dif)
    return newArr
arr = [4, 2, 3, 7] 
print (modify(arr))
arr = [-4, -2, -3, -7] 
print (modify(arr))

#Follow ups:
#
#What if the elements are not distinct?
#Second question: You have to perform the same operation on a 2D array of distinct elements.
#What if the matrix has duplicates?