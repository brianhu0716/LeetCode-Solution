# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:02:33 2021

@author: Brian
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        stack_left,stack_right = [],[]
        ans = 0
        for idx,char in enumerate(s):
            if char == "(":
                stack_left.append(idx)
            else:
                stack_right.append(idx)
                if len(stack_right) >= 2 and stack_right[-1] - stack_right[-2] == 1:
                    if stack_left :
                        stack_right = stack_right[:-2]
                        stack_left.pop()
                    else:
                        ans += 1
                        stack_right = stack_right[:-2]

        while stack_left and stack_right:
            if stack_left[0] < stack_right[0]:
                ans += 1
                stack_left.pop(0)
                stack_right.pop(0)
            else: # stack_left[0] > stack_right[0]:
                ans += 2
                stack_right.pop(0)
            
                
        ans += (len(stack_left) + len(stack_right)) * 2
        
        return ans