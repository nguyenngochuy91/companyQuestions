# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:28:22 2019

@author: huyn
"""
import random
#273. Integer to English Words
#Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
def numberToWords(num):
    if not num:
        return "Zero"
    single_digits = ["", "One", "Two", "Three",  
                     "Four", "Five", "Six", "Seven",  
                     "Eight", "Nine"] 
  
    # The first string is not used,  
    # it is to make array indexing simple  
    two_digits = ["Ten", "Eleven", "Twelve",  
                  "Thirteen", "Fourteen", "Fifteen",  
                  "Sixteen", "Seventeen", "Eighteen", 
                  "Nineteen"] 
  
    # The first two string are not used, 
    # they are to make array indexing simple 
    tens_multiple = ["Twenty", "Thirty", "Forty", 
                     "Fifty", "Sixty", "Seventy", "Eighty",  
                     "Ninety"]
  
    tens_power = ["", "Thousand","Million","Billion"]
    hundred    = "Hundred"
    myList     = []
    index = 0
    single     = []
    while num:
        val = tens_power[index]
        if val:
            single.append(val)
        # we will take 3 number from right, each time
        firstDigit = num%10
        num        = num//10
        val        = single_digits[firstDigit]
        if num:
            secondDigit = num%10
            num         = num//10
            if secondDigit==0:
                if val:
                    single.append(val)
            elif secondDigit==1:
                single.append(two_digits[firstDigit])
            else:
                if val:
                    single.append(val)
                single.append(tens_multiple[secondDigit-2])
        else:
            # only 1 digit
            if val:
                single.append(val)
        if num:
            thirdDigit = num%10
            num        = num //10
            # have 3 digit
            if thirdDigit:
                single.append(hundred)
            val  = single_digits[thirdDigit]
            if val:
                single.append(val)
        index+=1
        if len(single)>1 or (len(single)==1 and single[0] not in tens_power):
            myList.extend(single)
        single = []
#    print (myList)
    return " ".join(myList[::-1])
#for i in range(100):
#    print (random.randint(0,2**10))