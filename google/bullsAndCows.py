# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:20:11 2019

@author: huyn
"""
#Bulls and Cows
#You are playing the following Bulls and Cows game with your friend: You write 
#down a number and ask your friend to guess what the number is. Each time your friend makes 
#a guess, you provide a hint that indicates how many digits in said guess match your secret number 
#exactly in both digit and position (called "bulls") and how many digits match the secret number but 
#locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to 
#eventually derive the secret number.
#
#Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
#
#Please note that both secret number and friend's guess may contain duplicate digits.
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        C = 0
        B = 0
        # use dictionary to store count of digits for secret and guess
        dS = Counter(secret)
        dG = Counter(guess)
        for i in range(len(secret)):
            secretL = secret[i]
            guessL  = guess[i]
            if secretL == guessL:
                B+=1
                dS[secretL] -= 1
                dG[secretL] -= 1
        for letter in dG:
            if letter in dS:                
                C += min(dG[letter],dS[letter])
        return "{}A{}B".format(B,C)