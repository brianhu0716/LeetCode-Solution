# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:33:03 2021

@author: -
"""
'''
解題思路:
(a) 
'''
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        i = 0
        l,w = len(matrix[0]),len(matrix)
        while i < w:
            if target < matrix[0][0] or target > matrix[-1][-1]:
                return False
            elif matrix[i][-1] >= target and matrix[i][0] <= target:
                for j in range(l):
                    if matrix[i][j] == target:
                        return True
                    elif matrix[i][j] > target:
                        break
                    else:
                        continue
                return False
            else:
                i += 1
        return False

matrix = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]],
          [[1,3,5,7],[10,11,16,20],[23,30,34,60]]]
target = [3,
          13]
test = Solution()
for i in range(len(matrix)):
    print(test.searchMatrix(matrix[i], target[i]))