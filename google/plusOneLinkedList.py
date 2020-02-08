# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:26:43 2020

@author: huyn
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#369. Plus One Linked List

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def dfs(root,remainder):
            if root:
                if root.next:
                    toAdd = dfs(root.next,remainder)
                    val = (root.val+toAdd)%10
                    toAdd = (root.val+toAdd)//10
                    root.val = val
                    return toAdd
                else:
                    val = (root.val+1)%10
                    toAdd = (root.val+1)//10
                    root.val = val
                    return toAdd
        toAdd = dfs(head,0)
        if toAdd:
            root = ListNode(1)
            root.next = head
            return root
        return head