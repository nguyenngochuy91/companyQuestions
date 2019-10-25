# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:16:11 2019

@author: huyn
"""

#Logger Rate Limiter
#Design a logger system that receive stream of messages along with its timestamps, 
#each message should be printed if and only if it is not printed in the last 10 seconds.
#
#Given a message and a timestamp (in seconds granularity), return true if the message 
#should be printed in the given timestamp, otherwise returns false.
#
#It is possible that several messages arrive roughly at the same time.
#import heapq
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.d:
            self.d[message] = timestamp
            return True
        else:
            if timestamp - self.d[message]>=10:
                self.d[message] = timestamp
                return True
        return False