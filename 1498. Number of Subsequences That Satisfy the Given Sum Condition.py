# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:22:42 2021

@author: Brian
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        lp, rp = 0, n - 1
        ans = 0
        while lp <= rp:
            if nums[lp] + nums[rp] <= target:
                ans += 2 ** (rp - lp)
                lp += 1
            else:
                rp -= 1
        return ans % 1000000007 if ans >= 1000000007 else ans