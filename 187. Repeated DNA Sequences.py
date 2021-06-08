# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:11:27 2021

@author: Brian
"""
class Solution:
    def findRepeatedDnaSequences(self, s):
        DNA = {}
        repeatSeq =[] 

        for i in range(len(s) - 9):
            key = s[i:i+10]
            if key not in DNA.keys():
                DNA[key] = 1
            else:
                DNA[key] += 1

        repeatSeq += [key for key in DNA.keys() if DNA[key] > 1]
        return repeatSeq

