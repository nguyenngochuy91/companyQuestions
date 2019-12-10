# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:47:06 2019

@author: huyn
"""

#531. Lonely Pixel I
#
#
#Given a picture consisting of black and white pixels, find the number of black lonely pixels.
#
#The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
#
#A black lonely pixel is character 'B' that located at a specific position where the same row and same 
#column don't have any other black pixels.
from typing import List
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        r = len(picture)
        c = len(picture[0])
        row = [0]*r
        col = [0]*c
        for i in range(r):
            for j in range(c):
                if picture[i][j] == "B":
                    row[i]+=1
                    col[j]+=1
        count = 0
        for i in range(r):
            for j in range(c):
                if picture[i][j] == "B":
                    if row[i] == 1 and col[j] == 1:
                        count+=1
        return count
picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
sol = Solution()
sol.findLonelyPixel(picture)