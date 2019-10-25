# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:29:56 2019

@author: huyn
"""
#import time

#You have a huge array of integers containing only 0's and 1's. Write an algorithm
# that finds the number of 1's found in the array in a specific range.
def naiveCountOne(arr,start,stop):
    count = 0
    for i in range(start,stop+1):
        if arr[i]:
            count+=1
    return count

# unmuttable array, we do processing first
def process(arr):
    newArr =[]
    count = 0
    for num in arr:
        if num==1:
            count+=1
        newArr.append(count)
    return newArr
def countOneFromProcessedArr(arr,start,stop):
    if start ==0:
        return arr[stop]
    return arr[stop]-arr[start-1]

arr= [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
#start =time.time()
#print (naiveCountOne(arr,3,50))
#stop  = time.time()
#print (stop-start)
#arr1= process(arr)
#start =time.time()
#print (countOneFromProcessedArr(arr1,3,50))
#stop  = time.time()
#print (stop-start)

#307. Range Sum Query - Mutable
class SegmentNode:
    def __init__(self,val,start,stop,left=None,right=None):
        self.val   = val
        self.start = start
        self.stop  = stop
        self.left  = left
        self.right = right
class NumArray:
    def __init__(self, nums):
        self.root = self.initialize(nums,0,len(nums)-1)
    def initialize(self,nums,start,stop):
        if start == stop:
            node = SegmentNode(nums[start],start,stop)
            return node
        elif start<stop:
            mid = (start+stop)//2
            left = self.initialize(nums,start,mid)
            right = self.initialize(nums,mid+1,stop)
            node  = SegmentNode(left.val+right.val,start,stop,left,right)
            node.left = left
            node.right = right
            return node
    def update(self, i: int, val: int) -> None:
        def dfs(root,i,val):
            if root:
                if root.start==root.stop ==i:
                    extra = val-root.val
                    root.val = val
                    return extra
                else:
                    start,stop = root.start,root.stop
                    # check which half does it belong to, left or right
                    mid  = (start+stop)//2
                    if i>=start and i<=mid:
                        extra=  dfs(root.left,i,val)
                    else:
                        extra = dfs(root.right,i,val)
                    root.val+=extra
                    return extra
        dfs(self.root,i,val)
    def sumRange(self, i: int, j: int) -> int:
        def dfs(root,i,j):
            start,stop = root.start,root.stop
            if i== start and j == stop:
                return root.val
            else:
                mid = (start+stop)//2
                val = 0
                # check if i>mid
                if i>mid:
                    val+=dfs(root.right,i,j)
                elif i<=mid:
                    if j<=mid:
                        val+=dfs(root.left,i,j)
                    else:
                        # this means we have to search bothway
                        val+=dfs(root.left,i,mid)
                        val+=dfs(root.right,mid+1,j)
                return val
        return dfs(self.root,i,j)
    def printOut(self,node):
        if node:
            self.printOut(node.left)
            print (node.val)
            self.printOut(node.right)
    
arr  = [1,3,5]
tree = NumArray(arr)
#tree.update(0,10)
#tree.printOut(tree.root)
print (tree.sumRange(0,2))
