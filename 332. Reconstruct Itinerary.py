# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:48:47 2021

@author: brian.hu
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.d = collections.defaultdict(list)

        for start,end in tickets :
            self.d[start].append(end)
            
        def dfs(n,used,start,path) :
            if len(used) == n :
                self.ans.append(path[:] + [start])
                return 
            
            path.append(start)
            for end in self.d[start] :
                if [start,end] not in used :
                    dfs(n,used + [[start,end]],end,path)
            path.pop()


        self.ans = list()
        dfs(len(tickets),list(),"JFK",list())
        print(self.ans)
        return sorted(self.ans)[0]