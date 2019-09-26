# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:34:49 2019

@author: huyn
"""

#Find Intersection of Two Sorted Integer Arrays
def mergerPointers(arr1,arr2):
    p1,p2 = 0
    arr   = []
    while p1<len(arr1) and p2<len(arr2):
        num1,num2= arr1[p1],arr2[p2]
        if num1==num2:
            arr.append(num1)
            arr.append(num2)
            p1+=1
            p2+=1
        elif num1<num2:
            arr.append(num1)
            p1+=1
        else:
            arr.append(num2)
            p2+=1
    for i in range(p1,len(arr1)):
        arr.append(arr1[i])
    for i in range(p2,len(arr2)):
        arr.append(arr2[i])
    return arr
arr1,arr2=[1,3,6,17,21], [2,4,6,21]
def mergerBST(arr1,arr2):
    
    return 