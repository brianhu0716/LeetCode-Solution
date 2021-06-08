# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:26:24 2021

@author: Brian
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        for i in range(1,len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]: return i - 1
        return 0