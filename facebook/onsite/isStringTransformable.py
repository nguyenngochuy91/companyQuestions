# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:18:18 2019

@author: Huy Nguyen
"""
"""
Given an input string and a list of valid words, find if the input can be transformed 
into a valid word by 0 or 1 replacement i.e. at max only 1 character can be replaced to another character
Input: "applo" , ["apple", "apply", "cat", "dog"]
Output: True"""
def isTransformableLength(arr,string):
    size = len(string)
    for str in arr:
        if len(str) == size:
            count = 0
            check = True
            for i in range(size):
                if string[i]!= str[i]:
                    count +=1
                    if count == 2:
                        check= False
                        break
            if check:
                return True
    return False
class Trie:
    def __init__(self,arr):
        self.d = {}
        for string in arr:
            self.add(string)
    def add(self,string):
        root = self.d
        def add(root,string,index,usedStar):
            if index == len(string):
                root["#"] = 1
                return
            letter = string[index]
            if not usedStar:
                if "*" not in root:
                    root["*"] = {}
                add(root["*"],string,index+1,True)
            if letter not in root:
                root[letter] = {}
            add(root[letter],string,index+1,usedStar)
        add(root,string,0,False)
    
    def search(self,query):
        root = self.d
        def dfsSearch(root,query,index,usedStar):
            if index == len(query):
                if "#" in root:
                    return True
                else:
                    return False
            letter = query[index]
            check1 = False
            check2 = False
            if not usedStar:
                check1 = dfsSearch(root["*"],query,index+1,True)
            if letter in root:
                check2 = dfsSearch(root[letter],query,index+1,usedStar)
            return check1 or check2
        return dfsSearch(root,query,0,False)
arr = ["apple", "appqe", "cat", "dog"]
trie = Trie(arr)
print (trie.search("applo"))
print (trie.search("appqf"))
print (trie.search("cam"))
print (trie.search("d"))