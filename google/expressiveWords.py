# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:06:53 2019

@author: huyn
"""

#Expressive Words
#Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
#In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
#
#For some given string S, a query word is stretchy if it can be made to be equal to S by any number of 
#applications of the following extension operation: choose a group consisting of characters c, and add 
#some number of characters c to the group so that the size of the group is 3 or more.
#
#For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", 
#but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another 
#extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" 
#would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
#
#Given a list of query words, return the number of words that are stretchy. 
from typing import List
S = "heeellooo"
words = ["hello", "hi", "helo"]
def expressiveWords(S: str, words: List[str]) -> int:
    if not S:
        return 0
    s = helper(S)
    count = 0
    for word in words:
        w = helper(word)
        if len(w)== len(s):
            check = True
            for i in range(len(w)):
                letterW,countW = w[i]
                letterS,countS = s[i]
                if letterW != letterS:
                    check = False
                    break
                if countW>countS:
                    check = False
                    break
                if countS<3 and countW != countS:
                    check = False
                    break
            if check:
                count += 1
    return count
        
def helper(string):
    s = []
    current = string[0]
    count = 1
    for i in range(1,len(string)):
        if string[i] == current:
            count += 1
        else:
            s.append((current,count))
            current = string[i]
            count = 1
    s.append((current,count))
    return s
