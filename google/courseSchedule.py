# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:15:42 2019

@author: huyn
"""

#Course Schedule II
#There are a total of n courses you have to take, labeled from 0 to n-1.
#
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
#Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
#There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
from typing import List
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    parents = {i:set() for i in range(numCourses)}
    children = {i:set() for i in range(numCourses)}
    for child,parent in prerequisites:
        parents[child].add(parent)
        children[parent].add(child)
    startNodes = [node for node in parents if len(parents)==0]
    res = []
    while startNodes:
        node = startNodes.pop()
        res.append(node)
        for neighbor in children[node]:
            # remove edge from node to neighbor
            parents[neighbor].remove(node)
            if len(parents[neighbor]) == 0:
                startNodes.append(neighbor)
    for node in parents:
        if len(parents[node])!=0:
            return []
    return res
numCourses,prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]