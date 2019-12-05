# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:19:44 2019

@author: Huy Nguyen
"""
"""
Given a complete binary tree such that the nodes are filled in a level-wise manner 
starting from 0 to n. Given a number find if it exists in the tree."""
class TreeNode:
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def isExist(root,num):
    if num == 0:
        return root!=None
    arr = []
    while num:
        val = num%2
        arr.append(val)
        if val:
            num = (num-1)//2
        else:
            num = (num-2)//2
    for i in range(len(arr)-1,-1,-1):
        if not root:
            return False
        if arr[i]:
            root = root.left
        else:
            root = root.right
    if not root:
        return False
    return True
root = TreeNode(0,TreeNode(1,TreeNode(3,TreeNode(7)),TreeNode(4)),TreeNode(2,TreeNode(5),TreeNode(6)))
for i in range(0,10):
    print (i,isExist(root,i))