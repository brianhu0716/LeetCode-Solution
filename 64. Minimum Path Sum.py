# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:47:04 2021

@author: Brian
"""
'''
求左上走到右下路徑中和最小的值為多少，我們首先寫出遞迴式：f(row,col) = grid[row][col] + min(f(row - 1,col) , f(row,col - 1))，該式
代表當我們需要知道走道某座標row,col的最小路徑和時，我們需要先知道走到row - 1,col以及走到row,col - 1的路徑和，並找到最小值後加上
row,col的值回傳。由於是找最小值，當超出邊界時(row = -1 or col = -1)，我們回傳值為無窮大，避免取最小值時篩選到超出邊界，
但需要注意的是當我們在row = col = 0時做最後一次遞迴呼叫，必須要把回傳值設成0(因為此時兩個呼叫座標都超出邊界，同時回傳無窮大會導致
 答案出錯)，因此我們初始化字典時先給定兩組座標分別為(-1,0)以及(0,-1)時，必須回傳0，且在進入遞迴呼叫時，應先檢查字典在檢查邊界

'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.d = {(-1,0) : 0, (0,-1) : 0}
        max_row,max_col = len(grid) - 1,len(grid[0]) - 1
        def findMinPath(row,col,grid):
            if (row,col) in self.d.keys(): return self.d[(row,col)]
            if row == -1 or col == -1:return float('inf')  
            
            temp = grid[row][col] + min(findMinPath(row - 1,col,grid), findMinPath(row,col - 1,grid))
            self.d[(row,col)] = temp
            
            return temp
            
        return grid[max_row][max_col] + min(findMinPath(max_row - 1,max_col,grid),findMinPath(max_row,max_col - 1,grid))