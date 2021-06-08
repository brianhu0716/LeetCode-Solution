# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:40:33 2021

@author: Brian
"""
'''
動態規劃：第idx間房子能夠獲得的最大值必須是前idx - 1間累積的最大值或是前idx - 2間累積的最大值加上自己的價值
邊界條件：若idx小於0(沒有房子可以偷)，回傳0
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.d = dict()
        def findRoute(idx,nums):
            if idx in self.d.keys():return self.d[idx]
            if idx < 0:return 0
            
            res = max(nums[idx] + findRoute(idx - 2,nums),findRoute(idx - 1,nums)) 
            self.d[idx] = res
            return res
        return findRoute(len(nums) - 1,nums) 
    
    
    """ recursion + memoization
        def helper(position,nums):
            if position in self.memo.keys() : return self.memo[position]
            if position == 0: return nums[0]
            if position == 1 : return max(nums[0],nums[1])

            self.memo[position] = max(nums[position] + helper(position -2,nums),helper(position - 1,nums))

            return self.memo[position]
        
        if (l := len(nums)) <= 2: return max(nums)
        self.memo = dict()
        return max(nums[l - 1] + helper(l - 3,nums),helper(l - 2,nums))
    """

    """ tabulation
        if (l := len(nums)) <= 2: return max(nums)
        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,l):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]
    """   