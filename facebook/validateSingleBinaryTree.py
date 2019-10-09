# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:04:21 2019

@author: Huy Nguyen
"""
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val =val
        self.left = None
        self.right = None

n1 =  TreeNode(1);
n2 =  TreeNode(2);
n3 =  TreeNode(3);
n4 =  TreeNode(4);
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n3
n3.left = n4
arr= [n1,n2,n3]
def isBinaryTree(arr):
    parents= {}
    # check for if a node has more than 1 parent
    for node in arr:
        if node.left:
            if node.left not in parents:
                parents[node.left] = node
            else:
                return False
        if node.right:
            if node.right not in parents:
                parents[node.right] = node
            else:
                return False
    # check if there are more than 1 tree by traversing each node to the root node
    # if there are more than 1 root node, then there is a problem
    nodeSet=set(arr)
    rootNodes = set()
    while nodeSet:
        randomNode = nodeSet.pop()
        # traverse this randomNode up until we can't do it anymore
        while randomNode in parents:
            randomNode = parents[randomNode]
            if randomNode in nodeSet:
                nodeSet.remove(randomNode)
        rootNodes.add(randomNode)
    if len(rootNodes)!=1:
        return False
    # get the rootNode
    root = rootNodes.pop()
    # traverse through root, check if there is a cycle
    visited= set()
    visited.add(root)
    queue = deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
#            print (node)
            if node.left:
                if node.left in visited:
                    return False
                visited.add(node.left)
                queue.append(node.left)
            if node.right:
                if node.right in visited:
                    return False
                visited.add(node.right)
                queue.append(node.right)
    return len(visited)==len(arr)
print (isBinaryTree(arr))