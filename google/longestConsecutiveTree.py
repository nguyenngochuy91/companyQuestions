#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:36:03 2020

@author: huynguyen
"""


# 298 longest consecutive sequence
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max = 0
        def dfs(root,currentLength):
            if root:
                self.max = max(self.max,currentLength)
                if root.left and root.right:
                    if root.val+1 == root.left.val:
                        dfs(root.left,currentLength+1)
                    else:
                        dfs(root.left,1)
                    if root.val+1 == root.right.val:
                        dfs(root.right,currentLength+1)
                    else:
                        dfs(root.right,1)
                elif root.left:
                    if root.val+1 == root.left.val:
                        dfs(root.left,currentLength+1)
                    else:
                        dfs(root.left,1)  
                elif root.right:
                    if root.val+1 == root.right.val:
                        dfs(root.right,currentLength+1)
                    else:
                        dfs(root.right,1)  
        dfs(root,1)
        return self.max 
        
                