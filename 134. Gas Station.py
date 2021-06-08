# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:37:21 2021

@author: Brian
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) : return -1 
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        
        start = 0
        gas_so_far = 0
        
        for i in range(len(diff)):
            gas_so_far += diff[i]
            
            if diff[i] > gas_so_far:
                start = i
                gas_so_far = diff[i]
                
        return start