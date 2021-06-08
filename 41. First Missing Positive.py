# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:22:44 2021

@author: Brian
"""


import numpy as np
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = np.sort(np.array(nums)) #小到大
        index = np.where(nums > 0)[0]
        if index.size == 0: # nums中沒有正數,直接回傳1
            return 1
        elif index.size == 1: # nums中只有一個正數
            if nums[index[0]] == 1: # [1]
                return 2
            else: #[2]
                return 1
        else: #nums中超過2個正數
            if nums[index[0]] != 1: # [3,9]
                return 1
            else: 
                flag = True
                for i in range(len(index) - 1):
                    if nums[index[i + 1]] - nums[index[i]] > 1:
                        flag = False
                        break
                if flag == False: # [1,2,4]
                    return nums[index[i]] + 1
                else: # [1,2,3,4,5]
                    return nums[index[-1]] + 1
        ''' 簡化版
        nums = np.array(nums) #小到大
        nums = np.sort(nums[np.where(nums > 0)[0]]) # nums變為原先nums中所有的正數且由小到大排序
        if nums.size == 0 or nums[0] != 1: # nums中沒有正數或第一個正數不是0,直接回傳1
            return 1
        else: # [1],或nums中多於兩個正數且第一個數字都是1的情況
                flag = True
                for i in range(len(nums) - 1):
                    if nums[i + 1] - nums[i] > 1:
                        flag = False
                        break
                if flag == False: # [1,2,4]
                    return nums[i] + 1
                else: # [1,2,3,4,5][1]
                    return nums[-1] + 1
        '''