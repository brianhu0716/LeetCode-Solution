# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:56:11 2021

@author: Brian
"""
'''
建立一個字字典不斷儲存當前(row,col)所計算的值，若之後再呼叫到相同位置的值時，先判斷字典是否曾計算過答案，若有的話則值接回傳之
計算過得值，否則祭計算這個新的位置的值
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(row,col):
            if (row,col) in self.d.keys(): return self.d[(row,col)]
            
            if col == 0 or row == col: return 1
            else: 
                res = pascal(row - 1,col - 1) + pascal(row - 1,col)
                self.d[(row,col)] = res
                return res
        self.d = {}
        ans = list()
        for j in range(rowIndex + 1):
            ans.append(pascal(rowIndex,j))
        return ans