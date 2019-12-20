# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:40:22 2019

@author: Huy Nguyen
"""

#log
class Log:
    def __init__(self):
        self.arr = []
        self.highesIndexDone = None
    def start(self,id,startTime):
        self.arr.append([id,startTime,None])
    def stop(self,id,stopTime):
        self.arr[id][2] = stopTime
        res = []
#        print (self.arr)
        if self.highesIndexDone == None:
            if self.arr[0][0] == id:
                res.append(id)
                self.highesIndexDone = 0
                # we traverse toward the right until we hit something is not done
                for i in range(1,len(self.arr)):
                    nextId,nextStart,nextStop = self.arr[i]
                    if nextStop != None:
                        res.append(nextId)
                        self.highesIndexDone = i
                    else:
                        # we are done
                        break
            return res
        else:
            # we know our index at isDone is the highest possible
            # we check if this index +1 is equal to our id index
            index = self.binarySearch(self.highesIndexDone,id)
            if self.highesIndexDone+1 == index:
                res = [id]
                # we scan up to the first one that does not have endTime
                for i in range(index+1,len(self.arr)):
                    nextId,nextStart,nextStop = self.arr[i]
                    if nextStop!=None:
                        res.append(nextId)
                        self.highesIndexDone = nextId
                    else:
                        break
                
            return res
            
    def binarySearch(self,start,id):
        stop = len(self.arr)-1
        while start+1<stop:
            mid = (start+stop) //2
            if self.arr[mid][0] == id:
                return mid
            elif self.arr[mid][0] > id:
                stop = mid
            else:
                start = mid
        if self.arr[start][0] == id:
            return 0
        if self.arr[stop][0] == id:
            return stop

#log = Log()
#for i in range(11):
#    log.start(i,3+i)
##print (log.arr)
#print (5,log.stop(5,100))
#print(4,log.stop(4,101))
#print(3,log.stop(3,102))
#print(2,log.stop(2,103))
##print(0,log.stop(0,1000))
#print(1,log.stop(1,104))
#print(0,log.stop(0,1000))
#print(7,log.stop(7,200))
#print(9,log.stop(9,201))
#print(6,log.stop(6,202))
#print(10,log.stop(10,210))
#print(8,log.stop(8,201))
#print(0,log.stop(0,1000))
#


