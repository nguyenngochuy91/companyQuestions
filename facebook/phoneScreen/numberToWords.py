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
    # idea is to break into single digits, two digits and then combine every 3 number
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
    hundred    = "Hundred" # special case that reach to 3 number
    myList     = [] # my main result that store every 3 number
    index = 0 # this index indicate in which ten powers I am at
    single     = [] # store at most 3 number
    while num:
        val = tens_power[index]
        if val: # check if we have reach thousand mark or above
            single.append(val)
        # we will take 3 number from right, each time
        # we take first digit
        firstDigit = num%10
        num        = num//10
        val        = single_digits[firstDigit]
        # we see if we can retrive second digit
        if num:
            secondDigit = num%10
            num         = num//10
            # we start binding our two number, however we need to check if 00, or 0 case
            # if secondigit is 0, we wont add any of our ten multiple
            if secondDigit==0:
                # check if our val is not 0, then we have to append the signe digit first
                if val: 
                    single.append(val)
            # special cases for two digits
            elif secondDigit==1:
                # if it is 1 on the two digit, then we can query the index by the value of our first digit 12->2->twelve
                single.append(two_digits[firstDigit])
            else:
                # if it is not 0, or 1, then we can append firstly our val of not 0
                if val:
                    single.append(val)
                # and then append our secondigit
                single.append(tens_multiple[secondDigit-2]) # or i can set tens_multiple = ["","","Twenty", "Thirty", "Forty", 
#                     "Fifty", "Sixty", "Seventy", "Eighty",  
#                     "Ninety"]
        else:
            # only 1 digit
            if val:
                single.append(val)
        # check if we can pull the third digit
        if num:
            thirdDigit = num%10
            num        = num //10
            # have 3 digit
            # if there is a non 0 at thrird digit, we need the hundred thingy
            if thirdDigit:
                single.append(hundred)
            val  = single_digits[thirdDigit]
            # add the string that correspond to our digit at third place if not 0
            if val:
                single.append(val)
        index+=1
        # there could be a case 000 1, that we should not extedn our single into my list or for cases that we actually have 1 number (1 -> One)
        if len(single)>1 or (len(single)==1 and single[0] not in tens_power):# first len(single)>1 ->1 000 000, single = ["thounsand","milluon one"] 
            myList.extend(single)
        single = []
#    print (myList)
    return " ".join(myList[::-1])
#for i in range(100):
#    print (random.randint(0,2**10))