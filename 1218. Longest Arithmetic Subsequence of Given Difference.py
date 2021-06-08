# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:33:28 2021

@author: Brian
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = dict()
        
        for i in range(0,len(arr)):
            if arr[i] - difference in dp.keys():
                dp[arr[i]] = dp.get(arr[i] - difference,0) + 1
            else:
                dp[arr[i]] = 1
                
        return max(dp.values())