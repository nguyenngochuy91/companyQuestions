# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:37:08 2019

@author: huyn
"""

#Word Ladder
#Given two words (beginWord and endWord), and a dictionary's word list, find the length of 
#shortest transformation sequence from beginWord to endWord, such that:
#
#Only one letter can be changed at a time.
#Each transformed word must exist in the word list. Note that beginWord is not a transformed word
from collections import deque
from typing import List
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
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
    queue = deque([beginWord])
    visited.add(beginWord)
    distance = 0
    while queue:
        size = len(queue)
        distance += 1
        for i in range(size):
            node = queue.popleft()
            if node == endWord:
                return distance
            potential = generatePotential(node)
            for p in potential:
                for neighbor in graph[p]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return 0
def generatePotential(w):
    res = []
    for i in range(len(w)):
        res.append("{}*{}".format(w[:i],w[i+1:]))
    return res
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print (ladderLength(beginWord,endWord,wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print (ladderLength(beginWord,endWord,wordList))