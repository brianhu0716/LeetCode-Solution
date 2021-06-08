# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:17:17 2021

@author: Brian
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:nums.pop(i)
            else: i += 1
        return len(nums)