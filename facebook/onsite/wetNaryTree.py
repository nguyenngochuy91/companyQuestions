# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:55:28 2019

@author: Huy Nguyen
"""
"""
Given an N-ary tree, if a water drop is dropped at the root of the tree and it 
flows down throughout the tree, find out how much time will it take to wet the entire tree. 
The time to travel each edge is given."""
class TreeNode:
    def __init__(self,val,children=[]):
        self.val = val
        self.children= children
        
def getWater(root):
    def dfs(root):
        if not root:
            return 0
    
        sum = root.val
        for child in root.children:
            sum += dfs(child)
        return sum
    if not root:
        return 0
    return dfs(root) - root.val

root = TreeNode(1,[TreeNode(2,[TreeNode(5),TreeNode(6),TreeNode(7)]),TreeNode(3,[TreeNode(10),TreeNode(11),TreeNode(4)]),TreeNode(4,[TreeNode(9)])])
print (getWater(root))