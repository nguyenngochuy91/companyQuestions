# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:13:56 2019

@author: huyn
"""
"""
727. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". 
If there are multiple such minimum-length windows, return the one with the left-most starting index.
"""

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        start = 0
        stop = 0
        countT = {}
        for letter in T:
            if letter not in countT:
                countT[letter] = 0
            countT[letter]+=1
        d = {}
        hitting = 0
        length = float("inf")
        index = -1
        while stop<len(S):
            letter = S[stop]
            if letter not in d:
                d[letter] =0
            d[letter] +=1
            stop +=1
            if d[letter] == countT[letter]:
                hitting+=1
                while hitting == len(countT):
                    length = min(length,stop-start)
                    index = start
                    first = S[letter]
                    d[first]-=1
                    if first in countT:
                        if d[first] <countT[first]:
                            hitting-=1
        return index,length         