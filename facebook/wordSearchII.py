# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 02:02:25 2019

@author: Huy Nguyen
"""
from typing import List
#212. Word Search II
#Given a 2D board and a list of words from the dictionary, find all words in the board.
#
#Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
#cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
board =[["a","b","c"],["a","e","d"],["a","f","g"]]
words=["baa","baae","aa"]
expected = ["abcdefg","befa","eaabcdgfa","gfedcbaaa","aa","aa"]
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
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
                self.prune(path)
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
        return res
    def prune(self,path): # giving a currentRoot,check if we can prune up the path
        root =self.d
        def dfs(root,path,index):
            letter     = path[index]
            nextRoot   = root[letter]
            # we remove the "#" from root if index == len(path)-1
            if index == len(path)-1:
                nextRoot.pop("#")
                # check if no more letter in nextroot
                if len(nextRoot) == 0:
                    return True
                else:
                    return False
            else: # we keep travers
                noMorePath = dfs(nextRoot,path,index+1)
                if noMorePath:
                    # we can remove the current letter
                    root.pop(letter)
                # check if we can keep delete previous root
                if len(root)==0:
                    return True
                else: # means that either root has a different letter or root has a # sign
                    return False
        dfs(root,path,0)
            
#print (findWords(board,words))
        