# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:02:18 2019

@author: huyn
"""

#1016. Binary String With Substrings Representing 1 To N
#
#Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, 
#return true if and only if for 
#every integer X from 1 to N, the binary representation of X is a substring of S.
class Solution(object):
    def queryString(self, S, N):
        for n in range(1, N+1):
            if self.toBinary(n) in S:
                continue
            else: return False
        
        return True
        
    def toBinary(self, n):
        digits = []
        while n:
            digits.append(str(n%2))
            n//=2
        return ''.join(digits[::-1])