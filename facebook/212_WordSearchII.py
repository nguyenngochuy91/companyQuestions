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
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    myTrie= Trie(board,words)
    return myTrie.searchAll(words)

class Trie:
    def __init__(self,board,words):
        self.d= {}
        self.maxLength = max([len(word) for word in words])
        self.initialize(board)
        self.res =self.searchAll(words)
    def isValidGrid(self,currentRow,currentCol,row,col):
        return currentCol<col and currentRow<row and col>=0 and row >=0
    def addWord(self,word):
        root = self.d
        for letter in word:
            if letter not in root:
                root[letter]={}
            root = root[letter]
        # no need for "#"
    def initialize(self,board):
        row = len(board)
        col = len(board[0])
        def dfs(currentLength,maxLength,currentRow,currentCol,row,col,path,visited):
            if currentLength==maxLength:
                self.addWord("".join(path))
            elif currentLength<maxLength:
                temp = [(1,0),(0,1),(-1,0),(0,-1)]
                for x,y in temp:
                    if self.isValidGrid(currentRow+x,currentCol+y,row,col) and (currentRow+x,currentCol+y) not in visited:
                        visited.add((currentRow+x,currentCol+y))
                        path.append(board[currentRow+x][currentCol+y])
                        dfs(currentLength+1,maxLength,currentRow+x,currentCol+y,row,col,path,visited)
                        path.pop()
                        visited.remove((currentRow+x,currentCol+y))
        for r in range(row):
            for c in range(col):
                dfs(1,self.maxLength,r,c,row,col,[board[r][c]],{board[r][c]})
    def search(self,word):
        root = self.d
        for letter in word:
            if letter in root:
                root= root[letter]
            else:
                return False
        return True
    def searchAll(self,words):
        res = []
        for word in words:
            if self.search(word):
                res.append(word)
        return res
            
print (findWords(board,words))
        