# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:13:01 2021

@author: Brian
"""
'''
max_so_far是維持到目前為止的最大總和
max_end_here是決定當前的數字是否會成為新起點的參數，如果當前的數字大於累積到當前的數字和，則使當前的數字做為新
起始點，否則維持原起點繼續累加。而當max_end_here累加到比max_so_far還要大時，代表我們需要更新子數列和的最大值
'''
nums = [-2,1,-3,4,-1,2,1,-5,4]
max_so_far = max_end_here = nums[0]
for i in range(1,len(nums)):
    max_end_here = max(nums[i],max_end_here + nums[i])
    max_so_far = max(max_so_far,max_end_here)
    

