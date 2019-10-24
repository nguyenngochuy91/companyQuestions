# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 03:16:50 2019

@author: Huy Nguyen
"""
# coin change
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    d = {0:0}
    coins.sort()
    for currentAmount in range(1,amount+1):
        for coin in coins:
            if currentAmount >= coin:
                left = currentAmount - coin
                if left in d:
                    if currentAmount not in d:
                        d[currentAmount] = d[left]+1
                    d[currentAmount] = min(d[currentAmount],d[left]+1)
            else:
                break
    if amount not in d:
        return -1
    return d[amount]