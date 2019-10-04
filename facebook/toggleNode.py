# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 03:27:24 2019

@author: huyn
"""

class Node:
    def __init__(self,val,left=None,right=None,parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
    def print(self):
        root = self
        def dfs(root):
            if root:
                print (root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
# Toggle Node

def toggle(node):
    # if node is 0, then basically made everything on the path to 0
    if node.val ==1:
        while node:
            node.val = 0
            node = node.parent
    else:
        # togle to 1
        parent = node.parent
        node.val = 1
        while parent:
            if parent.left.val==1 and parent.right.val==1:
                parent.val =1
                
            else:
                parent.val =0
            parent = parent.parent
#
#A = Node(1)
#B= Node(1)
#C=Node(1)
#D=Node(1)
#E=Node(1)
#F=Node(1)
#G=Node(1)
#A.left = B
#A.right = C
#B.parent=A
#C.parent=A
#B.left = D
#B.right = E
#D.parent = B
#E.parent=B
#C.left  =F
#C.right = G
#F.parent=C
#G.parent= F
#A.print()
#toggle(E)
#A.print()
