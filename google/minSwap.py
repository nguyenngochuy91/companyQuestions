# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:40:16 2019

@author: huyn
"""

#801. Minimum Swaps To Make Sequences Increasing
"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only 
if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  
It is guaranteed that the given input always makes it possible.
"""
from typing import List
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        swap = 1
        unswap = 0
        L = len(A)
        for i in range(1, L):
            if A[i-1] >= A[i] or B[i-1] >= B[i]:
                swap, unswap = unswap +1, swap
            elif A[i-1] >= B[i] or B[i-1] >= A[i]:
                swap, unswap = swap +1, unswap
            else:
                swap, unswap = min(swap, unswap) + 1, min(swap, unswap)
        return min(swap, unswap)