# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 13:32:29 2021

@author: Brian
"""

import numpy as np
class Solution:
    def longestValidParentheses(self, s) -> int:
        self.pairs = 0
        self.flag = []
        i = 0
        count = 0 # 計算連續出現多少次()'的指標
        while i <= len(s) - 1:
            if len(s) < 2:
                break
            if s[i] == '(' and s[i+1] == ')':
                self.pairs += 1
                if count == 0:
                    self.flag += [self.pairs]
                else:
                    self.flag[-1] = self.pairs 
                i += 2
                count += 1
            #elif: # ()(())
            else:
                self.pairs = 0
                i += 1
                count = 0                   
        if not self.flag:
            return 0
        else:
            return max(self.flag) * 2
test = Solution()
test.longestValidParentheses(s = '(()())')
# test.pairs
test.flag                
