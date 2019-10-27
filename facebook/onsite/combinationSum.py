# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:42:08 2019

@author: huyn
"""

#39. Combination Sum
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        def dfs(accumulate,target,index,path):
            for i in range(index,len(candidates)):
                num = candidates[i]
                if num + accumulate > target:
                    break
                elif num + accumulate == target:
                    path.append(num)
                    self.res.append(path[:])
                    path.pop()
                    break
                else:
                    path.append(num)
                    dfs(accumulate + num, target,i,path)
                    path.pop()
        dfs(0,target,0,[])
        return self.res 
    
candidates = [2,3,5]
solution = Solution()
print (solution.combinationSum(candidates,8))