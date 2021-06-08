# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:42:08 2021

@author: Brian
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(roots,isConnected,n):
            res = []
            for root in roots:
                for i in range(n):
                    if isConnected[i][i] == 1 and isConnected[root][i] == 1 :
                        res += [i]
                        isConnected[i][i] = 0
            roots = res
            if roots : dfs(roots,isConnected,n)
            return     
        
        n = len(isConnected)
        ans = 0
        for i in range(n):
            if isConnected[i][i] == 1:
                isConnected[i][i] = 0
                ans += 1
                dfs([i],isConnected,n)
        return ans
        
        '''
        def dfs(isConnected,row,col,m,n):
            isConnected[row][col] = 2
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                if (0 <= row + dx < m) and (0 <= col + dy < n) and isConnected[row + dx][col + dy] == 1:
                    dfs(isConnected , row + dx , col + dy , m , n)
            if [row,col] == self.initial_position:
                print(isConnected)
                self.ans += 1
            return 
            
        m = len(isConnected)
        n = len(isConnected[0])
        self.ans = 0
        
        for row in range(m):
            for col in range(n):
                if isConnected[row][col] == 1:
                    self.initial_position = [row,col]
                    dfs(isConnected,row,col,m,n)
                    
        return self.ans
        '''