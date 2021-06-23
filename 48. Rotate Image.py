# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:27:08 2021

@author: Brian Hu
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        orig = [[matrix[i][j] for j in range(n)] for i in range(n)]
        for col in range(n - 1,-1,-1):
            for row in range(n):
                matrix[row][col] = orig[(n - 1) - col][row]
        return matrix