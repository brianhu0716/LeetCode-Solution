# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:57:57 2021

@author: Brian
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dfs(times,duration,node):
            # 代表由同樣的起點出發到同樣的終點已經有路徑可以更快到達，因此不需要跑耗時較長的路徑
            if duration >= self.memo[node] : return  
            
            self.memo[node] = duration

            for time,next_node in sorted(graph[node]): # 在相同的起點時，永遠都先嘗試耗時較短的路徑
                dfs(graph,duration + time,next_node)

        
        self.memo = {i : float("inf") for i in range(1,n + 1)}
        
        graph = collections.defaultdict(list)
        for source,target,time in times:
            graph[source].append((time,target))

        dfs(graph,0,k)
        
        #print(self.memo)
        max_time = max(self.memo.values())
        return max_time if max_time != float('inf') else -1 # 如果有耗常無窮大，代表該點無法由source到達