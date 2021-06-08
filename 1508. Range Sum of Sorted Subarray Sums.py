# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:15:49 2021

@author: brian.hu
"""

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix_sum = [0]
        for i in range(n := len(nums)) :
            prefix_sum.append(prefix_sum[-1] + nums[i])
        arr = list()
        for i in range(1,n + 1) :
            for j in range(i - 1,-1,-1) :
                arr.append(prefix_sum[i] - prefix_sum[j])
        arr.sort()
        return sum(arr[left - 1 : right]) % 1000000007