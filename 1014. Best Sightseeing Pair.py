# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:17:36 2021

@author: Brian Hu
"""
"""
maximize i + A[i] + A[j] - j for j > i
because i should less than j, we can update j related parameters first, so 
the first max is the choose max of (A[j] - j ) + (A[j_before] + j_before) , 
then we update the max of A[j] + j as val to use it in next round to calculte 
"""
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = val = 0
        for i, x in enumerate(A):
            ans = max(ans, x - i + val)
            val = max(val, x + i)
        return ans 