#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 06:25:44 2020

@author: huynguyen
"""


from typing import List
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row = len(forest)
        col = len(forest[0])
        trees = {}
        for r in range(row):
            for c in range(col):
                val =  forest[r][c]
                if val>1:
                    trees[val] = (r,c)
        myList = sorted(trees)
        res = 0
        def bfs(startX,startY,stopX,stopY):
            visited = set()
            queue = deque([(startX,startY)])
            count =0
            visited.add((startX,startY))
            while queue:
                count +=1
          
                for i in range(len(queue)):
                    nodeX,nodeY = queue.popleft()
            
                    for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                        newX,newY = nodeX+x,nodeY+y
                        if newX>=0 and newY>=0 and newX<row and newY<col:
                            if newX == stopX and newY == stopY:
                                return count
                            if (newX,newY) not in visited:
                                visited.add((newX,newY))
                                if forest[newX][newY]>=1:
                                    queue.append((newX,newY))
                
                                    
            return -1
        startX,stopX = 0,0
        for height in myList:
            nextX,nextY = trees[height]
            if startX == nextX and stopX == nextY:
                continue
            distance = bfs(startX,stopX,nextX,nextY)
      
            if distance == -1:
                return -1
            else:
                res+=distance
                startX,stopX = nextX,nextY
        return res
            