# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:52:06 2021

@author: Brian
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:      
        def dfs(idx):
            if not graph[idx] :
                self.safe.add(idx)
                return True
            
            if idx in self.safe : return True
                            
            if idx in self.path : return False # 避免陷入無限循環
            
            ans = True
            self.path.add(idx) # we've already walked through the idx
            for next_stop in graph[idx]: # search the next stop from current stop(idx)
                ans = ans & dfs(next_stop)
                #print(idx,next_stop,ans,self.path)
                
            if ans : 
                self.safe.add(idx) # ans == True means we can reach safe stop from each next_stop in graph[idx]
                self.path.remove(idx) # we only remain the path which can't reach the safe stop in self.path
            #print(idx,self.safe,self.path)
            
            return ans
        
        self.safe = set()
        self.path = set()
        for i in range(len(graph)):
            dfs(i)
            
        return sorted(list(self.safe))