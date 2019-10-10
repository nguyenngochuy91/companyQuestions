# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 00:16:14 2019

@author: Huy Nguyen
"""

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def dfs(l1,l2,over):
        if l1 and l2:
            n1 = l1.val
            n2 = l2.val
            val =n1+n2+over
            newNode = ListNode(val%10)
            newNode.next = dfs(l1.next,l2.next,val//10)
            return newNode
        elif l1:
            n1 = l1.val
            val =n1+over
            newNode = ListNode(val%10)
            newNode.next = dfs(l1.next,l2,val//10)
            return newNode
        elif l2:
            n2 = l2.val
            val =n2+over
            newNode = ListNode(val%10)
            newNode.next = dfs(l1,l2.next,val//10)
            return newNode
        else:
            if over==1:
                return ListNode(1)
    return dfs(l1,l2,0)