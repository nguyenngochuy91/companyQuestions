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
        right = {"XL":"LX","RX":"XR"}
        left  = {"LX":"XL","XR":"RX"} # because for case like XXL, we have to transform from reverse
        def dfs(index):
            if index == len(start):
                return True
            elif index < len(start):
                check1 = False
                check2 = False
                if start[index] == end[index]:
                    check1 = dfs(index+1)
                if index < len(start)-1:
                    string1 = start[index]+start[index+1]
                    string2 = end[index]+end[index+1]
                    if string1 in right:
                        if right[string1] == string2:
                            start[index],start[index+1] = start[index+1],start[index]
                            check2 = check2 or dfs(index+2)
                            start[index],start[index+1] = start[index+1],start[index]
                        elif right[string1][0] == string2[0]:
                            start[index],start[index+1] = start[index+1],start[index]
                            check2 = check2 or dfs(index+1)
                            start[index],start[index+1] = start[index+1],start[index]
                    elif string2 in left:
                        if left[string2] == string1:
                            end[index],end[index+1] = end[index+1],end[index]
                            check2 = check2 or dfs(index+2)
                            end[index],end[index+1] = end[index+1],end[index]
                        elif left[string2][0] == string1[0]:
                            end[index],end[index+1] = end[index+1],end[index]
                            check2 = check2 or dfs(index+1)
                            end[index],end[index+1] = end[index+1],end[index]                        
                return check1 or check2
        return dfs(0)
start = "XXXL"
end   = "LXXX"
mySolution = Solution()
print (mySolution.canTransform(start,end))
