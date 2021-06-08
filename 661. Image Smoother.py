# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:41:36 2021

@author: Brian
"""
'''
找當前位置周圍的八個點(上、下、左、右、左上、左下、右上、右下)的值做平均，要注意的是邊界只能row_max以及col_max之內，

'''
class Solution:
    def MovingAverage(self,row,col,M,row_max,col_max):
            neighbors = []
            for i in range(max(0,row - 1),min(row_max,row + 2)): # 到row + 1，但因為是上界為開邊界所以row + 2
                for j in range(max(0,col - 1),min(col_max,col + 2)):
                    neighbors.append(M[i][j])
            return sum(neighbors) // len(neighbors)
    def imageSmoother(self, M):
        row_max,col_max = len(M),len(M[0])
        MV = [[0 for j in range(col_max)] for i in range(row_max)] # moving average後的值
        for i in range(row_max):
            for j in range(col_max):
                MV[i][j] = self.MovingAverage(i,j,M,row_max,col_max)
        return MV