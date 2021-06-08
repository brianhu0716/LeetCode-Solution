# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:36:19 2021

@author: Brian
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp = [[[num]] for num in nums]
        for i in range(1,len(dp)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] += list(map(lambda x : x + [nums[i]] ,dp[j]))
        ans = []
        for combo in dp:
            if len(combo) > 1:
                ans += combo[1 : ]
        i = 0
        ans.sort()
        while i < len(ans) - 1:
            if ans[i] == ans[i + 1]:
                ans.pop(i + 1)
            else: 
                i += 1
        return ans