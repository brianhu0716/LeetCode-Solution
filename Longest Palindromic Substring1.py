# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:58:24 2021

@author: Brian
"""

import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.palindrome = []
        self.outerc = 0
        self.interc = 0
        for i in range(len(self.s)):            
            self.outerc += 1
            self.index = np.where(np.array([item for item in self.s]) == self.s[i])[0]           
            if self.index.size > 1:
                self.optimizePair()
                # for j in range(len(self.index)-1,-1,-1):
                for pair in self.pairs_sort:  # self.pairs_sort = [[],[],...]
                    self.interc += 1
                    self.furtherSearch(start = pair[1],end = pair[0])
                    if self.palindrome:
                        return self.palindrome[0]
        if not self.palindrome:
            self.palindrome += self.s[0] 
            return self.palindrome[0]
    def furtherSearch(self,start,end):
        interval = int(np.floor((start - end) / 2))
        flag = True
        for shift in range(1,interval + 1):
            if self.s[start - shift] != self.s[end + shift]:
                flag = False
                break
        if flag == True:
            self.palindrome += [self.s[end:start + 1]] 
    def optimizePair(self):
        self.pairs = []
        self.diff = []
        for i in range(len(self.index)):
            for j in range(i + 1,len(self.index)):
                self.pairs += [(self.index[i],self.index[j])]
                self.diff += [self.index[j] - self.index[i]]

        self.diff_sort = np.argsort(np.array(self.diff)) # self.diff_sort 是index
        self.diff_sort = list(reversed(self.diff_sort))
        self.pairs = np.array(self.pairs)
        self.pairs_sort = self.pairs[self.diff_sort] 
                
        # for i in range(start,end,-1):
        #     self.shift = 1
        #     self.interval = int(np.floor((start - end) / 2))
        #     while self.shift <= self.interval:
        #         if self.s[i - self.shift] == self.s[end + self.shift]:
        #             self.shift += 1
        #         else:
        #             break
        #     if self.shift >= self.interval:
        #         self.palindrome += [self.s[end:start + 1]]
        #         break

s = ["babad", # bab
     "cbbd", # bb
     "a", # a
     "ac", # a
     "aacabdkacaa"] # aca       
test = Solution()
for string in s:
    test.longestPalindrome(string)
    print(test.palindrome[0])            
            
                