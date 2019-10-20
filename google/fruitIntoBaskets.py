# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 02:02:51 2019

@author: huyn
"""

#Fruit Into Baskets
#In a row of trees, the i-th tree produces fruit with type tree[i].
#
#You start at any tree of your choice, then repeatedly perform the following steps:
#
#Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
#Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
#Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
#
#You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
#
#What is the total amount of fruit you can collect with this procedure?
from typing import List
def totalFruit(tree: List[int]) -> int:
    start ,stop = 0,0
    res = 0
    # the idea is using 2 pointers, and check wether we introduce more than 2 key in our dict
    dictionary = {}
    while stop<len(tree):
        currentFruit = tree[stop]
        if currentFruit not in dictionary:
#            print (start,stop,res)
            res = max(stop-start,res)
            # we store the current length first
            while len(dictionary)==2 and start<stop:
                firstFruit = tree[start]
                dictionary[firstFruit]-=1
                if dictionary[firstFruit] == 0:
                    dictionary.pop(firstFruit)
                start += 1
            # the loop escape for sure when len(dic) became 1
            dictionary[currentFruit] = 0
        dictionary[currentFruit] += 1
        stop+=1
    return max(stop-start,res)

tree =[1,2,1]
print (totalFruit(tree))
tree =[0,1,2,2]
print (totalFruit(tree))
tree = [1,2,3,2,2]
print (totalFruit(tree))
tree = [3,3,3,1,2,1,1,2,3,3,4]
print (totalFruit(tree))