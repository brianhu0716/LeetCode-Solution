# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:00:08 2021

@author: Brian
"""
"""
每個數字可以選擇拿或不拿
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            if i == 0 : 
                ans = [[],[nums[0]]] # 初始化答案，選擇不拿第一個數字([])或拿第一個數字([nums[0])
                continue
            #  不拿當前的數字 + 拿當前的數字
            ans = ans[:] + list(map(lambda x : x + [nums[i]],ans)) 
        
        return ans
