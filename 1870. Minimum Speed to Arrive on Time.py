#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 06:03:50 2021

@author: brian
"""
"""
use binary search : to find out the slowest spped to arrive desitination without
exceed the boundary, we can set min speed= 1 and max speed = 10 ** 9,
each time we calculate the time we need to take to desitination,until the 
lower bound exceed the upper bound. then return the final answer
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:   
        if hour < len(dist) - 1 : return -1
        
        low = 1
        high = 10 ** 9
        ans = -1
        while low <= high :
            speed = (low + high) // 2
            time = sum([math.ceil(d / speed) for d in dist[:-1]]) + dist[-1] / speed
            
            if time > hour :
                low = speed + 1
            else :
                high = speed - 1
                ans = speed
                
        return ans