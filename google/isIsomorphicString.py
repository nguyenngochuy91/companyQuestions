# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:09:15 2019

@author: huyn
"""

#  Isomorphic Strings
#Given two strings s and t, determine if they are isomorphic.
#
#Two strings are isomorphic if the characters in s can be replaced to get t.
#
#All occurrences of a character must be replaced with another character while 
#preserving the order of characters. No two characters may map to the same character but a character may map to itself.
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        v = {}
        for i in range(len(s)):
            first = s[i]
            second = t[i]
            if first not in d and second not in v:
                d[first] = second
                v[second] = first
            elif first in d and second in v:
                if d[first]!= second or v[second]!= first:
                    return False
            else:
                return False
        return True