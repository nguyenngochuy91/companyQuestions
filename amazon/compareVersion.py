# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:57:39 2020

@author: huyn
"""
#Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(item) for item in version1.split(".")]
        v2 = [int(item) for item in version2.split(".")]
        size1 = len(v1)
        size2 = len(v2)
        for i in range(min(size1,size2)):
            num1,num2 = v1[i],v2[i]
            if num1<num2:
                return -1
            elif num1>num2:
                return 1
            else:
                continue
        for j in range(min(size1,size2),size1):
            if v1[j]>0:
                return 1
        for j in range(min(size1,size2),size2):
            if v2[j]>0:
                return -1            
        return 0