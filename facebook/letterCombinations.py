# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:57:31 2019

@author: huyn
"""

#Letter Combinations of a Phone Number
#You are given two parameters * A mapping from digits (represented as strings or chars) to a list of letters.
#You want to return all the possible ways to replace each digit in the input string with its respective letters 
#from the mapping.
mapping = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L'] }
def phone_permute_DFS(digits, mapping):
    if not digits:
        return []
    res = []
    mapping = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL' ,
              '6':'MNO','7': 'PQRS','8':'TUV','9':'WXYZ'}
    def dfs(index,path):
        if index==len(digits):
            res.append("".join(path))
        else:
            for letter in mapping[digits[index]]:
                path.append(letter.lower())
                dfs(index+1,path)
                path.pop()
    dfs(0,[])
    return res
def phone_permute_iteration(digits,mapping):
    res = [""]
    for digit in digits:
        temp =[]
        for item in res:
            for letter in mapping[digit]:
                temp.append(item+letter)
        res = temp
    return res
digits ="123"
comb=phone_permute_iteration(digits,mapping)
def verifier(digits,comb):
    reverseMap = {letter:key for key in mapping for letter in mapping[key]}
    for combination in comb:
        if len(combination)!=len(digits):
            return False
        for i in range(len(digits)):
            if reverseMap[combination[i]]!=digits[i]:
                return False
    count = len(mapping[digits[0]])
    for digit in digits[1:]:
        count*=len(mapping[digit])
    
    return count == len(comb)

#print (verifier(digits,comb))