# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:14:07 2021

@author: Brian Hu
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        take = list() # how much time each monster needs to take to reach the  city
        for i in range(n := len(dist)):
            take.append(dist[i] / speed[i])
        take.sort()
        for i in range(n):
            if i >= take[i]: # monster[i] has already reached the city first, you lose
                return i
        return n # you can eliminate all monster and keep the city from attacking 