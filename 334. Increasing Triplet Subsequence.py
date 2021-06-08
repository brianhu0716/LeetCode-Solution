# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:01:16 2021

@author: brian.hu
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float("inf")
        min2 = float("inf")
        for i in range(len(nums)):
            if nums[i] > min1:
                min2 = min(min2,nums[i])
            if nums[i] > min2:
                return True
            min1 = min(min1,nums[i])
        return False
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3 : return False
        
        dp = [1 for _ in nums]
        for i in range(len(nums)) :
            for j in range(i) :
                if nums[i] > nums[j] :
                    dp[i] = max(dp[i], 1 + dp[j])
                    if dp[i] == 3 : return True
        
        return False
'''