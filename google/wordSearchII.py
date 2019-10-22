# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:19:55 2019

@author: huyn
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie= Trie(board,words)
        return myTrie.res

class Trie:
    def __init__(self,board,words):
        self.d= {}
        self.initialize(words)
        self.res =self.search(board)
    def isValidGrid(self,currentRow,currentCol,row,col):
        return currentCol<col and currentRow<row and currentCol>=0 and currentRow >=0
    def addWord(self,word):
        root = self.d
        for letter in word:
            if letter not in root:
                root[letter]={}
            root = root[letter]
        #need "#"
        root["#"]=1
#        root["?"] = 0 # have check this already
    def initialize(self,words):
        for word in words:
            self.addWord(word)
        
    def search(self,board):
        row = len(board)
        col = len(board[0])
        root = self.d
        visited = set()
        res = set()
        # store path to output a word
        def dfs(currentRow,currentCol,visited,currentRoot,path):
            if "#" in currentRoot: # we hit a word
                res.add("".join(path))
            temp = [(1,0),(0,1),(-1,0),(0,-1)]
            for x,y in temp:
                if self.isValidGrid(currentRow+x,currentCol+y,row,col) and (currentRow+x,currentCol+y) not in visited:
                    letter = board[currentRow+x][currentCol+y]
                    if letter in currentRoot:
#                        print (currentRow+x,currentRow+y,letter)
                        visited.add((currentRow+x,currentCol+y))
                        path.append(board[currentRow+x][currentCol+y])
                        dfs(currentRow+x,currentCol+y,visited,currentRoot[letter],path)
                        path.pop()
                        visited.remove((currentRow+x,currentCol+y))
        for r in range(row):
            for c in range(col):
                letter = board[r][c]
                if letter in root:
#                    print (65,r,c,letter)
                    visited.add((r,c))
                    path= [letter]
                    dfs(r,c,visited,root[letter],path)
                    visited.remove((r,c))
        return list(res)