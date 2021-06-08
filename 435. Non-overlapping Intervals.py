# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:16:51 2021

@author: brian.hu
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        pend = intervals[0][1]
        remove = 0
        for i in range(1,len(intervals)):
            if pend <= intervals[i][0]:
                pend = intervals[i][1]
            else:
                # intervals[i][1]比較小，要remove上一個interval,
                # 如果pending比較小，要remove當前的interval
                pend = min(pend,intervals[i][1])
                remove += 1
        return remove