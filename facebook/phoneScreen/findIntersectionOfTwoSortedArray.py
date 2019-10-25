# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 00:47:49 2019

@author: huyn
"""
import math
#Find intersection of 2 sorted interger arrays
def findIntersectionPointers(arr1,arr2):
    i,j =0,0
    arr = [  ]  
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr[j]:
            arr.append(arr1[i])
            i+=1
            j+=1
        if arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return arr

def findIntersectionBST(arr1,arr2):
    if len(arr1)<=len(arr2):
        short = arr1
        long  = arr2
    else:
        short = arr2
        long  = arr1
    arr = []
    start = 0
    stop  = len(long)-1
    for number in short:
        index = searchIndex(start,stop,long,number)
#        print (number,index,start,stop)
        if index == stop and long[index]!=number:
            break
        if long[index]==number:
            arr.append(number)
            start = index
            if start==len(long):
                break
    return arr
    
def searchIndex(start,stop,long,number):
    while start+1<stop:
        mid = (start+stop)//2
        if long[mid]>=number:
            stop  = mid
        else:
            start = mid
    return stop
#arr1,arr2=[1,3,6,17,21,21,21], [2,4,6,21,21,23]
#arr = findIntersectionBST(arr1,arr2)
# we keep checking the length of the 2 arr
def findIntersectionMix(arr1,arr2):
    arr = []
    i,j,c1,c2= 0,0,0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
            c1+=1
        elif arr1[i]>arr2[j]:
            j+=1
            c2+=1
        else:
            arr.append(arr1[i])
            i+=1
            j+=1

        # check if arr1 is denser than arr2
        if c1>math.log(len(arr1),2):
            i= searchIndex(i,len(arr1),arr1,arr2[j])
            c1= 0
        elif c2>math.log(len(arr2),2):
            j = searchIndex(j,len(arr2),arr2,arr1[i])
            c2 = 0
    return arr

arr1,arr2=[1,3,6,17,21,21,21], [2,4,6,21,21,23]
print (findIntersectionMix(arr1,arr2))