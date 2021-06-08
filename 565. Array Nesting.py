# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:11:31 2021

@author: Brian
"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def helper(idx,nums):
            if self.dp[idx] : return self.dp[idx]
            
            if self.visited[idx] : return 0

            if nums[idx] == idx : return float('-inf')
            
            self.visited[idx] = True
            ans = 1 + helper(nums[idx],nums)
            self.dp[idx] = ans
            
            return ans
        
        self.visited = [False for _ in nums]
        self.dp = [None for _ in nums]
        ans = []
        for start in range(len(nums)):
            if nums[start] == start:
                ans.append(1)
            else:
                ans.append(helper(start,nums))
        return max(ans)