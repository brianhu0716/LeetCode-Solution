# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:38:22 2021

@author: Brian
"""
'''
關鍵-->non-overlapping :interval[i][1] < intervals[i + 1][0]
(a)首先找出起始點欲插入的起始點位置，已新區間的起始點(newIntervals[0])為判斷基準：
(a.1)如果該點位於某個區間中(含邊界)，則我們跳出程式接著找插入終點
(a.2)如果該點位大於於某個區間上界但又不到下一個區間的下界，則我們接著判斷
 
'''
class Solution:
    def insert(intervals, newInterval):
        if not intervals: # intervals = []
            return [newInterval]
        if newInterval[0] < intervals[0][0]:
            if newInterval[1] > intervals[0][0]:
                intervals[0][0] = newInterval[0]
                start = 0
            elif newInterval[1] == intervals[0][0]:
                intervals[0][0] = newInterval[0]
                return intervals
            else:
                return (intervals := [newInterval] +intervals) 
        if newInterval[0] >= intervals[-1][1]:
            if newInterval[0] == intervals[-1][1]:
                intervals[-1][1] = newInterval[1]
                return intervals
            else:
                return (intervals := intervals + [newInterval])
        for start in range(l := len(intervals)): # 找出欲合併的起始區間位置
            if newInterval[0] >= intervals[start][0] and newInterval[0] <= intervals[start][1]:
                break
            elif newInterval[0] > intervals[start][1] and newInterval[0] <= intervals[start + 1][0]:
                if newInterval[1] > intervals[start][1] and newInterval[1] < intervals[start + 1][0]:
                    return (intervals := intervals[:start + 1] + [newInterval] + intervals[start + 1:])
                else:
                    start += 1
                    intervals[start][0] = newInterval[0]
                    break
        # print(intervals)
        if newInterval[1] > intervals[-1][1]:
            intervals[start][1] = newInterval[1]
            del intervals[start + 1:]
            return intervals
        else:
            for i in range(start,l):
                if newInterval[1] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                    if i == start:
                        return intervals
                    else:
                        intervals[start][1] = intervals[i][1]
                        del intervals[start + 1:i + 1]
                        return intervals
                elif newInterval[1] < intervals[i + 1][0] and newInterval[1] > intervals[i][1]:
                    intervals[start][1] = newInterval[1]
                    del intervals[start + 1:i + 1]
                    return intervals
test = Solution
intervals = [[[1,3],[6,9]],
              [[1,2],[3,5],[6,7],[8,10],[12,16]],
              [[1,5]],
              [[1,5]],
              [],
              [[2,4],[6,8],[12,15]],
              [[1,5]],
              [[1,5]],
              [[2,5],[6,7],[8,9]],
              [[1,5],[6,8]]]
newInterval = [[2,5],
                [4,8],
                [2,3],
                [2,7],
                [5,7],
                [11,18],
                [0,0],
                [0,1],
                [0,1],
                [0,9]]
# intervals = [[[1,2],[3,5],[6,7],[8,10],[12,16]]]
# newInterval = [[4,8]]
for i in range(len(intervals)):
    # print(intervals[i])
    # print(newInterval[i])
    print(test.insert(intervals[i], newInterval[i]))

