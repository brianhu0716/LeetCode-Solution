# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:37:28 2021

@author: Brian
"""
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in range(len(ops)):
            if ops[i] == "+" :
                stack.append(stack[-1] + stack[-2])
            elif ops[i] == "C":
                stack.pop()
            elif ops[i] == "D" :
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ops[i]))
        return sum(stack)