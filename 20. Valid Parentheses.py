# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:50:40 2021

@author: brian.hu
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for char in s :
            if char == "(" or char == "[" or char == "{" :
                stack.append(char)
            else :
                if not stack : return False # 缺少左括號
                
                if char == ")" and stack[-1] == "(" :
                    stack.pop()
                elif char == "]" and stack[-1] == "[" :
                    stack.pop()
                elif char == "}" and stack[-1] == "{" :
                    stack.pop()
                else : return False # 左右括號型態不匹配
        if stack : return False # 缺少右括號
        
        return True