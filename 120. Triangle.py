# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:14:23 2021

@author: Brian
"""
'''

'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def helper(row,idx):
            if (row,idx) in self.d.keys(): return self.d[(row,idx)]
            if row >= self.len: return 0
            
            temp = self.triangle[row][idx] + min(helper(row + 1,idx),helper(row + 1,idx + 1))
            self.d[(row,idx)] = temp
            return temp
        
        self.len = len(triangle)
        self.triangle = triangle
        self.d = dict()
        return helper(0,0)