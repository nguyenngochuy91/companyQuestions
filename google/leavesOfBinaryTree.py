# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 00:56:03 2019

@author: Huy Nguyen
"""

#366. Find Leaves of Binary Tree
#Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        d = {}
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    if 0 not in d:
                        d[0] = []
                    d[0].append(root.val)
                    return 0
                elif root.left and root.right:
                    left = dfs(root.left)+1
                    right = dfs(root.right)+1
                    level = max(left,right)
                    if level not in d:
                        d[level] = []
                    d[level].append(root.val)
                    return level
                elif root.left:
                    left = dfs(root.left)+1
                    if left not in d:
                        d[left] = []
                    d[left].append(root.val)
                    return left
                else:
                    right = dfs(root.right)+1
                    if right not in d:
                        d[right] = []
                    d[right].append(root.val)        
                    return right
        dfs(root)
        res = []
        if not d:
            return []
        for i in range(min(d),max(d)+1):
            res.append(d[i])
        return res