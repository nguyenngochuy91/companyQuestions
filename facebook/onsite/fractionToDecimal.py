# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:47:50 2019

@author: huyn
"""
"""
166. Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses."""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator == 0:
            return str(numerator//denominator)
        res = [str(numerator//denominator),"."]
        numerator = abs(numerator)
        denominator = abs(denominator)
        left = numerator%denominator*10
        if left == 0:
            res.append("0")
            return ",".join(res)
        else:
            index = 0
            d = {}
            v = set()
            # we increase our numerator until it is larger or equal to our denominator
            while left <denominator:
                res.append("0")
                left*=10
            # we break out the loop once we are greater or equal
            repeated = False
            while True:
                val = left//denominator
                left = left%denominator
                print (left)
                if left in v:
                    # we found our repeated
                    repeated = True
                    break
                else:
                    if left == 0: 
                        break
                    else:
                        d[index] = str(val)
                        index += 1
                        v.add(left)
                        left*=10
                        
            print (res,d,v)
            string = "".join([d[i] for i in range(len(d))])
            if repeated:
                res.append("(")
                res.append(string)
                res.append(")")
            else:
                res.append(string)
        return "".join(res)
    
solution = Solution()
print(solution.fractionToDecimal(2,11))