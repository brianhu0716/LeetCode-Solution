# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:07:25 2021

@author: Brian
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def pascal(row,col):
            if (row,col) in self.d.keys(): return self.d[(row,col)]
            if col == 0 or col == row : return 1
            else:
                res = pascal(row - 1,col) + pascal(row - 1,col - 1)
                self.d[(row,col)] = res
                return res
        self.d = dict()
        ans = list()
        for row in range(numRows - 1,-1,-1):
            res = list()
            for col in range(0,row + 1):
                res.append(pascal(row,col))
            ans += [res]
        return ans[::-1]