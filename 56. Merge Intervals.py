# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:56:16 2021

@author: Brian
"""

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[0,0],[0,0]]
intervals = [[10,11],[2,6],[8,10],[15,18]]
i,intervals = 0,sorted(intervals) # 確保intervals中所有的start都是由小到大排序的(防止[[10,11],[2,6],[8,10],[15,18]])
while i < len(intervals) - 1:
    # n1,n2 = intervals[i],intervals[]
    if intervals[i][1] >= intervals[i + 1][0] :
        if intervals[i][1] <= intervals[i + 1][1]:
            intervals[i][1] = intervals[i + 1][1]
        intervals.pop(i + 1) # 大於的話直接刪除i + 1(intervlas[i + 1]被intervals[i]完全覆蓋)
    else:
        i += 1

print(intervals)
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Pretty straightforward solution - we first sort the array based on the indices of starting indices. If the start
        #times were already sorted, the solution would run in linear time. From observation, it overlaps if and only if
        #there exists a start between a previous start and end time. We make use of a start and end sliding pointer to 
        #keep track of this and accordingly append our array based on this property.
        
        #Time: O(n log n), where n is the number of intervals. 
        #Space: O(n) where n is the number of intervals
        
        starts, ends = zip(*intervals)
        indices = [i[0] for i in sorted(enumerate(starts), key=lambda x:x[1])] #sort the intervals by start indices
        
        start, end = starts[indices[0]], ends[indices[0]] #cache first interval
        
        result = []
        
        for i in range(1, len(starts)):
            if end >= starts[indices[i]]:
                #just because an end time is greater than the current start time doesn't mean that it's also greater than the current
                #end time. We have to check for this. An example of this is [ [1, 4], [2, 3] ]. Without the below condition, the 
                #output would've been [1, 3]. But the answer should be [1, 4]. Using this, we can elongate the end time and essentially
                #recompare on the next timestep.
                if end >= ends[indices[i]]:
                    continue
                end = ends[indices[i]]
            else:
                result.append([start, end])
                start, end = starts[indices[i]], ends[indices[i]]
            
        return result + [[start, end]]

    