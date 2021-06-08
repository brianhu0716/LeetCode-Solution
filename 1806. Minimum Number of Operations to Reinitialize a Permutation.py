# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:48:50 2021

@author: Brian
"""
'''
暴力解
'''
from copy import deepcopy
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        res = [0 for i in range(n)]
        cnt = 0
        while True:
            for i in range(n):
                if i % 2 == 0 : res[i] = perm[i // 2]
                    
                else : res[i] = perm[n // 2 + (i - 1) // 2]
                    
            cnt += 1

            if res == [i for i in range(n)]: return cnt
               
            perm = copy.deepcopy(res)