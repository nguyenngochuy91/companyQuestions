# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:05:51 2019

@author: huyn
"""
#Candy
#
#There are N children standing in a line. Each child is assigned a rating value.
#
#You are giving candies to these children subjected to the following requirements:
#
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#What is the minimum candies you must give?
import random
class Solution(object):
    # O(n^2)
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        arr = [1]
        for i in range(1,len(ratings)):
            # if greater than our currentLast, assing last +1
            if ratings[i]>ratings[i-1]:
                arr.append(arr[-1]+1)
            # if equal, assign 1
            elif ratings[i] == ratings[i-1]:
                arr.append(1)
            else:
                # if new is less
                # if our last is not 1, just assign 1
                if arr[-1]>1:
                    arr.append(1)
                # if last is 1, have to modify
                else:
                    # we from index i the left for the monotonic increase, until it decrease
#                    print (i,arr)
                    arr.append(1)
#                    print (i,arr)
                    for j in range(i,-1,-1):
                        if j == 0:
                            break
                        # we only change if our rating j-1 is better while our candy at j-1 is equal or less
                        if ratings[j]<ratings[j-1] and arr[j-1]<=arr[j]:
                            arr[j-1]+=1
                        else:
                            break

        return arr
def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,10))
    return arr
for i in range(10):
    arr = generate(5)
    print (arr)
#sol = Solution()
#print (sol.candy(arr))
def candy2List(ratings):
    s = 0
    left = []
