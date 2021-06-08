# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:14:45 2021

@author: Brian
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]

        for i in range(l := len(nums)):
            if nums[i] == target:
                ans[0] = i
                if nums[-1] == target: 
                    ans[1] = l - 1
                    return ans
                for j in range(i + 1,l):
                    if nums[j] != target:
                        ans[1] = j - 1
                        return ans

            elif nums[i] < target: continue
            else: break
        return ans
            