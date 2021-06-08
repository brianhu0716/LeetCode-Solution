# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:01:14 2021

@author: Brian
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ref = set(nums)
        for n in range(len(nums) + 1):
            if n not in ref:
                return n
            
        '''
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        if nums[-1] != (l := len(nums)):
            return l
        for i in range(l - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1
        '''