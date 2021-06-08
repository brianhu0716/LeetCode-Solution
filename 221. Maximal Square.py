# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:06:08 2021

@author: Brian
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def helper(row,col):
            if not (0 <= row < self.m) or not (0 <= col < self.n) : return 0
            
            if self.memo[row][col] != -1 : return self.memo[row][col]   
            
            if self.matrix[row][col] == "0" : return 0

            ans = 1 + min(helper(row - 1,col),helper(row,col - 1),helper(row - 1,col - 1))
            self.memo[row][col] = ans

            return ans
        
        self.m,self.n = len(matrix),len(matrix[0])
        self.matrix = matrix
        self.memo = [[-1 for row in range(self.n)] for col in range(self.m)]
        max_side = 0
        
        for row in range(self.m - 1,-1,-1):
            for col in range(self.n - 1,-1,-1):
                ans = helper(row,col)
                self.memo[row][col] = ans
                max_side = max(max_side,ans)
                
        #print(self.memo)
        return max_side ** 2
    
        '''
        def helper(row,col):
            if (row,col) in self.memo.keys() : return self.memo[(row,col)]    
            
            if not (0 <= row < self.m) or not (0 <= col < self.n) : return 0
            
            if self.matrix[row][col] == "0" : return 0

            ans = 1 + min(helper(row - 1,col),helper(row,col - 1),helper(row - 1,col - 1))
            self.memo[(row,col)] = ans

            return ans
        
        self.m,self.n = len(matrix),len(matrix[0])
        self.matrix = matrix
        self.memo = dict()
        for row in range(self.m - 1,-1,-1):
            for col in range(self.n - 1,-1,-1):
                ans = helper(row,col)
                self.memo[(row,col)] = ans
                
        #print(self.memo)
        return (max(self.memo.values())) ** 2 if self.memo else 0
        '''
'''
test case = 
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] # 4
[["0","1"],["1","0"]] # 1
[["0"]] # 0
[["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]] # 16
'''