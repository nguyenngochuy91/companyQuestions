# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:33:59 2019

@author: huyn
"""

#Jewels and Stones
#You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
#Each character in S is a type of stone you have.  
#You want to know how many of the stones you have are also jewels.
#
#The letters in J are guaranteed distinct, and all characters in J and S are letters. 
#Letters are case sensitive, so "a" is considered a different type of stone from "A".
from collections import Counter
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        S = Counter(S)
        s = 0
        for item in S:
            if item in J:
                s+= S[item]
        return s