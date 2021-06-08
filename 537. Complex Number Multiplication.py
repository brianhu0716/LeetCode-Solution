# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:02:49 2021

@author: brian.hu
"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        for idx,char in enumerate(num1) :
            if not char.isnumeric() :
                if idx == 0 : continue
                break
        coef1 = [int(num1[ : idx]),int(num1[idx + 1 : -1])]
        
        for idx,char in enumerate(num2) :
            if not char.isnumeric() :
                if idx == 0 : continue
                break
        coef2 = [int(num2[ : idx]),int(num2[idx + 1 : -1])]
        
        ans = list()
        for i in range(2) :
            for j in range(2) :
                ans.append(coef1[i] * coef2[j])
        return str(ans[0] - ans[-1]) + "+" + str(ans[1] + ans[2]) + "i"
            