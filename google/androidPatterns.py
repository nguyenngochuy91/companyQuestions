# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 02:48:04 2019

@author: huyn
"""

#Android Unlock Patterns
#Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, 
#count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys 
#and  maximum n keys.
#Rules for a valid pattern:
#
#Each pattern must connect at least m keys and at most n keys.
#All the keys must be distinct.
#If the line connecting two consecutive keys in the pattern passes through any other keys, 
#the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
#The order of keys used matters.
#Invalid move: 4 - 1 - 3 - 6
#Line 1 - 3 passes through key 2 which had not been selected in the pattern.
#
#Invalid move: 4 - 1 - 9 - 2
#Line 1 - 9 passes through key 5 which had not been selected in the pattern.
#
#Valid move: 2 - 4 - 1 - 3 - 6
#Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
#Valid move: 6 - 5 - 4 - 1 - 9 - 2
#Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
def numberOfPatterns(m: int, n: int) -> int:
    check = {(1,9):5,(9,1):5,(2,8):5,(8,2):5,(3,7):5,(7,3):5,(4,6):5,(6,4):5,
             (1,3):2,(3,1):2,(7,9):8,(9,7):8,(1,7):4,(7,1):4,(3,9):6,(9,3):6}
    res = [] # storing good path at step k
    visited = set()
    def dfs(index,path,m):
        if index == m:
            res.append(path[:])
        elif index<m:
            for i in range(1,10):
                last = path[-1]
                if i not in visited:
                    if (last,i) in check:
                        if check[(last,i)] in visited:
                            visited.add(i)
                            path.append(i)
                            dfs(index+1,path,m)
                            path.pop()
                            visited.remove(i)
                            
                    else:                       
                        visited.add(i)
                        path.append(i)
                        dfs(index+1,path,m)
                        path.pop()  
                        visited.remove(i)
    for i in range(1,10):
#        print (i,visited)
#        print ("starting",i)
        visited.add(i)
        dfs(1,[i],m)
        visited.remove(i)
#    print (res)
#    print (len(res))
    # now for each step from m+1, to n, we increment the count, also update our res
    count = len(res)
    for j in range(m,n):
#        print (res)
        newRes = []
        for path in res:
            lastNum = path[-1]
            for i in range(1,10):
                if i not in path:
                    if (lastNum,i) in check:
                        if check[(lastNum,i)] in path:
                            temp = path[:]
                            temp.append(i)
                            newRes.append(temp)
                    else:
                        temp = path[:]
                        temp.append(i)
                        newRes.append(temp)
        res = newRes
        count += len(res)
#    print (res)
    return count
m = 1
n = 9
print (numberOfPatterns(m,n))