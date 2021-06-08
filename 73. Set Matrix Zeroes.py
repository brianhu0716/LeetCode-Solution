# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:57:38 2021

@author: Brian
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_idx = set()
        zero_col_idx = set()
        for row in range(lr := len(matrix)):
            for col in range(lc := len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_row_idx.add(row)
                    zero_col_idx.add(col)
        for row in range(lr):
            for col in range(lc):
                if matrix[row][col] != 0:
                    if row in zero_row_idx or col in zero_col_idx:
                        matrix[row][col] = 0