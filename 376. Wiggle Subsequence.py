# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:18:13 2021

@author: Brian
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 移除重複的數字
        for i in range(1,len(nums) + 1):
            if i == len(nums):
                break
            if nums[i] != nums[i - 1] : 
                break
        nums = nums[i - 1 : ]
        
        dp = [[] for _ in nums]
        dp[0] = [nums[0]]
        for i in range(1,len(nums)):
            for j in range(i): # 由小往大更新
                # 初始化第二個數字的dp，確保新加入的數字可以形成 + - + 或 - + -的格式，且長度最長
                if len(dp[j]) == 1 or (nums[i] - nums[j]) * (dp[j][-1] - dp[j][-2]) < 0 and 1 + len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
    
        return max([len(combo) for combo in dp])