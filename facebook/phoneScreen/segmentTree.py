# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:17:30 2019

@author: huyn
"""

class segmentNode:
    def __init__(self,val,start,stop,left=None,right=None):
        self.start = start
        self.stop  = stop
        self.val   = val
        self.left  = left
        self.right = right
class segmentTree:
    def __init__(self,arr):
        self.root = self.initialize(arr,0,len(arr)-1)
    def initialize(self,nums,start,stop):
        if start == stop:
            node = segmentNode(nums[start],start,stop)
            return node
        elif start<stop:
            mid = (start+stop)//2
            left = self.initialize(nums,start,mid)
            right = self.initialize(nums,mid+1,stop)
            node  = segmentNode(left.val+right.val,start,stop,left,right)
            return node
    def getSum(self,i,j):
        root = self.root
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

        return dfs(root,i,j)
    def update(self,index,val):
        root = self.root
        def dfs(root,index,val):
            if root.start == root.stop ==index:
                extra = val-root.val
                root.val = val
                return extra
            else:
                mid = (root.start+root.stop)//2
                if mid<index:
                    extra = dfs(root.right,index,val)
                else:
                    extra = dfs(root.left,index,val)
                root.val+=extra
                return extra
        extra = dfs(root,index,val)
        return extra
    
arr  = [1,3,5,7,9,11,13]
tree = segmentTree(arr)
#print (tree.root.val)
print (tree.getSum(0,4))
tree.update(3,100)
print (tree.getSum(3,3))