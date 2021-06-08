# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:17:20 2021

@author: Brian
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def helper(matrix,row,col):            
            if (row,col) in self.d.keys() : return self.d[(row,col)]
            
            if row == len(matrix) : return 0
            
            if col < 0 or col >= len(matrix[0]) : return float('inf')
            

            ans = matrix[row][col] + min(helper(matrix,row + 1,col - 1),helper(matrix,row + 1,col),helper(matrix,row + 1,col + 1))
                    
            self.d[(row,col)] = ans
                    
            return ans
        
        self.d = {}
        table = []
        for col in range(len(matrix[0])):
            table.append(helper(matrix,0,col))
        return min(table)