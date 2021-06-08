# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:54:37 2021

@author: Brian
"""
'''
由出現頻遇最高的數字開始刪除，直到剩下的數字個數小於原始長度的一半以上為止
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            d[n] = d.get(n,0) + 1
        table = sorted([[freq,num] for num,freq in d.items()])
        
        cnt,l = 0,len(arr)
        criterion = int(l // 2)
        while l > criterion:
            cnt += 1
            l -= table.pop()[0]
        return cnt