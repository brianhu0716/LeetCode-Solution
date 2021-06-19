# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 09:25:41 2021

@author: Brian
"""
"""
for i < j
type1 : 
    odd : arr[i] > arr[i + 1]
    even : arr[i] < arr[i + 1]
type2:
    odd : arr[i] < arr[i + 1]
    even : arr[i] > arr[i + 1]
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [1 for _ in arr]
        max_len = 1
        for i in range(0,len(arr) - 1): # check type1 : 
            if (i % 2 == 1 and arr[i] > arr[i + 1]) or (i % 2 == 0 and arr[i] < arr[i + 1]):
                dp[i + 1] = dp[i] + 1
                max_len = max(max_len, dp[i + 1])    
        dp = [1 for _ in arr]
        for i in range(0,len(arr) - 1): # check type2
            if (i % 2 == 0 and arr[i] > arr[i + 1]) or (i % 2 == 1 and arr[i] < arr[i + 1]):
                dp[i + 1] = dp[i] + 1
                max_len = max(max_len, dp[i + 1])
        return max_len