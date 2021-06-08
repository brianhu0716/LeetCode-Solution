# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:22:17 2021

@author: Brian
"""

class Solution:
    def frontsequence(self): # judge front sequence from first element to max element
        for i in range(len(self.front)-1):
            res = self.front[i+1] - self.front[i]
            if res <= 0:
                self.flag = 0
                break
    def backsequence(self): # judge back sequence from max element to last element
        for i in range(len(self.back)-1):
            res = self.back[i+1] - self.back[i] 
            if res >= 0:
                self.flag = 0 
                break
    def validMountainArray(self, arr: List[int]) -> bool:
        self.arr = arr # define array
        self.ipeak = self.arr.index(max(self.arr)) # index of maxima element
        self.peak = max(self.arr) # value of maxima element
        self.flag = 1 
        self.front = self.arr[:self.ipeak] # generate front sequence
        self.back = self.arr[self.ipeak:] # generate back sequence
        '''
        when max value appears in the array(excludes first or last position)
        we need to examine both front and back sequence. if the maxima value 
        appears at first or last position, return False
        '''
        if self.ipeak != 0 and self.ipeak != len(self.arr)-1: 
            self.frontsequence()
            if self.flag == 0:
                return False
            self.backsequence()
            if self.flag == 0:
                return False
            if self.flag == 1:
                return True
        else: 
            return False

