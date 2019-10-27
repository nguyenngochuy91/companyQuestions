# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:38:29 2019

@author: huyn
"""

#1004. Max Consecutive Ones III
#Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
#Return the length of the longest (contiguous) subarray that contains only 1s. 
import random
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = 0
        start , stop = 0, 0
        d = {0:0}
        while stop < len(A):
            currentNum = A[stop]
            if currentNum == 0:
                length  = max(length,stop-start)
                while d[0] == K and start <stop: # we break either d[0] <K or start == stop
                    firstNum = A[start]
                    start += 1 
                    if firstNum == 0:
                        d[0] -= 1
                # we break the loop either start  == stop, or d[0] ==k -1
                # if d[0] <= k- 1, we can include this index for stop to our length
                if d[0] <= K-1:
                    d[0] += 1
                elif d[0] == K:
                    # if d[0] still equal to K, we can't include this num, and start already equal to stop
                    # increment the start to not include it
                    start += 1
            # for case currentNum = 1, just increment stop
            stop +=1
        return max(length,stop-start)

def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,1))
    return arr

for i in range(10):
    print (generate(100))
    print (random.randint(1,100))