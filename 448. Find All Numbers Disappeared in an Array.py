# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:14:06 2021

@author: Brian
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        ans = list()
        for i in range(1,n + 1):
            if i not in nums: ans.append(i)
        return ans