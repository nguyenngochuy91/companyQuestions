# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:39:11 2019

@author: huyn
"""
"""
Subtree with Maximum Average
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. 
The average value of a subtree is the sum of its values, divided by the number of nodes."""

class NTreeNode:
    def __init__(self,val,children = []):
        self.val = val
        self.children = children

class TreeNode:
    def __init(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max = -float("inf")
        def dfs(root):
            if not root:
                return 0,0
            else:
                leftSum,leftNode = dfs(root.left)
                rightSum,rightNode  = dfs(root.right)
                currentSum = root.val + leftSum + rightSum
                numNode = 1+ leftNode + rightNode
                average = currentSum/numNode
                self.max = max(self.max,average)
                return currentSum,numNode
        dfs(root)
        return self.max
    def maximumAverageSubtreeNtree(self, root: NTreeNode) -> float:
        self.max = -float("inf")
        def dfs(root):
            if not root:
                return 0,0
            else:
                currentSum = root.val 
                numNode = 1
                for child in root.children:
                    sum,nodes = dfs(child)
                    currentSum+=sum
                    numNode +=nodes
                average = currentSum/numNode
                self.max = max(self.max,average)
                return currentSum,numNode
        dfs(root)
        return self.max