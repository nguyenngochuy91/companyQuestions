# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:12:29 2019

@author: huyn
"""
#40. Combination Sum II
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = set()
        def dfs(path,acc,target,index):
            for i in range(index,len(candidates)):
                num = candidates[i]
                if num + acc == target:
                    path += [num]
                    self.res.add(tuple(path))
                    path.pop()
                elif num + acc < target:
                    path += [num]
                    dfs(path,acc + num , target, i + 1)
                    path.pop()
                else:
                    break
        dfs([],0,target,0)
        return [list(item) for item in list(self.res)]

candidates = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
print (solution.combinationSum2(candidates,target))