# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 23:44:25 2019

@author: Huy Nguyen
"""
import random
def solve(arr):
    res = ["1"]
    d= []
    for i in range(10**5):
        if i <arr[0]:
            d.append(1)
        else:
            d.append(0)
    print (d[:10])
    current = 1
    start = 0
    for num in arr[1:]:
        indexNum = num-1
        if num<current:
            res.append(str(current))
            continue
        else:
            d[indexNum]+=1
            # we do binary search here to find the highest index
            # that our current still change
            stop = indexNum
            print (num,start,stop)
            while start+1<stop:
                mid = (start+stop)//2
#                print (start,stop,mid)
                # we know for sure any number below the indexNum can increase the value
                d[mid]+= 1
                # if our current is less than the new updated value, set start to this index
                if current < min(d[mid],mid+1):
                    start = mid
                    # set our current this this
                
                elif current > min(d[mid],mid+1):
                    stop = mid
                else:
                    start +=1
            # escape loop when start +1 == stop
#            print (42,start,stop)
            if min(d[stop],stop+1) >=current:
                current = min(d[stop],stop+1) 
                start = stop
            elif min(d[start],start+1) >=current:
                current = min(d[start],start+1)  
            print (49,start,stop)
        res.append(str(current))
        print (d[:10])
    return " ".join(res)

def solveNaive(arr):
    res= []
    d= [0]*10**5
    current = 0
    res = []
    for num in arr:
        for i in range(num):
            d[i]+=1
            current = max(current,min(d[i],i+1))
        res.append(str(current))
    return " ".join(res)

#t = int(input().strip())
#for i in range(t):
#    n = int(input().strip())
#    arr = [int(item) for item in input().strip().split()]
#    res = solveNaive(arr)
#    print ("Case #{}: {}".format(i+1,res))
arr =[2, 6]
#for i in range(100):
#    arr.append(random.randint(1,10))
res1 = solve(arr)
#res2 = solveNaive(arr)
#print (res1 == res2)
print (res1)
#print (res2)
print (arr)