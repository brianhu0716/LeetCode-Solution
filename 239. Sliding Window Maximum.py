# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:05:38 2021

@author: Brian Hu
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        dq = deque([(float('-inf'), -1)])
        for i in range(k):
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append((nums[i], i))
        ans = [dq[0][0]] 
        
        for i in range(k, len(nums)):
            # remove the value less than current nums[i]
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append((nums[i], i))
            
            # remove the value out of bounds
            while dq and dq[0][1] <= i - k:
                dq.popleft()

            ans.append(dq[0][0])
        return ans