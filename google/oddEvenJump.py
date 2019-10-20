# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:30:26 2019

@author: huyn
"""

#Odd Even Jump
#You are given an integer array A.  From some starting index, you can make a series of jumps.  
#The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the 
#(2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.
#
#You may from index i jump forward to index j (with i < j) in the following way:
#
#During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such 
#that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such 
#indexes j, you can only jump to the smallest such index j.
#During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that 
#A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, 
#you can only jump to the smallest such index j.
#(It may be the case that for some index i, there are no legal jumps.)
#A starting index is good if, starting from that index, you can reach the end of 
#the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)
#
#Return the number of good starting indexes.


from typing import List
def oddEvenJumps(A: List[int]) -> int:
    
    return