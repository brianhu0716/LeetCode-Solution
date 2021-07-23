# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:52:58 2021

@author: Brian Hu
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        star, left = list(), list()
        for idx, char in enumerate(s):
            if char == '*':
                star.append(idx)
            elif char == '(':
                left.append(idx)
            else:
                if not left:
                    if not star:  # no left parathesis and star can match right parathesis
                        return False
                    else: # star can be treated as left parathesis
                        star.pop()
                else:
                    left.pop()
        while left and star: # if there is still left parathesis, we now treat star as right parathesis
            if star[-1] > left[-1]: # star appears beyond left parathesis
                star.pop()
                left.pop()
            else:
                return False
        return True if not left else False # no parathesis match remaining left parathesis