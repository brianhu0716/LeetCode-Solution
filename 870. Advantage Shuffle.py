# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:54:05 2021

@author: Brian
"""
'''
'''
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        B = sorted([[val,idx] for idx,val in enumerate(B)])
        ans = [0 for _ in A]
        while A :
            if A[-1] > B[-1][0]: ans[B[-1][1]] = A.pop()    
            else: ans[B[-1][1]] = A.pop(0)
            B.pop()

        return ans  