# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 02:27:24 2019

@author: huyn
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for letter in word:
            if letter not in root:
                root[letter]= {}
            root = root[letter]
        root["#"]= 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        root = self.root
        def dfs(index,root):
            if index==len(word):
                if "#" in root:
                    return True
                return False
            elif index<len(word):
                letter = word[index]
                if letter == ".":
                    for potential in root:
                        if potential!="#":
                            check = dfs(index+1,root[potential])
                            if check:
                                return True
                    return False
                else:
                    if letter in root:
                        return dfs(index+1,root[letter])
                    else:
                        return False
        return dfs(0,root)
myWord = WordDictionary()
myWord.addWord("bad")
myWord.addWord("dad")
myWord.addWord("mad")
print (myWord.search("pad")) 
print (myWord.search("bad")) 
print (myWord.search(".ad")) 
print (myWord.search("b..")) 