#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:27:28 2021

@author: brian
"""
"""
if current num meets the limit, total length is add with idx_cur - idx_over,
idx_over is the previous idx with value exceeds upper bound. next, we need to check
from idx_cur to len(nums) to pick out the consecutive number that lower than 
lower bound, and add the length with idx_cur - idx_over.
following the algorithm, we can finally find the answer
"""
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right) -> int:
        idx_over = -1
        ans,n = 0,len(nums)
        idx = 0
        while idx < n :
            if nums[idx] > right :
                idx_over = idx
                idx += 1
            else :
                if (left <= nums[idx] <= right) :
                    ans += idx - idx_over
                    for j in range(idx + 1,n + 1) :
                        if j == n or not left > nums[j] :
                            break
                        ans += idx - idx_over
                    idx = j
                else : 
                    idx += 1
        return ans