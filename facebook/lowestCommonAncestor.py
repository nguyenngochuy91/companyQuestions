# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:44:58 2019

@author: Huy Nguyen
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def findPath(root,target,path):
        if root:
            if root.val == target.val:
                path.append(root)
                return True
            else:
                checkLeft = findPath(root.left,target,path)
                if checkLeft:
                    path.append(root)
                    return True
                checkRight = findPath(root.right,target,path)
                if checkRight:
                    path.append(root)
                    return True
                return False
        else:
            return False
    pathP = []
    foundP = findPath(root,p,pathP)
    pathQ = []
    foundQ = findPath(root,q,pathQ)
    pathP.reverse()
    pathQ.reverse()
    for i in range(min(len(pathP),len(pathQ))):
        if pathP[i]!=pathQ[i]:
            return pathQ[i-1]
    return pathQ[i]