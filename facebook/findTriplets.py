# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:08:09 2019

@author: huyn
"""

#Find triplets that sum to zero
#Determine if any 3 integers in an array sum to 0.
# just return True False, or the triplet
# find all or just any
# can a number be repeated for the triplets
# any 2 sums make overflow
#O(n^3)
def containsTripletNaive(arr,num):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i]+arr[j]+arr[k]==num:
                    return True
    return False
#O(n^2) and O(n) space
def containsTripletHash(arr,num):
    dictionary = set()
    for item in arr:
        dictionary.add(item)
    for i in range(len(arr)):
        for j in range(len(arr)):
            mySum = arr[i]+arr[j]
            if num-mySum in dictionary:
                return True
    return False

arr = [-5, -5, -4, -3, -2, -1, 1, 1, 2, 2, 2, 3, 5, 10, 10, 31]
num = 0
#print (containsTripletNaive(arr,num))
#print (containsTripletHash(arr,num))
#O(n^2logn)
def binarySearch(arr,num):
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(arr)):
            mySum = arr[i]+arr[j]
            target = num-mySum
            start,stop =0,len(arr)-1
            while start+1<stop:
                mid = (start+stop)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    start= mid
                else:
                    stop = mid
            if arr[start]==mid:
                return True
            if arr[stop]==mid:
                return True
    return False
# 2 pointers, O(n^2)
def pointers(arr,num):
    arr.sort()
    for i in range(len(arr)):
        item = num- arr[i]
        start = 0
        stop  = len(arr)-1
        while start<=stop:
            s = arr[stop]+arr[start]
            if s>item:
                stop-=1
            elif s<item:
                start+=1
            else:
                return True        
    return False