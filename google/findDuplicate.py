# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:34:41 2020

@author: huyn
"""

#609. Find Duplicate File in System
from typing import List
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            item = path.split()
            root = item[0]
            for file in item[1:]:
                file = file.split("(")
                fileName = file[0]
                content = file[1].split(")")[0]
                if content not in d:
                    d[content] = []
                d[content].append(root+"/"+fileName)
        return [d[key] for key in d if len(d[key])>=2]