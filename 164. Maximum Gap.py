# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:48:16 2021

@author: brian.hu
"""
# 找出sorted array中兩相鄰數字差最大的值
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_gap = 0
        for i in range(0,len(nums) - 1) :
            max_gap = max(nums[i + 1] - nums[i],max_gap)
        return max_gap