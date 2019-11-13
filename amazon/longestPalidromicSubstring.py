# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:04:34 2019

@author: huyn
"""

""" longest palidromic substring"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        l,r = 0 , -1
        length = 0
        for i in range(len(s)):
            start, stop = i,i
            while start>=0 and stop<len(s):
                if s[start] == s[stop]:
                    start-=1
                    stop+=1
                    if stop- start -1 >length:
                        l,r = start+1,stop
                        length = stop-start-1
                else:
                    break
            start, stop = i,i+1
            while start>=0 and stop<len(s):
                if s[start] == s[stop]:
                    start-=1
                    stop+=1
               
                    if stop- start -1 >length:
                        l,r = start+1,stop
                        length = stop-start-1
                else:
                    break
        return s[l:r]