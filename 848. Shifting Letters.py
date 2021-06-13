# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:07:51 2021

@author: Brian Hu
"""
import string 
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        d1 = {string.ascii_lowercase[i] : i for i in range(26)}
        d2 = {i : string.ascii_lowercase[i] for i in range(26)}
        n = len(s)
        times = [0 for _ in range(n + 1)]
        for i in range(n - 1,-1,-1): # using prefix sum to calculate the total times s[i] needs to be shifted
            times[i] += times[i + 1] + shifts[i]
        for i in range(n - 1,-1,-1):
            new_position= (d1[s[i]] +times[i]) % 26 # 26 letters is one cycle
            s = s[:i] + d2[new_position] + s[i + 1:] # get the new letter after shifting
        return s