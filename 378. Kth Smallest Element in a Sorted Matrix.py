# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:05:52 2021

@author: brian.hu
"""
# 直接把value讀出來，sort後找第k - 1個值
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([matrix[i][j] for j in range(len(matrix[0])) for i in range(len(matrix))])[k - 1]