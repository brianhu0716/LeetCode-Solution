# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:44:04 2021

@author: Brian Hu
"""

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]*m for _ in range(m+1)]
        
        for i in reversed(range(m)):
            for j in range(i, m): 
                k = i + m - j - 1
                dp[i][j] = max(nums[i] * multipliers[k] + dp[i+1][j], 
                               nums[j-m+n] * multipliers[k] + dp[i][j-1])
        
        return dp[0][-1]