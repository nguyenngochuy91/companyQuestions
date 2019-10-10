# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:42:47 2019

@author: Huy Nguyen
"""

#Group anagrams
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = {}
    for word in strs:
        sortedW = "".join(sorted(word))
        if sortedW not in d:
            d[sortedW]=[]
        d[sortedW].append(word)
    return [d[word] for word in d]