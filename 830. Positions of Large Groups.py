# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:08:58 2021

@author: Brian
"""

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans,ls = [[0]],len(s)
        for i in range(0,ls): 
            if i == ls - 1:
                if s[i] != s[i - 1]: 
                    ans.pop()
                else:
                    ans[-1].append(i)
                    if ans[-1][1] - ans[-1][0] + 1 < 3: ans.pop()
                
                break
                
            if s[i] != s[i + 1]:
                ans[-1].append(i)
                if ans[-1][1] - ans[-1][0] + 1 < 3: ans.pop()
                    
                ans += [[i + 1]]
        return ans
            