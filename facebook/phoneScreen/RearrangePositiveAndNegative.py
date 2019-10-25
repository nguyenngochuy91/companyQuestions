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
    def dfs(start,stop):
        if start<stop:
            mid = (start+stop)//2
#            print ("start:{},mid:{},stop:{}".format(start,mid,stop))
            dfs(start,mid)
            dfs(mid+1,stop)
            # we find the first positive index and the end of it
            leftPosStart = None
            leftPosEnd   = None
            for i in range(start,stop+1):
                if array[i]>0:
                    if leftPosStart==None:
                        leftPosStart = i
                    leftPosEnd   = i
                # we hit negative, ,we check if lefposStart still is None, keep continue
                else:
                    if leftPosStart==None:
                        continue
                    else:
                        break
            rightPosStart = None
            rightPosEnd   = None
            if leftPosEnd!=None: # we find the first negative next to this
                for i in range(min(leftPosEnd+1,stop),stop+1):
                    if array[i]<0:
                        if not rightPosStart:
                            rightPosStart = i
                        rightPosEnd=i
                    else:
                        break
            if leftPosEnd!=None and rightPosStart!=None:
                # we have LN LP RN RP
                # reverse LP
                reverseArr(array,leftPosStart,leftPosEnd)
                # reverse RN
                reverseArr(array,rightPosStart,rightPosEnd)
                # reverse LP RN
                reverseArr(array,leftPosStart,rightPosEnd)
                
        
    dfs(0,len(array)-1)
    return
def reverseArr(arr,start,stop):
    while start<stop:
#        print (start,stop)
        arr[start],arr[stop]=arr[stop],arr[start]
        start+=1
        stop-=1
rearrangeFast(array)