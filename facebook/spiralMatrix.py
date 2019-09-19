# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:43:31 2019

@author: huyn
"""

# given number n, print spiral matrix n
def printSpiral(n):
    output = [[0]*n for i in range(n)]
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    current  = (0,0)
    index = 0
    def check(x,y,direction,n):
        addX,addY = direction
        X,Y =x+addX,y+addY
        if X>=0 and Y>=0 and X<n and Y<n and output[X][Y]==0:
            return True
        return False
    for i in range(1,n**2+1):
        x,y = current
        output[x][y]=i
        # plan for next step
        direction   = directions[index]
        if check(x,y,direction,n):
            current = (x+direction[0],y+direction[1])
        else:
            index = (index+1)%4
            direction   = directions[index]
            current = (x+direction[0],y+direction[1])
    return output
#print (printSpiral(3))