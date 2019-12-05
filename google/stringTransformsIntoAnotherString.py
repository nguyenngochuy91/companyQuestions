# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:42:33 2019

@author: Huy Nguyen
"""
"""
1153. String Transforms Into Another String
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
"""

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        return