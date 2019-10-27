# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:32:10 2019

@author: huyn
"""
"""
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that
 only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
 """
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [1,2,3,4,5,6,7,8,9]
        self.res = []
        def dfs(index,path,target,k,acc):
            if len(path) == k: 
                if acc == target:
                    self.res.append(path[:])
            elif len(path) < k:
                for i in range(index, len(arr)):
                    num = arr[i]
                    if num + acc <=target:
                        path.append(num)
                        dfs(i+1,path,target,k,acc + num)
                        path.pop()
        dfs(0,[],n,k,0)
        return self.res