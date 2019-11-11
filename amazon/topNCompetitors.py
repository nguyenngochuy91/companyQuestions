# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:24:39 2019

@author: huyn
"""
"""
Top N Competitors
Amazon Echo has lots of competitors
Web crawler got list of reviews
Given list of reviews, list of competitors, N, return most frequently mentioned top N competitors in the reviews."""
import heapq
def topNCompetitors(numCompetitors,topNCompetitors,competitors,numReview,reviews):
    d = {}
    for competitor in competitors:
        d[competitor] = 0
    for review in reviews:
        for word in review.split():
            word = word.lower()
            for char in """"()~!@#$%^&*_-+=[]{}\|;"':,<.>?/""":
                word = word.replace(char,"")
            if word in d:
                d[word] += 1
    queue = []
    for competitor in d:
        heapq.heappush(queue,(-d[competitor],competitor))
    res = []
    for i in range(topNCompetitors):
        res.append(heapq.heappop(queue)[1])
    return res