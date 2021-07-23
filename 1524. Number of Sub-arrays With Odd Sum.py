# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:20:35 2021

@author: Brian Hu
"""

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp, ans = [0], 0
        for num in arr:
            dp.append(dp[-1] + num)
        accu_even, accu_odd = 1, 0
        for i in range(1, len(dp)):
            if dp[i] % 2 == 0: # if prefix sum is even, we can only get odd result by subtract it with odd number 
                ans += accu_odd
                accu_even += 1 # current prefix sum
            else:
                ans += accu_even # if prefix sum is odd, we can only get odd result by subtract it with even number 
                accu_odd += 1   # current prefix sum          
        return ans % (10 ** 9 + 7)