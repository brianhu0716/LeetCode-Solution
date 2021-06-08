# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:31:28 2021

@author: brian.hu
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        def findNext1(start,seats,n) :
            for i in range(start + 1,n) :
                if seats[i] == 1 :
                    return i
            return n
        
        n = len(seats)
        i = seats.index(1)
        max_dist = i # 初始化最大間隔
        while i < n :
            if seats[i] == 1 :
                next_start = findNext1(i,seats,n)
                if next_start == n : return max(max_dist,n - 1 - i) # 超出邊界ex:...1000
                # 更新1與1之間的最大間隔
                max_dist = max(max_dist,int((next_start - i) // 2))
                i = next_start
            else :
                i += 1
        return max_dist