# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:21:35 2019

@author: huyn
"""

#1111. Maximum Nesting Depth of Two Valid Parentheses Strings
#A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:
#
#It is the empty string, or
#It can be written as AB (A concatenated with B), where A and B are VPS's, or
#It can be written as (A), where A is a VPS.
#We can similarly define the nesting depth depth(S) of any VPS S as follows:
#
#depth("") = 0
#depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
#depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
#For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
#
# 
#
#Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length).
#
#Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.
#
#Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 
#if seq[i] is part of A, else answer[i] = 1.  
#Note that even though multiple answers may exist, you may return any of them.

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # if the num of ( is divisible by 2, then we can just set each equal to half
        res = []
        countA, countB = 0,0
        for item in seq:
            if item == "(":
                if countA >=countB:
                    countB +=1
                    res.append(1)
                else:
                    countA+=1
                    res.append(0)
            else:
                if countA>=countB:
                    countA-=1
                    res.append(0)
                else:
                    countB-=1
                    res.append(1)
        return res
                    