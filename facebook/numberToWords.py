# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:28:22 2019

@author: huyn
"""

#273. Integer to English Words
#Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
def numberToWords(num):
    single_digits = ["Zero", "One", "Two", "Three",  
                     "Four", "Five", "Six", "Seven",  
                     "Eight", "Nine"] 
  
    # The first string is not used,  
    # it is to make array indexing simple  
    two_digits = ["", "Ten", "Eleven", "Twelve",  
                  "Thirteen", "Fourteen", "Fifteen",  
                  "Sixteen", "Seventeen", "Eighteen", 
                  "Nineteen"] 
  
    # The first two string are not used, 
    # they are to make array indexing simple 
    tens_multiple = ["", "", "Twenty", "Thirty", "Forty", 
                     "Fifty", "Sixty", "Seventy", "Eighty",  
                     "Ninety"]
  
    tens_power = ["Hundred", "Thousand","Million","Billion"]
    
    return