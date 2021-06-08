# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 01:04:54 2021

@author: Brian
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
            if d[num] == 2:
                return num