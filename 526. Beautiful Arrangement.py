# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:51:37 2021

@author: brian.hu
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(used,idx) :
            if idx == n + 1 :
                self.ans += 1
            
            for num in range(1,n + 1) :
                # 該數字沒被用過且放入的位置可以被該數整除，或該數可以被放入的位置整除
                if (num not in used) and (num % idx == 0 or idx % num == 0) : 
                    used.add(num)
                    dfs(used,idx + 1)
                    used.remove(num)
        self.ans = 0            
        dfs(set(),1)
        return self.ans