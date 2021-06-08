# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 22:29:15 2021

@author: Brian
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dp = [[nums[0]]]
        for i in range(1,len(nums)):
            res = []
            for combo in dp:
                for j in range(i + 1):
                    res += [combo[:j] + [nums[i]] + combo[j:]]
            dp = res
        return dp