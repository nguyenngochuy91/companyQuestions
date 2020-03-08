# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:06:17 2020

@author: huyn
"""
from typing import List
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = {i:[] for i in range(1,n+1)}
        for x,y in edges:
            graph[x].append(y)
        self.res = 0.0
#        print (graph)
        def dfs(node,visited,val):
            if node == target:
                self.res = val
#                print (18)
                return True
            else:
                if len(graph[node])>0:
                    nextVal = 1/(len(graph[node]))
#                    print (node,visited,nextVal)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            check = dfs(neighbor,visited,val*nextVal)
                            visited.remove(neighbor)
                            if check:
                                return True
                return False
        visited= set([1])
        for neighbor in graph[1]:
            visited.add(neighbor)
            dfs(neighbor,visited,1/len(graph[1]))
            visited.remove(neighbor)
        return self.res
solution = Solution()
print (solution.frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],2,4))
#solution.frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],1,7)
#print (solution.frogPosition(8,[[1,2],[1,4],[1,7],[1,5],[2,3],[4,6],[7,8]],7,7))