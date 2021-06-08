# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:35:15 2021

@author: Brian
"""
"""
本題要求找出一個array中任選三個數始其乘積為最大，並回傳該最大值
(a) 先對array做排序
(b) 由於可能有負數，我們必須要考慮最小的兩個數(可能是負數)相乘再乘上最大的正數(nums[0] * nums[1] * nums[-1])
    是否有比最大的三個數相乘(nums[-1] * nums[-2] * nums[-3])來的大
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if  nums[0] * nums[1] * nums[-1] > nums[-1] * nums[-2] * nums[-3]:
            return nums[0] * nums[1] * nums[-1]
        else:
            return nums[-1] * nums[-2] * nums[-3]