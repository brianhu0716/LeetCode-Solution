# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:52:18 2021

@author: brian.hu
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else :
                if cnt == 3 :
                    cnt = 1
                else : # 只出現一次
                    return nums[i - 1]
        return nums[-1] # 最後一個數字只出現一次