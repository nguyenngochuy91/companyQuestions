# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 03:57:00 2019

@author: Huy Nguyen
"""
"""
126. Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same."""
from typing import List
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        wordList.append(beginWord)
        for i in range(len(wordList)):
            word = wordList[i]
            potential = generatePotential(word)
            for p in potential:
                if p not in graph:
                    graph[p] = []
                graph[p].append(word)
        visited = set()
        queue = deque([[beginWord]])
        visited.add(beginWord)
        res = []
        check = False
        while queue:
#            print (queue)
            size = len(queue)
            globalSubset = set()
            for i in range(size):
                nodeList = queue.popleft()
                node = nodeList[-1]
                if node == endWord:
                    res.append(nodeList)
                    check = True
                potential = generatePotential(node)
                subset = set()
                for p in potential:
                    for neighbor in graph[p]:
                        if neighbor not in visited and neighbor not in subset:
                            subset.add(neighbor)
                            newList = nodeList[:]
                            newList.append(neighbor)
                            queue.append(newList)
                globalSubset.union(subset)
            visited.union(globalSubset)
            if check:
                break
        return res
def generatePotential(w):
    res = []
    for i in range(len(w)):
        res.append("{}*{}".format(w[:i],w[i+1:]))
    return res
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
solution = Solution()
print (solution.findLadders(beginWord,endWord,wordList))