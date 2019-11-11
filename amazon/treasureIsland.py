# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:33:12 2019

@author: huyn
"""
"""
Treasure Island
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and 
dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. 
The top-left corner is always safe. Output the minimum number of steps to get to the
Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""
from collections import deque
def treasureIsland(array):
    row = len(array)
    col = len(array[0])
    visited = set()
    queue = deque([(0,0)])
    distance = 1
    while queue:
        for i in range(len(queue)):
            x,y = queue.popleft()
            temp = [(0,1),(1,0),(0,-1),(-1,0)]
            for addX,addY in temp:
                X,Y = x+addX,y+addY
                if X>=0 and Y>=0 and X<row and Y<col and (X,Y) not in visited:
                    if array[X][Y] == "X":
                        return distance
                    elif array[X][Y] == "O":
                        visited.add((X,Y))
                        queue.append((X,Y))
        distance += 1
    return
array = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]
print (treasureIsland(array))