# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:12:23 2021

@author: Brian Hu
"""

class Solution:
    def clumsy(self, n: int) -> int:
        res = n # initial res
        operator = "*" # next operator
        for i in range(n - 1,0,-1):
            if operator == "*":
                res *= i
                operator = "/" # next operator
            elif operator == "/":
                res = res // i
                operator = "+" # next operator
            elif operator == "+": # number behind "+" can be added directly to ans
                if "ans" not in locals():
                    init = True
                    ans = i
                else:
                    ans += i
                operator = "-" # next operator
            else:
                # update the res value to ans first, then re-initialize res value
                if init:
                    ans += res
                    init = False
                else:
                    ans -= res
                res = i
                operator = "*"  # next operator
                

        if n <= 4 :  # before the first "+", ans is not in variables
            return ans + res if "ans" in locals() else res
        else: 
            return ans - res