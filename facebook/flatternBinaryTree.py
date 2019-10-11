# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:53:28 2019

@author: Huy Nguyen
"""

def flatten(root) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root:
        flatten(root.left)
        flatten(root.right)
        if root.left and root.right:
            temp = root.right
            root.right = root.left
            root.left  = None
            while root.right:
                root= root.right
            root.right = temp
        elif root.left:
            root.right = root.left
            root.left=  None