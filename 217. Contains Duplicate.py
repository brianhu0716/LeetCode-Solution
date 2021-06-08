# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:55:32 2021

@author: Brian
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            if freq[num] == 2: return True
        return False