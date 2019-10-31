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
    def __init__(self, x,next = None):
        self.val = x
        self.next = next
    def printOut(self):
        root = self
        while root:
            print (root.val)
            root = root.next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = getArray(l1)
        arr2 = getArray(l2)
        arr3 = []
        left = 0
        while arr1 and arr2:
            val = arr1.pop()+arr2.pop()+left
            if val>=10:
                left = 1
            else:
                left = 0
            arr3.append(val%10)
        while arr1:
            val = arr1.pop()+left
            if val>=10:
                left = 1
            else:
                left = 0
            arr3.append(val%10)
        while arr2:
            val = arr2.pop()+left
            if val>=10:
                left = 1
            else:
                left = 0
            arr3.append(val%10)
        if left:
            arr3.append(1)
#        print (arr3)
        def dfs(index):
            if index == len(arr3)-1:
                node = ListNode(arr3[index])
                return node,node
            else:
                currentNode = ListNode(arr3[index])
                nextNode,rootNode = dfs(index+1)
                nextNode.next = currentNode
                return currentNode, rootNode
        return dfs(0)[1]
def getArray(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr
#Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 8 -> 0 -> 7
l1 = ListNode(7,ListNode(2,ListNode(4,ListNode(3))))
l2 = ListNode(5,ListNode(6,ListNode(4)))
solution = Solution()
l3 = solution.addTwoNumbers(l1,l2)
l3.printOut()