# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:11:45 2021

@author: Brian Hu
"""

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        imax = [0 ,0]
        vmax = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > vmax:
                    imax = [i, j]
                    vmax = mat[i][j]
        return imax