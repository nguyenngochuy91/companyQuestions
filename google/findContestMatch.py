# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:26:02 2019

@author: huyn
"""

#544. Output Contest Matches
#During the NBA playoffs, we always arrange the rather strong team to play with the 
#rather weak team, like make the rank 1 team play with the rank nth team, which is a good
# strategy to make the contest more interesting. Now, you're given n teams, you need to output their final 
# contest matches in the form of a string.
#
#The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. 
#(Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') 
#to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. 
#During the pairing process in each round, 
#you always need to follow the strategy of making the rather strong one pair with the rather weak one.
class Solution(object):
    def findContestMatch(self, n):
        team = map(str, range(1, n+1))

        while n > 1:
            for i in xrange(n / 2):
                team[i] = "({},{})".format(team[i], team.pop())
            n /= 2

        return team[0]