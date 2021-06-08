# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:49:41 2021

@author: brian.hu
"""

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        dp1 = [1 for _ in nums]
        for i in range(n := len(nums)) : 
            for j in range(i) :
                if nums[i] > nums[j] :
                    dp1[i] = max(1 + dp1[j],dp1[i])
        #print(dp1)
        dp2 = [1 for _ in nums]
        for i in range(n - 1,-1,-1) :
            for j in range(n - 1,i,-1) :
                if nums[i] > nums[j] :
                    dp2[i] = max(1 + dp2[j],dp2[i])
        #print(dp2)
        max_len = 0
        for i in range(1,n - 1) :
            if dp1[i] == 1 or dp2[i] == 1 : continue # 1代表是單邊遞增或單邊遞減(不滿足要求)
            max_len = max(max_len,dp1[i] + dp2[i] - 1)
        
        return n - max_len