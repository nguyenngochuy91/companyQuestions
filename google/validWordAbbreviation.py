# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 02:13:52 2020

@author: huyn
"""
#408. Valid Word Abbreviation
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i ,j =0 ,0
        while i < len(word) and j <len(abbr):
            letter2 = abbr[j]
            if letter2.isalpha():
                letter1 = word[i]
                if letter1!= letter2:
                    return False
                else:
                    i+=1
                    j+=1
                    continue
            else:
                num = 0
                while j<len(abbr):
                    digit = abbr[j]
                    if digit.isdigit():
                        if digit == "0" and num == 0:
                            return False
                        num = num*10 +int(digit)
                        j+=1
                    else:
                        break
                if i+num>len(word):
                    return False
                else:
                    i+=num
        if i >=len(word) and j>=len(abbr):
            return True
        return False