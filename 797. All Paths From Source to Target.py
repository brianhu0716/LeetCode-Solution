# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:39:19 2021

@author: Brian
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(idx,graph,path):
            if path[-1] == len(graph) - 1:
                self.ans += [path[:]]
                return 
            for node in graph[idx]:
                path.append(node)
                dfs(node,graph,path)
                path.pop()
            return 
                
        self.ans = list()        
        dfs(0,graph,[0])
        return self.ans