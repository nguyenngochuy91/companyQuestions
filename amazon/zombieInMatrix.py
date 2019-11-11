# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:56:19 2019

@author: huyn
"""
"""
Zombie in Matrix
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) 
human beings into zombies every hour. Find out how many hours does it take to infect all humans?"""
from collections import deque
def numHoursToInfectAll(grid):
    zombies = deque([])
    row = len(grid)
    col = len(grid[0])
    numHuman = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c]:
                zombies.append((r,c))
            else:
                numHuman += 1
    minute = 0
    while zombies:
        for i in range(len(zombies)):
            x,y = zombies.popleft()
            temp = [(0,1),(1,0),(-1,0),(0,-1)]
            for a,b in temp:
                X,Y = x+a,y+b
                if X >= 0 and Y >= 0 and X < row and Y< col and grid[X][Y] == 0:
                    grid[X][Y] = 1
                    numHuman -= 1
                    zombies.append((X,Y))
        minute+=1
    if numHuman:
        return -1
    return minute