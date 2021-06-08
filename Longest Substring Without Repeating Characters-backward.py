# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:10:13 2021

@author: Brian
"""



"""
Created on Sat Feb  6 17:51:05 2021

@author: Brian
"""

class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        self.s = s
        if len(self.s) == 1:
            self.maxima = 1
        else:
            i = 0
            self.init = 0
            self.maxima = 0
            while i <= len(self.s) - 2:
                if self.s[i+1] not in self.s[self.init:i+1]:
                    self.maxima = max(self.maxima,i - self.init + 1 + 1)
                    i += 1
                else:
                    self.maxima = max(self.maxima,i - self.init + 1)
                    self.findrepeat(flag = self.s[i+1], end = self.init - 1, start = i)
                    i += 1
        return self.maxima
    def findrepeat(self,flag,end,start):
        self.reindex = 0
        for i in range(start,end,-1):
            if self.s[i] == flag:
                self.reindex = i 

        self.init = self.reindex + 1
        
        # self.s = s
        # self.init = 0
        # self.maxima = 0
        # while True:
        #     for i in range(self.init,len(self.s)-1):
        #         if self.s[i+1] not in self.s[self.init:i+1]:
        #             self.maxima = max(self.maxima, i + 1 - self.init + 1)
        #         else:
        #             self.init = i + 1
        #             self.maxima = max(self.maxima,1)
        #             break
        #     if self.init > len(self.s) - 2:
        #         break
        # return self.maxima


s = ["abcabcbb", # 3
     "bbbbb", # 1
     "pwwkew", # 3
     'aab', # 2
     'aba',# 2
     '', # 0
     ' ', # 1     
     "dvdf" # 3
     ]
     
test = Solution()
for i in range(len(s)):
    test.lengthOfLongestSubstring(s[i])
    print(test.maxima)
