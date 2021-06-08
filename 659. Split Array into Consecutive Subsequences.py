# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 08:41:23 2021

@author: Brian
"""
nums = [1,1,2,3,3,4,4,5,5]
r = []
if len(nums) >= 2:
    i = 0
    while i <= len(nums) - 2:
        if nums[i + 1] - nums[i] == 1:
            i += 1
        elif nums[i + 1] - nums[i] == 0:
            r += [nums.pop(i + 1)]
            if i == len(nums) - 1:
                break
        else:
            print("False")
            break

if len()