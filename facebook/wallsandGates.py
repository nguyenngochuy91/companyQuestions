# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:24:33 2019

@author: huyn
"""

#286. Walls and Gates
#Given a maze with cells being: gates, walls or empty spaces.
#You are given a m x n 2D grid initialized with these three possible values.

#-1 - A wall or an obstacle.
#0 - A gate.
#INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you 
#may assume that the distance to a gate is less than 2147483647.
#Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, 
#it should be filled with INF.
from typing import List
from collections import deque
num = 2147483647
rooms=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
def wallsAndGates(rooms: List[List[int]]) -> None:
    rows = len(rooms)
    cols = len(rooms[0])
    for r in range(rows):
        for c in range(cols):
            # find the gate
            if rooms[r][c]==0:
                visited = set()
                distance = 0
                queue = deque([[r,c]])
#                print (queue)
                visited.add((r,c))
                while queue:
                    size = len(queue)
                    distance +=1
                    for i in range(size):
                        currentRow,currentCol = queue.popleft()                       
                        add= [(1,0),(0,1),(-1,0),(0,-1)]
                        for x,y in add:
                            nextRow,nextCol = currentRow+x,currentCol+y
                            if isValid(nextRow,nextCol,rows,cols) and (nextRow,nextCol) not in visited:
                                if rooms[nextRow][nextCol]!=-1 and  rooms[nextRow][nextCol]!=0:
                                    visited.add((nextRow,nextCol))
                                    queue.append((nextRow,nextCol))
                                    # update rooms distance
                                    rooms[nextRow][nextCol] = min(rooms[nextRow][nextCol],distance)
    return

def isValid(currentRow,currentCol,rows,cols):
    return currentRow>=0 and currentCol>=0 and currentRow<rows and currentCol<cols
#wallsAndGates(rooms)
def wallsAndGatesCheckAllSameTime(rooms: List[List[int]]) -> None:
    rows = len(rooms)
    cols = len(rooms[0])
    gates = []
    for r in range(rows):
        for c in range(cols):
            # find the gate
            if rooms[r][c]==0:
                gates.append([[r,c]])
    visited = set()
    distance = 0
    while gates:
#        print (gates)
        temp =[]
        distance+=1
        for item in gates:
            nextList = []
            for currentRow,currentCol in item:
                add= [(1,0),(0,1),(-1,0),(0,-1)]
                for x,y in add:
                    nextRow,nextCol = currentRow+x,currentCol+y
                    if isValid(nextRow,nextCol,rows,cols) and (nextRow,nextCol) not in visited:
                        if rooms[nextRow][nextCol]!=-1 and  rooms[nextRow][nextCol]!=0:
                            visited.add((nextRow,nextCol))
                            nextList.append((nextRow,nextCol))
                            rooms[nextRow][nextCol] =distance
            if nextList:
                temp.append(nextList)
        gates= temp
    return
wallsAndGatesCheckAllSameTime(rooms)