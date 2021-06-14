# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:26:46 2021

@author: Brian Hu
"""
import collections
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        keys = sorted(d.keys())[::-1]
        ans = 0
        for i in range(len(keys) - 1): # the minima number doesn't need to change it value
            ans += d[keys[i]] # how many times to make greater value to next greater
            d[keys[i + 1]] += d[keys[i]]  # update # of next greater values
        return ans