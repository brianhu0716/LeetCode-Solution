# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:42:56 2021

@author: Brian
"""
class Solution:
    def calculate(self, s: str) -> int:
        def findNumber(start,finish,s):
            for i in range(start,finish):
                if not s[i].isnumeric():
                    return i
            return finish
        
        stack_op,idx,ls = list(),0,len(s)        
        while idx < ls:
            if s[idx].isnumeric():
                n = s[idx : (end := findNumber(idx,ls,s))]
                stack_op.append(int(n))
                idx = end
            elif s[idx] == "-":
                if s[idx + 1] == "(" or s[idx + 1] == " ":
                    stack_op.append(s[idx])
                    idx += 1
                else: # "-" connect with digit --> ex : "-23"
                    n = s[idx + 1 : (end := findNumber(idx + 1,ls,s))]
                    stack_op.append(-int(n))
                    idx = end
            elif s[idx] == "(":
                stack_op.append(s[idx])
                idx += 1

            elif s[idx] == ")":
                    res = 0
                    while stack_op[-1] != "(":
                        res += stack_op.pop()
                    stack_op.pop() # remove "("
                    if stack_op:
                        if stack_op[-1] == "-": # ex : 2-(-3)
                            stack_op.pop()
                            stack_op.append(-res)
                        else:
                            stack_op.append(res)
                    else:
                        stack_op.append(res)
                    idx += 1
            else:
                idx += 1
                
        if len(stack_op) == 1:
            return stack_op[-1]
                
        return sum(stack_op) # 最後不包含括號的部分
"1 + 1"
" 2-1 + 2 "
"(1+(4+5+2)-3)+(6+8)"
"- (3 + (4 + 5))"

                
    