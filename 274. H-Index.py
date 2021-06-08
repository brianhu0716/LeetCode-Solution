# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:36:32 2021

@author: brian.hu
"""
# H-index要越大越好
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n,H = len(citations) - 1,list()
        for i in range(n,-1,-1) :
            H.append(min(n - i + 1, citations[i])) # 當前的H-index最大值(大於該引用數的篇數或該引用數取最小)
            if len(H) > 1 and H[-1] < H[-2] : return H[-2] # H-index開始遞減，return 最大值
        return H[-1] # 