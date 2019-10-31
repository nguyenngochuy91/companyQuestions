# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:15:08 2019

@author: Huy Nguyen
"""
"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list."""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next
    def printOut(self):
        root = self
        while root:
            print (root.val)
            root = root.next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = ListNode(0)
        root.next = head
        count = 1
#        while count + 1<m:# try to get to the head rightbefore the node
        prev = root
        while count!= m:
            prev = head
            head = head.next
            count += 1
        time = n - m +1
        fakeNode = ListNode(0)
        fakeNode.next = head
        p = fakeNode
        first = head # 1->2->3->4->5->6, nead fisrt at 3 to link with 6
        while time and head:
            next = head.next
            head.next = p
            p = head
            head = next
            time -= 1
        # link 2 to 5
        prev.next = p
        # link 3 to 6
        first.next = head
        return root.next
    
root = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
#root.printOut()
solution = Solution()
newRoot = solution.reverseBetween(root,1,6)
newRoot.printOut()