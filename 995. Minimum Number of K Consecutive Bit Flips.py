# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:42:23 2021

@author: Brian
"""
class Solution:
    def minKBitFlips(self, A, K) -> int:
        nflip = 0
        for i in range((l := len(A))):
            if A[i] == 0:
                if (bound := i + K) <= l:
                    nflip += 1
                    updateindex = False
                    for j in range(i,bound): 
                        if A[j] == 0:
                            A[j] = 1
                        else:
                            A[j] = 0
                            if not updateindex :
                                i = j
                                updateindex = True
                    if not updateindex :
                        i = bound
                else:
                    nflip = -1
                    break
        print(A,nflip)
# A = [[0,0,1,0,0]]
# K = [3]

A = [[0,1,0],
      [0,0,1,1,0,1,0,1,1,1,0],
      [0,0,1,0,0],
      [0,0,0,1,0,1,1,0],
      [1,1,0]]
K = [1,
      4,
      3,
      3,
      2]
test = Solution()
for i in range(len(K)):
    test.minKBitFlips(A[i], K[i])