# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:37:21 2021

@author: Brian
"""

"""
Created on Sat Feb  6 19:30:57 2021

@author: Brian
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:30:57 2021

@author: Brian
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:37:21 2021

@author: Brian
"""

"""
Created on Sat Feb  6 19:30:57 2021

@author: Brian
"""

import numpy as np
class Solution:
    def longestValidParentheses(self, s) -> int:
        i = 0
        self.s = s
        self.pairs = []
        self.c = 0
        self.flag = []
        if len(s) <= 1: # in case s = '','('...
            return 0
        while True:
            if self.s[i] == '(' and self.s[i+1] == ')':
              self.c += 1
              self.flag += [(i,i+1)]
              i += 2              
            elif self.s[i] == '(' and self.s[i+1] == '(':
                self.checkconsecutive(i)
                i = self.fi
                    
            else:
                 i += 1
                 # self.pairs += [self.c]
                 self.c = 0 

            self.pairs += [self.c] 
            
            if i > len(self.s) - 2:
                break
        if len(self.flag) > 1:    
            for i in range(len(self.flag)-1):
                if self.flag[i+1][0] - self.flag[i][1] != 1:
                    break
                else:
                    if '(' in self.s[0:self.flag[0][0]] and ')' in self.s[self.flag[-1][1] + 1:]:
                        self.pairs += [len(self.flag) + len(self.s[0:self.flag[0][0]])]
                    # condition = True
            # if condition and len(self.s[0:self.flag[0][0]]) == len(self.s[self.flag[-1][1]:]):
            #     if '(' in self.s[0:self.flag[0][0]] and ')' in self.s[self.flag[-1][1]:]:
            #         self.pairs += [len(self.flag) + len(self.s[0:self.flag[0][0]])]
            #         return max(self.pairs) * 2
            
        return max(self.pairs) * 2
    def checkconsecutive(self,fi):
        self.fi = fi
        for i in range(fi,len(self.s)):
            if self.s[i] == ')':
                break
        shift = i-self.fi
        if len(self.s[self.fi:i]) == len(self.s[i:i+shift]) and (np.array([item for item in self.s[i:i+shift]]) == ')').all():
            self.c += i - self.fi 
            self.fi = i + shift
        else:
            self.c = 0
            self.fi = fi + 1
    
s = ['()((())))', # 8
     '()()', # 4
     '()(()', # 2 
     '())()', # 2
     ')(', # 0
     '())((()))', # 6
     '()(((()))', # 6
     '(()())', # 6
     ")()())", # 4
     "(()()", # 4
     "((()))())"]  

test = Solution()
for i in range(len(s)):
    test.longestValidParentheses(s[i])
    print(max(test.pairs) * 2)

            
                

