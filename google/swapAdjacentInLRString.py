# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:35:59 2019

@author: huyn
"""

#Swap Adjacent in LR String
#In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either 
#replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". 
#Given the starting string start and the ending string end, 
#return True if and only if there exists a sequence of moves to transform one string to the other.
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        start = list(start)
        end = list(end)
        move = {"XL":"LX","RX":"XR"}
        for i in range(len(start)-1):
            first = "".join(start[i:i+2])
            second = "".join(end[i:i+2])
            if first == second:
                continue
            else:
                if first not in move:
                    return False
                if move[first] == second:
                    start[i] = second[0]
                    start[i+1] = second[1]
                else:
                    return False
        return True