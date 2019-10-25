# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:01:07 2019

@author: Huy Nguyen
"""

def reverseList(head):
    def dfs(head,prev):
        if not head:
            return head,head
        else:
            newHead, newRoot = dfs(head.next,head) # our recursive relation
            # our work to link
            # link our head.next to prev
            head.next = prev
            # link newHead next to head
            newHead.next = head
            return head,newRoot
    if head:
        return dfs(head,None)[1]
    else:
        return None