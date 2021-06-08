# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:33:17 2021

@author: Brian
"""

nums = [1,2,3,4]
nums = [1,1,2,3]
decode = []
for i in range(0,len(nums),2):
    decode += [nums[i + 1]] * nums[i]
print(decode)