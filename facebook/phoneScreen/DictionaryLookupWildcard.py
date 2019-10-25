# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:05:48 2019

@author: huyn
"""
#There are two parts to this question. The first is a function called setup that 
#takes a list of words. In this function, you have a chance to preprocess the list of words 
#in order to solve and improve the runtime of the second part which is a function called isMember. 
#isMember takes in a string and returns whether or not that string exists in the list of words. 
#isMember may also contain one or more dots (.) which is a wildcard that matches exactly one character 
#of any value in setup at the current index of the string.
#Examples
#
#setup(["foo", "bar", "baz"]);
#isMember("foo"); # returns true
#isMember("garply"); # returns false because "garply" is not in the dictionary
#isMember("f.o"); # returns true (it matches foo where the '.' matches the first 'o')
#isMember(".."); # returns false (there are no two-letter words)

#Clarifying questions
#
#setup is a one time call and isMember is called many times. So while time spent 
#is setup should be reasonable, time spent in isMember is the most important thing.
#Only lowercase alphabetical characters will exist in the list of words in setup.
# The argument to isMember is also only lowercase alphabetical characters as well as the dot 
# (.) representing the wildcard.

# support keep add e the dictionary, keep count howmany with this index
class Trie:
    def __init__(self):
        self.root = {}
    def addWord(self,word):
        root = self.root
        for letter in word:
            if letter not in root:
                root[letter] = {}
            if "?" not in root:
                root["?"]=0
            root["?"]+=1
            root = root[letter]
        # not chunking if there is only
        root["#"]=1
        root["?"]=1
        # we intialize count down here
    def search(self,word):
        def dfs(word,index,currentRoot):
            if index==len(word):
                if "#" in currentRoot:
                    return True
                else:
                    return False
            elif index<len(word):
                letter = word[index]
                if letter!=".":
                    if letter in currentRoot:
                        return dfs(word,index+1,currentRoot[letter])
                    else:
                        return False
                else:
                    for possibleLetter in currentRoot:
                        if letter !="#":
                            if dfs(word,index+1,currentRoot[possibleLetter]):
                                return True
                    return False
        return dfs(word,0,self.root)     
    def count(self,suffix):
        def dfs(word,index,currentRoot):
            if index == len(word):
                return currentRoot["?"]
            elif index<len(word):
                count = 0
                letter = word[index]
                if letter!=".":
                    if letter in currentRoot:
                        count+=dfs(word,index+1,currentRoot[letter])

                else:
#                    print ("currentRoot",currentRoot)
                    for possibleLetter in currentRoot:
                        if possibleLetter not in "?#":
                            # pawn a thread
#                            print ("possibleLetter",possibleLetter)
                            count+= dfs(word,index+1,currentRoot[possibleLetter])
                return count
        return dfs(suffix,0,self.root)
        
# function that takes in a list of string, return a Trie object that store info
def setup(wordList):
    myTrie = Trie()
    for word in wordList:
        myTrie.addWord(word)
    return myTrie
myTrie = setup(["foo", "bar", "baz","abcdfegre","footootoolo","fool","foutain","faol"])
print (myTrie.count("b.."))
print (myTrie.count("f.."))
print (myTrie.count("fo."))
print (myTrie.count("f..l"))
# function search that takes in a word and check if it is store in my Trie
def isMember(word,myTrie):
    # a function that dfs through myTrie and find a path that might return True
    def dfs(word,index,currentRoot):
        if index==len(word):
            if "#" in currentRoot:
                return True
            else:
                return False
        elif index<len(word):
            letter = word[index]
            if letter!=".":
                if letter in currentRoot:
                    return dfs(word,index+1,currentRoot[letter])
                else:
                    return False
            else:
                for possibleLetter in currentRoot:
                    if letter !="#":
                        if dfs(word,index+1,currentRoot[possibleLetter]):
                            return True
                return False
    return dfs(word,0,myTrie.root)
#print (isMember("foo",myTrie))
#print (isMember("garply",myTrie))
#print (isMember("f.o",myTrie))
#print (isMember("..",myTrie))
#print (isMember("",myTrie))

# class trie that will chunk word together, might not support update
class TrieChunking:
    def __init__(self,wordList):
        self.root = {}
    def addWord(self,word):
        def dfs(dictionary,word,index):
            return
        
            