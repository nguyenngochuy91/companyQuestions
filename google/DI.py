# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:42:40 2020

@author: huyn
"""
#from typing import List
#942. DI String Match
class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]