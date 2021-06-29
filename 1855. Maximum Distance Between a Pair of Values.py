# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:37:42 2021

@author: Brian Hu
"""

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0 # index of nums1 and index of nums2
        max_len = 0 # maxima length
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                if p1 <= p2: # update max_len
                   max_len = max(max_len, p2 - p1)
                p2 += 1
            else:
                p1 += 1 
        return max_len