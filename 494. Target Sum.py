# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:42:15 2021

@author: Brian
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def helper(idx,nums,S,total):
            if (idx,total) in self.memo.keys() : return self.memo[(idx,total)]
            if idx == len(nums): return 1 if total == S else 0
        
            self.memo[(idx,total)] = helper(idx + 1,nums,S,total = total - nums[idx]) \
                                       + helper(idx + 1,nums,S,total = total + nums[idx])
            
            return self.memo[(idx,total)]

        self.memo = dict()
        
        helper(0,nums,S,0)

        return self.memo[(0,0)]