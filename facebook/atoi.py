# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:23:36 2019

@author: huyn
"""

#myAtoi
def myAtoi(string: str) -> int:
    numeric = []
    d ={'7': 7, '3': 3, '8': 8, '6': 6, '5': 5, '2': 2, '1': 1, '4': 4, '9': 9, '0': 0}
    for letter in string:
        if letter.isalpha():
            break
        elif letter ==" " and not numeric:
            continue
        elif letter ==" " and numeric:
            break
        elif letter.isnumeric():
            numeric.append(letter)
        elif (letter =="-" or letter =="+") and not numeric:
            if letter =="-" :
                numeric.append("-")
            else:
                numeric.append("+")
                    
        else:
            break
    isNeg= False
    if not numeric:
        return 0
    if numeric[0]=="-" or numeric[0]=="+":
        if numeric[0]=="-":
            isNeg= True
        numeric.pop(0)
    # we go to the first numeric that is not 0
    while numeric:
        if numeric[0]=="0":
            numeric.pop(0)
        else:
            break
    val = 0

    while numeric:
        val=val*10+d[numeric.pop(0)]
        
    if isNeg:
        return max(-2147483648,-val)
    return min(val,2147483647)