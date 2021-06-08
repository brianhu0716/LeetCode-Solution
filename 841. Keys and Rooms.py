# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:30:58 2021

@author: brian.hu
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(start,path) :
            path.add(start) # 防止rooms[i]是[]
            
            if len(path) == Nrooms :
                self.flag = True
                return 
            ''''
            path.add(start) 不可以在這裡，如果rooms[i]是[]會直接return 回上一個狀態，
            代表永遠都無法走到這個空房間
            '''
            for end in rooms[start] :
                if not self.flag and end not in path :
                    dfs(end,path)
        
        self.flag = False
        Nrooms = len(rooms) 
        dfs(0,set())
        return self.flag