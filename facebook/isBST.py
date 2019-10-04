# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:44:42 2019

@author: huyn
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None    

#Problem: Is this binary tree a valid binary search tree?
def isValidBSTAssignMinMax(root: TreeNode) -> bool:
    if not root:
        return True
    else:
        checkLeft  = isValidBSTAssignMinMax(root.left)
        checkRight = isValidBSTAssignMinMax(root.right)
        if not root.left and not root.right:
            root.min = root.val
            root.max = root.val
            return True
        elif root.left and root.right:
            leftMin,leftMax = root.left.min, root.left.max
            rightMin,rightMax = root.right.min,root.right.max
            root.min = min(leftMin,rightMin,root.val)
            root.max = max(leftMax,rightMax,root.val)
            return root.val>leftMax and root.val<rightMin and checkLeft and checkRight
        elif root.left:
            leftMin,leftMax = root.left.min, root.left.max
            root.min = min(leftMin,root.val)
            root.max = max(leftMax,root.val)
            return root.val>leftMax  and checkLeft and checkRight
        else:
            rightMin,rightMax = root.right.min,root.right.max
            root.min = min(rightMin,root.val)
            root.max = max(rightMax,root.val)            
            return root.val<rightMin and checkLeft and checkRight
    
def isValidBstPreorder(self, root: TreeNode) -> bool:
    self.last = None
    def dfs(root):
        if not root:
            return True
        else:
            checkL = dfs(root.left)
            check  = True
            if self.last!=None:
                if root.val<=self.last:
                    check= False
            self.last = root.val
            checkR = dfs(root.right)
            return check and checkL and checkR
    return dfs(root)
    
def isValidBstPreorder1(self, root: TreeNode) -> bool:

    def dfs(root,last):
        if not root:
            return True
        else:
            checkL = dfs(root.left,last)
            check  = True
            if last!=None:
                if root.val<=self.last:
                    check= False
            last   = root.val
            checkR = dfs(root.right)
            return check and checkL and checkR
    return dfs(root,None)