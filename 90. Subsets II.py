# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:29:32 2021

@author: Brian
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            if i == 0 :
                ans = [[],[nums[0]]]
                continue
            
            ans = ans[:] + list(map(lambda x : x + [nums[i]], ans))
            
        ans = sorted([sorted(combo) for combo in ans])
        i = 0
        while i < len(ans) - 1:
            if ans[i] == ans[i + 1]:
                ans.pop(i + 1)
            else:
                i += 1
        return ans