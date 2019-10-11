# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 01:40:37 2019

@author: huyn
"""

#Strobogrammatic Number II
def findStrobogrammatic(n: int) :
    mapping = {"1":"1","8":"8","9":"6","6":"9","0":"0"}
    if n ==0 :
        return [""]
    elif n==1:
        return ["1","8","0"]
    res = set()
    def dfs(path,index):
        if index == n//2:
            string = "".join(path)
            reverseString = ""
            for item in string[::-1]:
                reverseString+=mapping[item]
            if n%2:
                string1 = string+"1"+reverseString
                res.add(string1)
                string2 = string+"8"+reverseString
                res.add(string2)
                string3 = string+"0"+reverseString
                res.add(string3)
            else:
                string1 = string+reverseString
                res.add(string1)
                string2 = string+reverseString
                res.add(string2)                    
        elif index<n//2:
            if index ==0:
                for item in mapping:
                    if item!="0":
                        path.append(item)
                        dfs(path,index+1)
                        path.pop()
            else:
                for item in mapping:

                    path.append(item)
                    dfs(path,index+1)
                    path.pop()
    dfs([],0)
    return [item for item in res]    