# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 00:09:10 2021

@author: Brian
"""

points = [[3,3],[5,-1],[-2,4]]
k = 2
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist,ans = [],[]
        dist = [p[0] ** 2 + p[1] ** 2 for p in points]
        index = sorted((v,i) for i,v in enumerate(dist))
        ans = [points[index[i][1]] for i in range(k)]
        return ans