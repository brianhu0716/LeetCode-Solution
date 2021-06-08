# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:27:09 2021

@author: Brian
"""
'''
回傳出現次次數超過總長度的三分之一的數字，利用字典累積個數字出現的次數，只要該數字次數超過限制值，把它加入一個set中，之後只要看到
當前數字在set中，即可略過，否則繼續累加數字出現次數，直到所有數字遍歷完為止
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        over_bound,d = set(),dict()
        for num in nums:
            if num in over_bound:
                continue
            d[num] = d.get(num,0) + 1
            if d[num] > n // 3:
                over_bound.add(num)
        return list(over_bound)