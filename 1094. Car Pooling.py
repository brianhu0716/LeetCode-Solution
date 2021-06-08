#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:21:27 2021

@author: brian
"""
"""
for any stop, we first eliminate the # of passengers that shiuld leave at previous
stop, then we add the passengers who need to get in, if at any time, the 
passengers on bus is greater than the max capacity, return False


"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        passengers = 0
        res = list()
        for num,start,end in trips :
            if res : 
                for i in range(len(res) - 1,-1,-1) :
                    n,destination = res[i][0],res[i][1]
                    if destination <= start :
                        passengers -= n
                        res.pop(i)
                        
            passengers += num
            
            if passengers > capacity : return False
            
            res.append([num,end])
            
        return True
                   