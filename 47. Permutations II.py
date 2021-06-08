# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:14:46 2021

@author: Brian
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = [[nums[0]]]
        for i in range(1,len(nums)):
            res = []
            for combo in dp:
                for insert_idx in range(0,i + 1):
                    res += [combo[:insert_idx] + [nums[i]] + combo[insert_idx:]]
            dp = res
        
        dp = sorted(dp)

        i = 0
        while i < len(dp):
            if i == len(dp) - 1:
                break
            
            if dp[i] == dp[i + 1]:
                dp.pop(i + 1)
            else:
                i += 1
        
        return dp