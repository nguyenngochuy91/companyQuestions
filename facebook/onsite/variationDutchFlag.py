# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:27:33 2019

@author: Huy Nguyen
"""
"""
Variation of Dutch National Flag problem
You have an unsorted array of integers and a function
string getCategory(integer), which deterministically returns 1 of three possible strings: "low", "medium", or "high", 
depending on the input integer. You need to output an array with all the "low" numbers at the bottom, all the "medium" numbers
 in the middle, and all the "high" numbers at the top. This is basically a partial sort. Within each category, the order of the numbers does not matter.

For example, you might be give the array [5,7,2,9,1,14,12,10,5,3].
For input integers 1 - 3, getCategory(integer) returns "low", for 4 - 10 it returns "medium," and for 11 - 15 it returns "high".

You could output an array (or modify the given array) that looks like this: [3,1,2,5,5,9,7,10,14,12]"""
def rearrangeExtraSpace(arr,low,medium,high):
    l,m,h = [],[],[]
    for item in arr:
        if item<=low:
            l.append(item)
        elif item<=medium:
            m.append(item)
        else:
            h.append(item)
    return l+m+h
arr = [5,7,2,9,1,14,12,10,5,3]
low,medium,high = 3,10,15
#print (rearrangeExtraSpace(arr,low,medium,high))
def rearrangePointers(arr,low,medium,high):
    l,m,h = 0,0,len(arr)-1
    while m <h:
        item = arr[m]
        print (l,m,h)
        if item<=low:
            arr[l],arr[m] = arr[m],arr[l]
            l += 1
            m += 1
        elif item<=medium:
            m += 1
        else:
            arr[m],arr[h] = arr[h],arr[m]
            h -=1
        
rearrangePointers(arr,low,medium,high)