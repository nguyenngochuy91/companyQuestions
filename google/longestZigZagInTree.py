# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:20:02 2020

@author: huyn
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(root):
            if not root: return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]
        return dfs(root)[-1]