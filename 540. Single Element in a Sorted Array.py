# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:12:04 2021

@author: brian.hu
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(1,len(nums),2) :
            if nums[i] != nums[i - 1] :
                return nums[i - 1] # 找到只出現一次的值
        return nums[-1] # 只出現一次的值在數列尾端