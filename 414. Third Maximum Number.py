# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:52:53 2021

@author: Brian
"""
'''
set是可以被排序的,語法:sorted(set(list...))
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        c,maxN = 0,max(nums)
        while nums and c < 2:
            c += 1
            nums = [nums[i] for i in range(len(nums)) if nums[i] != max(nums)]
        return maxN if not nums else max(nums)
    '''
        return max(N) if len(N := sorted(set(nums))) < 3 else N[-3]
    '''
