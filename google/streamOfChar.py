# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:39:38 2019

@author: huyn
"""
"""
1032. Stream of Characters
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried 
(in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
"""
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # set up a set of reference to the beginning for each of the word
        self.wordRoot = []
        for w in words:
            firstLetter = w[0]
            trie = Trie(firstLetter)
            head = trie
            for letter in w[1:]:
                nextTrie = Trie(letter)
                trie.next = nextTrie
                nextTrie.prev = trie
                trie = nextTrie
            self.wordRoot.append(head)
    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        check = False
        for index,trie in enumerate(self.wordRoot):
            if trie.letter == letter:
                if not trie.next:
                    check = True
                    # reset the pointer
                    while trie.prev:
                        trie = trie.prev
                else:
                    trie = trie.next
#                    print ("found",index,letter,trie.letter)
            else:
                while trie.prev:
                    trie = trie.prev
                if trie.letter == letter:
                    trie = trie.next
            self.wordRoot[index] = trie
        return check
class Trie:
    def __init__(self,letter,isDone = False,next = None,prev = None):
        self.letter = letter
        self.next = next
        self.prev = prev
    
streamChecker = StreamChecker(["baa","aa","aaaa","abbbb","aba"])
print (streamChecker.query('a'))
print (streamChecker.query('a'))
print (streamChecker.query('a'))
