# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:46:44 2021

@author: Brian Hu
"""
'''
prefix[i] is the accumulation sum from index0 to i, 
then we using dp to calculate the accumulation sum from index j to index i with j in range(0, i - 1) by using prefix[i] - prefix[j] then check whether the difference can be mod by k
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [nums[0]]
        for i in range(1, n := len(nums)):
            if nums[i] == nums[i - 1] == 0 :
                return True
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] % k == 0:
                return True
        if prefix[-1] < k:
            return False
        
        for i in range(1, n):
            for j in range(i - 1):
                if (prefix[i] - prefix[j]) % k == 0:
                    return True
        return False