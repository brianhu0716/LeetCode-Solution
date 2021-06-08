# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:05:17 2021

@author: Brian
"""

class Solution:
    def findMaxForm(self, S: List[str], M: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for str in S:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(M, zeros - 1, -1):
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[M][N]
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count0and1(s):
            n0,n1 = 0,0
            for char in s:
                if char == "0": n0 += 1
                else : n1 += 1
            
            return n0,n1
       
        def helper(idx,strs,m,n):
            if (m,n,idx) in self.d.keys() : return self.d[(m,n,idx)]
            
            if idx == len(strs) : return 0
            
            n0,n1 = count0and1(strs[idx])
            #n0,n1 = strs[idx].count("0"), strs[idx].count("1")
            
            if n0 > m or n1 > n : 
                ans = helper(idx + 1,strs,m,n)
            else:
                ans = max(1 + helper(idx + 1,strs,m - n0,n - n1),helper(idx + 1,strs,m,n))
            
            self.d[(m,n,idx)] = ans
            
            return ans  
        
        self.d = {}        
        
        return helper(0,strs,m,n)
'''
              