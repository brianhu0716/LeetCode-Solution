# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:29:29 2021

@author: Brian
"""


import numpy as np
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # self.arr = np.array(arr)
        self.arr = arr
        i = 0
        while True:
            if self.arr[i] == 0:
                if i <= len(self.arr) - 2:
                    self.arr[i+2:] = self.arr[i+1:-1]
                    self.arr[i+1] = 0
                    i += 2
                elif i == len(self.arr) - 1:
                    break 
            else:
                i += 1
            if i >= len(self.arr):
                break
        self.arr = list(self.arr)
test = Solution()
test.duplicateZeros(arr = [1,0,2,3,0,4,5,0])
test.arr
