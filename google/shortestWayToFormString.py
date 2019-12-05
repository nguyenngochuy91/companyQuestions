# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:51:15 2019

@author: Huy Nguyen
"""
"""
1055. Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation 
equals target. If the task is impossible, return -1.
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz"."""
class Solution:
    # O(mn), space : O(1)
    def shortestWay1(self, source: str, target: str) -> int:
        if len(set(target)-set(source))!= 0:
            return -1
        i, j = 0 ,0 
        res = 0
        while j < len(target):
            letterS = source[i]
            letterT = target[j]
            if letterS == letterT:
                i += 1
                j += 1
            else:
                i += 1
            if i == len(source):
                # we have to reset i and increment res
                res+=1
                i = 0
        if i!=0:
            res+=1
        return res