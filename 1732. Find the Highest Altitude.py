# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:19:25 2021

@author: Brian
"""
'''
兩個變數：一個紀錄到目前為止的最大高度，另一個紀錄當前的高度，當當前高度大於到目前為止最大高度時，更新到目前為止最大高度

'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height_now = 0
        height_max = 0
        for i in range(0,len(gain)):
            height_now += gain[i]
            height_max = max(height_now,height_max)
        return height_max