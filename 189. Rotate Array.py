# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:37:42 2021

@author: Brian
"""

nums = [1,2,3,4,5,6,7]
k = 3


for i in range(k):
    res = nums[-1]
    nums[1:] = nums[:-1]
    nums[0] = res
 
