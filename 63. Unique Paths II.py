# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:05:12 2021

@author: Brian
"""
'''
本題一樣是由左上走到右下的路徑總數計算，但多一項限制：當矩陣中有值為1時，代表該點有障礙物不能通行
解題思路與62題類似，欲知走到座標(row,col)有幾種路徑，必須先逆推走到(row - 1,col)以及(row,col - 1) 有幾種路徑後加總，
因此遞迴式為f(row,col) = f(row - 1,col) + f(row,col - 1)，唯一不同的是我們的base case需要修正，原本第62題當座標的row或col碰到1時
及回傳1，但此例中必須要走完全程(走到(0,0))才可以確定是否能回傳1(因為不確定row = 0 或col = 0的路上是否有障礙物)
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:return 0
        self.d = {}
        self.obstacleGrid = obstacleGrid
        def countPath(row,col):
            if row == -1 or col == -1: return 0
            if (row,col) in self.d.keys(): return self.d[(row,col)]
            if self.obstacleGrid[row][col] == 1: return 0
            if row == col == 0:
                return 1 if self.obstacleGrid[row][col] == 0 else 0
    
            
            temp1 = countPath(row - 1,col)
            self.d[(row - 1,col)] = temp1
            temp2 = countPath(row,col - 1)
            self.d[(row,col - 1)] = temp2
            
            return temp1 + temp2
        return countPath(len(obstacleGrid) - 1,len(obstacleGrid[0]) - 1)