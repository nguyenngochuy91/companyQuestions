# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:51:51 2019

@author: huyn
"""

#Binary Tree Paths
def binaryTreePaths(root):
    res = []
    def dfs(root,string):
        if root:

            string.append(str(root.val))
            if root.left and root.right:
                dfs(root.left,string)
                dfs(root.right,string)
            elif root.left:
                dfs(root.left,string)
            elif root.right:
                dfs(root.right,string)
            else:
                res.append("->".join(string))
            string.pop()
    dfs(root,[])
    return res