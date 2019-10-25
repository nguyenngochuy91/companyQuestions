# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:13:20 2019

@author: Huy Nguyen
"""

#binary right side view
from collections import deque
def rightSideView(root):
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        # we will append the last node in queue to res
        res.append(queue[-1].val)
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res