# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:54:19 2019

@author: Huy Nguyen
"""

#621. Task Scheduler
#
#Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different 
#letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.
#
#However, there is a non-negative cooling interval n that means between two same tasks, there must be at least 
#n intervals that CPU are doing different tasks or just be idle.
#
#You need to return the least number of intervals the CPU will take to finish all the given tasks.