# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:00:27 2019

@author: Huy Nguyen
"""

#Spaced permutations
#Given an integer n, create an array such that each value is repeated twice.
def generateRepeate(n):
    arr =[]
    for i in range(1,n+1):
        for j in range(2):
            arr.append(i)
    return arr

#Follow up 1: After creating it, find a permutation such that each number is spaced in
# such a way, they are at a "their value" distance from the second occurrence of the same number. 
# Return any 1 permutation if it exists. Empty array if no permutation exists.
    
#Input: n = 3 --> This is the array - [1, 1, 2, 2, 3, 3]
#Output: [3, 1, 2, 1, 3, 2]
#Explanation:
#The second 3 is 3 digits away from the first 3. 
#The second 2 is 2 digits away from the first 2. 
#The second 1 is 1 digit away from the first 1
def findPermutation(n):
    arr = [0]*(2*n)
    def dfs(num):
        if num ==0:
            return True
        for i in range(2*n-num-1):
            try:
                if arr[i]==0 and arr[i+num+1]==0:
                    arr[i],arr[i+num+1] = num,num
                    check = dfs(num-1)
                    if check:
                        return True
                    arr[i],arr[i+num+1] = 0,0
            except:
                continue
        return False
    if dfs(n):
        return arr
    return False
#print (findPermutation(1))
#
#print (findPermutation(2))

#for i in range(1,11):
#    print (findPermutation(i))
    
#Follow up 2: Return all possible permutations.
def findAllPermute(n):
    res = []
    arr = [0]*(2*n)
    def dfs(num,arr):
        if num ==0:
            t= []
            for num in arr:
                t.append(num)
            res.append(t)
        for i in range(2*n-num-1):
            try:
                if arr[i]==0 and arr[i+num+1]==0:
                    arr[i],arr[i+num+1] = num,num
                    dfs(num-1,arr)
                    arr[i],arr[i+num+1] = 0,0
            except:
                continue
    dfs(n,arr)
    if res:
        return res
    return False

#print (findAllPermute(8))