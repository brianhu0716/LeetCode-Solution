# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 23:02:38 2021

@author: Brian
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,c,l = 0,0,len(nums)
        while i < l - c:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                c += 1
            else :
                i += 1
                
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(l := len(nums)):
            if nums[i] == 0:
                lp = i
                break
        if "lp" not in locals(): return nums
        rp = lp + 1
        while rp < l and lp < rp:
            if nums[rp] != 0:
                nums[rp],nums[lp] = nums[lp],nums[rp]
                lp += 1
                rp += 1
            else:
                rp += 1
        return nums