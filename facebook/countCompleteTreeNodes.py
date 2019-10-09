# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:30:11 2019

@author: huyn
"""
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val= val
        self.left = left
        self.right = right
#222. Count Complete Tree Nodes
#Given a complete binary tree, count the number of nodes.
def countNodes(root: TreeNode) -> int:
    if not root:
        return 0
    left = countNodes(root.left)
    right = countNodes(root.right)
    return 1+left+right
        
        
a = TreeNode(3)
c = TreeNode(5,a)
d = TreeNode(6)
e = TreeNode(7)
f = TreeNode(8,d,e)
g = TreeNode(10,c,f)


# since we know it is a full binary tree, traverse to the left until we can't traverse more, then try to count node at that step

def countNodesSmart(root):
    def getDepth(root):
        if not root:
            return 0
        return 1+getDepth(root.left)
    depth = getDepth(root)
    def findPath(index):
        path = []
        while index:
            path.append(index%2)
            index//=2
        return path
    def checkIndex(root,path):
        for index in range(len(path)-1,-1,-1):
            if index==1:
                if root.right:
                    root= root.right
                else:
                    return False
            else:
                if root.left:
                    root = root.left
                else:
                    return False
        return True
    if depth<=1:
        return depth
    start = 0
    stop  = 2**depth-1
    while start+1<stop:
        mid = (start+stop)//2
        path = findPath(mid)
        if checkIndex(root,path):
            start = mid
        else:
            stop = mid
    if checkIndex(root,findPath(stop)):
        return 2**(depth-1)+stop
    elif checkIndex(root,findPath(start)):
        return 2**(depth-1)+start
    
print (countNodesSmart(g))
    