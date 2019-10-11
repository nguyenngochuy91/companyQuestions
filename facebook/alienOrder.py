# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:43:09 2019

@author: huyn
"""
#269. Alien Dictionary
#There is a new alien language which uses the latin alphabet. However, the order
# among letters are unknown to you. You receive a list of non-empty words from the dictionary,
# where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.
def alienOrder(words):
    res = []
    parents = {} # map the backward edge to check whether a character should be a start node
    neighbors = {} # store the forward edge
    for word in words:
        for letter in word:
            if letter not in parents:
                parents[letter]=set()
            if letter not in neighbors:
                neighbors[letter] = set()
    # 
    for i in range(len(words)-1):
        w1 = words[i]
        for j in range(i+1,len(words)):
            w2 = words[j]
            for k in range(min(len(w1),len(w2))):
                if w1[k]==w2[k]:
                    continue
                elif w1[k]!=w2[k]:
                    smaller = w1[k]
                    larger =  w2[k]                     
                    # set up neighbor that map smaller to larger
                    # make parents as set so we can remove the parent from each node faster
                    neighbors[smaller].add(larger)
                    parents[larger].add(smaller)
                    
                    # remember to break
                    break
    startNodes = [node for node in parents if len(parents[node])==0]
    # we keep pop out startnodes 
    while startNodes:
        node = startNodes.pop()
        # add this to res, we know for sure it is equal or less to everything on the left
        res.append(node)
        # for each neighbor, remove edge from neighbor to node as parent
        for neighbor in neighbors[node]:
            # remove edge
            parents[neighbor].remove(node)
            # if there are no more parents of neighbor, add it to start node
            if not parents[neighbor]:
                startNodes.append(neighbor)
    # we check if there are some edges for any key in parents node
    for node in parents:
        if parents[node]:
            return ""
    return "".join(res)
        
#words = ["ab","adc"]
#words = ["z","z"]
#print (alienOrder(words))
