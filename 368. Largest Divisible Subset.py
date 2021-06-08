# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:15:10 2021

@author: Brian
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[[num]] for num in nums]
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    if 1 + len(dp[j][-1]) >= len(dp[i][-1]):
                        dp[i][-1] = dp[j][-1] + [nums[i]]

                    
        table = [len(combo[-1]) for combo in dp]
       # print(table)
        idx_max = table.index(max(table))
        
        return dp[idx_max][-1]