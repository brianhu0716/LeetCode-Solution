# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:00:25 2021

@author: Brian
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(want,source):
            if want in self.memo.keys() : return self.memo[want] 
            if want in source : # 形成cycle，ex : [1,2],[2,3],[3,1]
                self.memo[want] = False
                return False
            
            ans = True
            source.append(want) # 將當前要上的課程加入源頭
            #print(source)
            for idx in range(len(prerequisites)):
                if prerequisites[idx][0] == want :
                    ans = ans & dfs(prerequisites[idx][1],source) # 搜索當前要上的課程的預修課程所需的預修課程
                    
            self.memo[want] = ans # 把當前要上的課程是否可行的結果紀錄下來(沒有cycle就是True，有cycle是False)
            source.pop()
            #print(self.memo,source)
            return ans
        
        self.memo = dict()
        for want,need in prerequisites:
            if not dfs(want,[]) : return False # 當前要上的課程以及所需的先修課中有形成cycle
        return True