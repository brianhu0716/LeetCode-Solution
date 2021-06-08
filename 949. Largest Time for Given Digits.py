#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:45:50 2021

@author: brian
"""
"""
use recursion with backtracking to find out all valid solution, than pick the 
largest one
"""
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        #if min(arr) > 2 : return ""
        def helper(res,used) :
            if len(res) == 1 and int(res) > 2 : return 
            
            elif len(res) == 2 and int(res) > 23 : return
            
            elif len(res) == 3 and int(res[2]) > 6 : return 
            
            elif len(res) == 4 :
                if int(res[2 :]) > 59 : return  
                self.ans += [res[:]]
                return 
                        
            
            for i in range(4) :
                if i not in used : 
                    helper(res + str(arr[i]),used + [i])
        self.ans = list()
        helper("",list())
        
        if not self.ans : return ""
        
        num = [int(possible) for possible in self.ans]
        self.ans = self.ans[num.index(max(num))]
        
        return self.ans[: 2] + ":" + self.ans[2 :]