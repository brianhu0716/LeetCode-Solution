# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:55:00 2021

@author: Brian Hu
"""
from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # deque is guaranteed to be monotonic decreasing stack and all element in it is in the range [i - k, i], where i is the current index
        q = deque([(nums[0],0)]) 
        
        for i in range(1,len(nums)):
            dp[i] = nums[i] + q[0][0]
            
            while q and q[-1][0] < dp[i]: # remove element with value less than current value
                q.pop()
                
            q.append((dp[i],i))
            
            if i - k == q[0][1]: # ensure the max value in deque is in the bounds
                q.popleft()
        
        return dp[-1]
        '''
        n = len(nums)
        dp = [0 if i != 0 else nums[0] for i in range(n)]
        for i in range(1, n):
            r = float('-inf')
            for j in range(max(0, i - k), i):
                r = max(r, dp[j])
            dp[i] = nums[i] + r

        return dp[-1]
        '''