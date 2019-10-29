# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:51:49 2019

@author: huyn
"""
"""
1007. Minimum Domino Rotations For Equal Row
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1."""
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        top = 0
        bot = 0
        set1 = set([A[0],B[0]])
        set2 = set([A[1],B[1]])
        val  = set1.intersection(set2)
        if len(val) == 0:
            return -1
        if len(val) == 1:
            val = val.pop()
            for i in range(len(A)):
                if A[i] == val and B[i] == val:
                    continue
                elif A[i] == val:
                    top += 1
                elif B[i] == val:
                    bot += 1
                else:
                    return -1
            return min(top,bot)
        else:
            val1 = val.pop()
            check1 = True
            for i in range(len(A)):
                if A[i] == val1 and B[i] == val1:
                    continue
                elif A[i] == val1:
                    top += 1
                elif B[i] == val1:
                    bot += 1
                else:
                    check = False
                    break
            if check1:
                res1 = min(top,bot)
            top = 0
            bot = 0
            val1 = val.pop()
            check2 = True
            for i in range(len(A)):
                if A[i] == val1 and B[i] == val1:
                    continue
                elif A[i] == val1:
                    top += 1
                elif B[i] == val1:
                    bot += 1
                else:
                    check2 = False
                    break
            if check2:
                res2 = min(top,bot)   
            if check1 and check2:
                return min(res1,res2)
            elif check1:
                return res1
            elif check2:
                return res2
            return -1