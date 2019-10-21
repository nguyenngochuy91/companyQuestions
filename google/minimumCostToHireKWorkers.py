# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:25:00 2019

@author: huyn
"""

#Minimum Cost to Hire K Workers
#There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
#
#Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:
#
#Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
#Every worker in the paid group must be paid at least their minimum wage expectation.
#Return the least amount of money needed to form a paid group satisfying the above conditions.
from typing import List
def mincostToHireWorkers(quality: List[int], wage: List[int], K: int) -> float:
    
    return