# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:40:44 2021

@author: Brian
"""

class Solution(object):    
    def findCheapestPrice(self, n, flights, src, dst, k):
        def dfs(start,k):
            if (start,k) in memo : return memo[(start,k)]

            if start == dst : 
                return 0
            if k < 0 : 
                return float('inf')


            res = float('inf')
            for next_start,price in graph[start]:

                res = min(res,price + dfs(next_start,k - 1))

            memo[(start,k)] = res

            return memo[(start,k)]
        
        graph = collections.defaultdict(list)
        for start,end,price in flights:
            graph[start].append([end,price])
            
        memo = dict()
        ans = dfs(src,k)
        
        return ans if ans != float('inf') else -1    
       