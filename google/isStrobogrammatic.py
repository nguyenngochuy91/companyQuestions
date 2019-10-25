# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:16:13 2019

@author: huyn
"""
#Strobogrammatic Number

class Solution(object):
    def isStrobogrammatic(self, num):
        mapping = {"1":"1","8":"8","9":"6","6":"9","0":"0"}
        for i in range(len(num)//2+1):
            first,last = num[i],num[len(num)-1-i]
            if first not in mapping or last not in mapping:
                return False
            if mapping[first]!=last:
                return False
        return True