# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:28:22 2019

@author: huyn
"""

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        # have a string that building by input c
        self.string = ""
        # have a trie that store what we have for sentences
        self.d = {}
        for i in range(len(sentences)):
            sentence,time = sentences[i],times[i]
            self.initialize(sentence,time)
#        print (self.d)
    # given a sentence, we input this into our dictionary
    def initialize(self,sentence,time):
        root = self.d
        for letter in sentence:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        if "#" not in root:
            root["#"] = [time,sentence]
        else:
            root["#"][0] += time
        return

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.initialize(self.string,1)
            self.string = ""
            return []
        else:
            self.string += c
            res = []
            root = self.d
            # we first traverse the letter in string until 
            # either run out of the string, or we can't find in root
            found = True
            for letter in self.string:
                if letter in root:
                    root = root[letter]
                else:
                    found = False
            if not found: # not found, just return []
                # we add tgus strubg ti iyr d
                return []
            else:
                # if found, we will find all the string that have the currentPrefix
                res = []
                def dfs(root):
                    for char in root:
                        if char == "#":

                            time,sentence = root[char]
                            res.append([-time,sentence])
                        else:
                            dfs(root[char])
                dfs(root)

                res.sort()
                return [item[1] for item in res][:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)