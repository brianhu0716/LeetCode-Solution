# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:33:21 2021

@author: Brian
"""
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
ans = []
for b in arr2:
    i = 0
    while i < len(arr1):
        if arr1[i] == b:
            ans += [b]
            arr1.remove(b)
        else:
            i += 1
print((ans := ans + arr1))