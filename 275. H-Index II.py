# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:36:45 2021

@author: brian.hu
"""
# 與274類似
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n,H = len(citations) - 1,list()
        for i in range(n,-1,-1) :
            H.append(min(n - i + 1, citations[i]))
            if len(H) > 1 and H[-1] < H[-2] : return H[-2]
        return H[-1]