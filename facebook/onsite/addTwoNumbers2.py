# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:43:32 2019

@author: huyn
"""

"""
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. A
dd the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = ListNode(0)
        self.leftOver = 0
        def dfs(l1,l2):
            if not l1 and not l2:
                return None
            else:
                newNode = ListNode(0) # make a node 
                if l1 and l2:
                    nextNode = dfs(l1.next,l2.next)
                elif l1:
                    nextNode = dfs(l1.next,l2)
                else:
                    nextNode = dfs(l1,l2.next)
                # our nextNode come back, if it is None means that it is the end
                newNode.next = nextNode
                # we will check value of l1.val and l2.val
                return newNode
        return
#Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 8 -> 0 -> 7