# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 01:06:03 2021

@author: Brian
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,c = 1,0
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                (c := c + 2) if c == 0 else (c := c + 1)
                if c > 2:
                    nums.pop(i)
                else:
                    i += 1
            else:
                c = 0
                i += 1
        return len(nums)