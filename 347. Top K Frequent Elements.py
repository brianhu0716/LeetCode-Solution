# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:46:53 2021

@author: Brian
"""
nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10

d = {}
for n in nums:
    if n not in d.keys():
        d[n] = 1
    else:
        d[n] += 1
table = sorted([[d[key],key] for key in d.keys()])
ans = []
for i in range(k):
    ans += [table.pop()[1]]
