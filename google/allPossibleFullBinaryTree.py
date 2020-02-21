# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:43:21 2019

@author: huyn
"""

#894. All Possible Full Binary Trees
#A full binary tree is a binary tree where each node has exactly 0 or 2 children.
#
#Return a list of all possible full binary trees with N nodes.  Each element of the answer
# is the root node of one possible tree.
#
#Each node of each tree in the answer must have node.val = 0.
#
#You may return the final list of trees in any order.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]