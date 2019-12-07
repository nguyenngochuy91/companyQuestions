# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:57:10 2019

@author: huyn
"""

#1061. Lexicographically Smallest Equivalent String
#Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters. 
#For example, if A = "abc" and B = "cde", then we have 'a' == 'c', 'b' == 'd', 'c' == 'e'.
#
#Equivalent characters follow the usual rules of any equivalence relation:
#
#Reflexivity: 'a' == 'a'
#Symmetry: 'a' == 'b' implies 'b' == 'a'
#Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'
#For example, given the equivalency information from A and B above, S = "eed", "acd", and "aab" 
#are equivalent strings, and "aab" is the lexicographically smallest equivalent string of S.
#
#Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        graph = {}
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            graph[a].add(b)
            graph[b].add(a)
        cc = []
        visited = set()
        for letter in graph:
            if letter not in visited:
                queue = [letter]
                visited.add(letter)
                current = [letter]
                while queue:
                    node = queue.pop()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            current.append(neighbor)
                            queue.append(neighbor)
                cc.append(current)
        graph = {}
        for current in cc:
            m = min (current)
            for letter in current:
                graph[letter] = m
        output = ""
        for letter in S:
            if letter not in graph:
                output+=letter
            else:
                output+=graph[letter]
        return output