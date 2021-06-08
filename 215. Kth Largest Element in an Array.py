# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:14:39 2021

@author: Brian
"""

nums = [3,2,3,1,2,4,5,5,6]
k = 4
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]