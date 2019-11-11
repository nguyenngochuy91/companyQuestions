# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:16:04 2019

@author: huyn
"""
"""
Given 2 lists a and b. Each element is a pair of integers where the first integer 
represents the unique id and the second integer represents a value. Your task is to find an element 
from a and an element form b such that the sum of their values is less or equal to target and as close 
to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.
Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
"""

def findPairs(a,b,target):
    res = []
    dA = {}
    dB = {}
    for key,val in a:
        if val not in dA:
            dA[val] = []
        dA[val].append(key)
    for key,val in b:
        if val not in dB:
            dB[val] = []
        dB[val].append(key)    
    listA, listB = sorted(dA),sorted(dB)
#    print (listA)
#    print (listB)
    closest = None
    start ,stop = 0, len(listB)-1
    while start<len(listA) and stop >=0 :
        val = listA[start] + listB[stop]
        if val > target: # we have to decrease stop
            stop -= 1
        elif val <= target:
            if closest == None:
                closest = val
                res.append((listA[start],listB[stop]))
            else:
                if closest == val:
                    res.append((listA[start],listB[stop]))
                elif val > closest: 
                    closest = val
                    res = [(listA[start],listB[stop])]
            if val < target:
                start += 1
            else:
                start += 1
                stop -= 1

    output = []
    for val1,val2 in res:
        list1 = dA[val1]
        list2 = dB[val2]
        for key1 in list1:
            for key2 in list2:
                output.append((key1,key2))
    return output
#a = [[1, 3], [2, 5], [3, 7], [4, 10]]
#b = [[1, 2], [2, 3], [3, 4], [4, 5]]
#target = 10
#print (findPairs(a,b,target))
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
print (findPairs(a,b,target))
#a = [[1, 8], [2, 15], [3, 9]]
#b = [[1, 8], [2, 11], [3, 12]]
#target = 20
#print (findPairs(a,b,target))
#a = [[1, 1], [2, 1], [3, 3],[4, 3],[5,2],[6,4],[7,5],[8,5]]
#b = [[1,5],[2,6],[3,7],[4,8],[5,9],[6,10]]
#target = 10
#print (findPairs(a,b,target))