# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 03:20:17 2019

@author: huyn
"""

##Cartesian tree
#build a tree with property:
#    1. binary tree
#    2. Min Heap
#    3. In order traversal return array
class TreeNode:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print (root.val)
            self.inorder(root.right)
class cartersianTree:
    def __init__(self,arr):
        self.root = self.initialize(arr)
    
    def initialize(self,arr):
        root = None
        for item in arr:
            newNode = TreeNode(item)
            if not root:
                root = newNode
            else:
                if newNode.val>root.val:
                    # make our root as newNode child, set newNode as root
                    newNode.left = root
                    root = newNode
                # bigger will be lower, and something happens first will be on the left child
                else:
                    # we traverse the right until we hit nothing, or we hit one that is greater than root
                    # use a copy of the root
                    tempRoot = root
                    while tempRoot.right:
                        # we have to check if our root.right is still lower than item
                        if tempRoot.right.val<item:
                            tempRoot= tempRoot.right
                        else:
                            # we have to swap
                            temp = tempRoot.right
                            tempRoot.right = newNode
                            newNode.left = temp
                            break
                    # we break the loop either we hit none or we have done assignment, if we have done 
                    # asssignment , our tempRoot.right would not be empty
                    if not tempRoot.right:
                        tempRoot.right = newNode
        return root

arr = [5,8,6,1]
tree = cartersianTree(arr)
root = tree.root
root.inorder(root)
# O(nlogn),O(n) space