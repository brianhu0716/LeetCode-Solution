# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 23:21:47 2021

@author: Brian
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1 :return False
        target,ln = int(sum(nums) / 2),len(nums)
        dp = [[False if i != 0 else (nums[0] == j) for j in range(target + 1)] for i in range(ln)]
        
        for i in range(1,ln):
            for prefix_sum in range(target + 1):
                if prefix_sum <= nums[i]:
                    dp[i][prefix_sum] = dp[i - 1][prefix_sum]
                else:# 一定要看dp[i - 1]，因為nums[i]只能用一次
                    dp[i][prefix_sum] = dp[i - 1][prefix_sum] or dp[i - 1][prefix_sum - nums[i]] 
        print(dp)
        return dp[-1][-1]

'''
Case [4,4,3,1]
Dp[i][prefix_sum – nums[i]]:
4[[False, False, False, False, True, False, False], 
4[False, False, False, False, True, False, False], 
3[False, False, False, False, True, False, False], 
1[False, False, False, False, True, True, True]]
Dp[i - 1][prefix_sum – nums[i]]:
4[[False, False, False, False, True, False, False], 
4[False, False, False, False, True, False, False], 
3[False, False, False, False, True, False, False], 
1[False, False, False, False, True, True, False]]
'''