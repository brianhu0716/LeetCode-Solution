# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:24:01 2021

@author: Brian Hu
"""
# just find median of the sequence to make the least increments to create a array with all elements are equal
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if (n := len(nums)) % 2 == 0:
            mid = int((nums[n // 2] + nums[n // 2 - 1]) / 2)
        else:
            mid = nums[n // 2]
        for num in nums:
            ans += abs(num - mid)
        return ans