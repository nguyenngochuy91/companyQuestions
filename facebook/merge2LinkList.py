# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:00:39 2019

@author: Huy Nguyen
"""
# merge 2 list given 2 list node
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(None)
    def dfs(l1,l2,currentHead):
        if l1 and l2:
            if l1.val>l2.val:
                currentHead.next= l2
                currentHead = l2
                dfs(l1,l2.next,currentHead)
            else:
                currentHead.next = l1
                currentHead = l1
                dfs(l1.next,l2,currentHead)
        elif l1:
            currentHead.next=l1
        elif l2:
            currentHead.next = l2
    dfs(l1,l2,head)
    return head.next