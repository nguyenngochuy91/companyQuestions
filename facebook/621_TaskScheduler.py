# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:28:53 2019

@author: huyn
"""

#621. Task Scheduler

#Given a char array representing tasks CPU need to do. It contains capital letters 
#A to Z where different letters represent different tasks. Tasks could be done without 
#original order. Each task could be done in one interval. For each interval, CPU could 
#finish one task or just be idle.
#
#However, there is a non-negative cooling interval n that means between two same tasks, 
#there must be at least n intervals that CPU are doing different tasks or just be idle.
#
#You need to return the least number of intervals the CPU will take to finish all the given tasks.
import heapq
from typing import List
def leastInterval(tasks: List[str], n: int) -> int:
    d = {}
    for task in tasks:
        if task not in d:
            d[task]=0
        d[task]+=1
    priorityQueue= []
    time = 0
    for task in d:
        heapq.heappush(priorityQueue,-d[task])
    print (priorityQueue)
    while priorityQueue:
        jobs = []
        for i in range(n+1):
            if priorityQueue:
                jobs.append(heapq.heappop(priorityQueue))
        print (jobs)
        for job in jobs:
            job=job+1
            if job!=0:
                heapq.heappush(priorityQueue,job)  
        if not priorityQueue:
            time+=len(jobs)
        else:
            time+=n+1
    return time
#tasks = ["A","A","A","B","B","B"]
#n = 2
#print (leastInterval(tasks,n))