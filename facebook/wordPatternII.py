# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 03:39:55 2019

@author: huyn
"""

#291. Word Pattern II
#Given a pattern and a string str, find if str follows the same pattern.
#
#Here follow means a full match, such that there is a bijection between a letter
# in pattern and a non-empty substring in str.

def wordPatternMatchNaive(pattern: str, string: str) -> bool:
    def dfs(pToS,StoP,indexPattern,indexString):
        if indexPattern==len(pattern) and indexString==len(string):
#            print (pToS,StoP)
            return True
        elif indexPattern<len(pattern) and indexString<len(string):
            # we can keep traverse
            p = pattern[indexPattern]
            if p in pToS:
                #check if it maps out for the string
                for letter in pToS[p]:
                    if indexString == len(string):
#                        print (26,pToS,StoP,indexPattern,indexString)
                        return False 
                    else:
                        if letter!=string[indexString]:
#                            print (30,pToS,StoP,indexPattern,indexString)
                            return False
                    indexString+=1
                # if maps is ok, check the nextone
                return dfs(pToS,StoP,indexPattern+1,indexString)
            else:
                # we will have to scale the string to all possible that can map p
                for i in range(indexString,len(string)):
                    potentialMap = string[indexString:i+1]
                    if potentialMap not in StoP: # it has to be somethign that was not map string to pattern
                        pToS[p]            = potentialMap
                        StoP[potentialMap] = p
                        check = dfs(pToS,StoP,indexPattern+1,i+1)
                        # pop
                        pToS.pop(p)
                        StoP.pop(potentialMap)
                        if check:
                            return True
#                print (46,pToS,StoP,indexPattern,indexString)
                return False
        else:
            return False
            
    return dfs({},{},0,0)
def wordPatternMatchAll(pattern: str, string: str) -> bool:
    res = []
    def dfs(pToS,StoP,indexPattern,indexString):
        if indexPattern==len(pattern) and indexString==len(string):
            temp = []
            for key in pToS:
                temp.append((key,pToS[key]))
            res.append(temp)
        elif indexPattern<len(pattern) and indexString<len(string):
            # we can keep traverse
            p = pattern[indexPattern]
            if p in pToS:
                #check if it maps out for the string
                for letter in pToS[p]:
                    if indexString == len(string):
#                        print (26,pToS,StoP,indexPattern,indexString)
                        return False 
                    else:
                        if letter!=string[indexString]:
#                            print (30,pToS,StoP,indexPattern,indexString)
                            return False
                    indexString+=1
                # if maps is ok, check the nextone
                return dfs(pToS,StoP,indexPattern+1,indexString)
            else:
                # we will have to scale the string to all possible that can map p
                for i in range(indexString,len(string)):
                    potentialMap = string[indexString:i+1]
                    if potentialMap not in StoP: # it has to be somethign that was not map string to pattern
                        pToS[p]            = potentialMap
                        StoP[potentialMap] = p
                        check = dfs(pToS,StoP,indexPattern+1,i+1)
                        # pop
                        pToS.pop(p)
                        StoP.pop(potentialMap)
                        if check:
                            return True
#                print (46,pToS,StoP,indexPattern,indexString)
                return False
        else:
            return False
            
    dfs({},{},0,0)
    return res
pattern = "abab"
string = "redblueredblue"
print (wordPatternMatchAll(pattern,string))
pattern = pattern = "aaaa"
string = "asdasdasdasd"
print (wordPatternMatchAll(pattern,string))
pattern = "aabb"
string = "xyzabcxzyabc"
print (wordPatternMatchAll(pattern,string))