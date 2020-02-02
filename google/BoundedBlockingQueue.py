# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:21:35 2020

@author: huyn
"""
#1188. Design Bounded Blocking Queue
import threading
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
 
        self.queue = collections.deque()
        self.cur = 0
        self.ept, self.ful = threading.Semaphore(0), threading.Semaphore(capacity)
    def enqueue(self, element):
 
        self.ful.acquire()
        self.queue.appendleft(element)
        self.cur+=1
        self.ept.release()

    def dequeue(self):
 
        self.ept.acquire()
        temp = self.queue.pop()
        self.cur-=1
        self.ful.release()
        return temp
        
    def size(self):
    
        return self.cur