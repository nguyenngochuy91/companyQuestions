# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 23:43:24 2019

@author: huyn
"""

#123456789 = K
def target(k):
    letter = "123456789"
    res = []
    def dfs(index,currentVal,k,path):
        if index==len(letter):
            if currentVal ==k:
                res.append("".join(path))
        else:
            for i in range(index,len(letter)):
                val = int(letter[index:i+1])
                # -
                currentVal-=val
                path.append("-")
                path.append(letter[index:i+1])
                dfs(i+1,currentVal,k,path)
                currentVal+=val
                path.pop()
                path.pop()
                # +
                currentVal+=val
                path.append("+")
                path.append(letter[index:i+1])
                dfs(i+1,currentVal,k,path)
                currentVal-=val
                path.pop()
                path.pop()
    for i in range(len(letter)):
        val = int(letter[:i+1])
        dfs(i+1,-val,k,["-"+letter[:i+1]])
        dfs(i+1,val,k,[letter[:i+1]])
    return res

#print (target(100))