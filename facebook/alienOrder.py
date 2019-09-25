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
    res          = []
    parentOfNode = {}
    neighbors    = {}
    for word in words:
        for letter in word:
            if letter not in parentOfNode:
                parentOfNode[letter]=set()
            if letter not in neighbors:
                neighbors[letter] = set()
    for i in range(len(words)-1):
        w1 = words[i]
        for j in range(i+1,len(words)):
            w2 = words[j]
#            print (w1,w2)
            for k in range(min(len(w1),len(w2))):
                if w1[k]==w2[k]:
                    letter = w1[k]
                    continue
                else:
                    parent = w1[k]
                    child  = w2[k]
                    parentOfNode[child].add(parent)
                    neighbors[parent].add(child)
                    break
#    print (parentOfNode)
#    print (neighbors)
    startNode = [node for node in parentOfNode if len(parentOfNode[node])==0]
    while startNode:
        node = startNode.pop()
        res.append(node)
        for neighbor in neighbors[node]:
            parentOfNode[neighbor].remove(node)
            if not parentOfNode[neighbor]:
                startNode.append(neighbor)
#    print (parentOfNode)
    for node in parentOfNode:
        if parentOfNode[node]:
            return ""
    return "".join(res)
#words = ["ab","adc"]
#print (alienOrder(words))
