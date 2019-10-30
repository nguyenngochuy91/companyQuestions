# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 02:16:42 2019

@author: huyn
"""
"""
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral 
for four is not IIII. Instead, the number four is written as IV. Because the one is before the five 
we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999."""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        single = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
        v = {'X': 10, 'D': 500, 'V': 5, 'L': 50, 'M': 1000, 'I': 1, 'C': 100}
        res = []
        while num:
            res.append(num%10)
            num //= 10

        string = []
        for index,num in enumerate(res):
            if num == 0:
                continue
            small = single[num]
            newLetter = ""
            for letter in small:
                newLetter += d[v[letter]*10**index]
            string.append(newLetter)
        return "".join(string[::-1])
            
                
                

solution = Solution()
for i in range(100,201):
    print(i)
            