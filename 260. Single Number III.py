# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:58:25 2021

@author: brian.hu
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        cnt = 1
        ans = list()
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] :
                cnt += 1
            else :
                if cnt != 2 :
                    ans.append(nums[i - 1])
                if len(ans) != 2 : # 還沒找到答案
                    cnt = 1
                else : # 找到兩個數字
                    return ans
        return ans + [nums[-1]] # 第二個缺的數字是nums[-1]