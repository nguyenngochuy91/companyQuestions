# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 02:47:41 2019

@author: huyn
"""
"""
224. Basic Calculator
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or 
minus sign -, non-negative integers and empty spaces ."""
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        num = ""
        
        for char in s:
            if char.isdigit():
                num += char
            else:
                if char == "+":
        return res
solution = Solution()
string ="(1+(4+5-2)-(2+3))+(6+8)"