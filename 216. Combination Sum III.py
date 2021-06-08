# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:20:51 2021

@author: brian.hu
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(start,k,n,path,length):
            if n == 0 : 
                if len(path) == k : self.ans.add(tuple(path[:]))
                return 
            ''' 一個數字只能用一次，設定start就不需要一直檢查當前num是否有在path中，也不
                回出現ans中有重複的排列組合答案'''
            for num in range(start,10): 
                if n - num >= 0 and length + 1 <= k :
                    dfs(num + 1,k,n - num,path + [num],length + 1)
        
        self.ans = set()
        
        if n > 45 : return self.ans
        
        dfs(1,k,n,list(),0)
        
        return self.ans