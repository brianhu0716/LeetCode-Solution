# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:20:17 2021

@author: Brian Hu
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int: 
        '''
        l = sorted([[x, i] for i, x in enumerate(nums)])
        ans = 0
        idx_min = float('inf')
        for x, i in l:
            idx_min = min(idx_min, i)
            ans = max(ans, i - idx_min)
        return ans
        '''
    def maxWidthRamp(self, nums: List[int]) -> int: # binary search + stack
        def binarySearch(stack, v):
            left, right = 0, len(stack)
            while left <= right:
                mid = (left + right) // 2
                if stack[mid][0] > v:
                    left = mid + 1
                else:
                    right = mid - 1
            return stack[left][1]
            
        ans = 0
        stack = list()
        for i, v in enumerate(nums):
            if not stack or stack[-1][0] > v: # maintain monotonic decreasing stack
                stack.append([v,i])
                continue
             # if not momotonic decreasing, use binary search to find the farest 
             # index with value less than v, so that we can get the max ramp 
            ans = max(ans, i - binarySearch(stack, v))
        return ans