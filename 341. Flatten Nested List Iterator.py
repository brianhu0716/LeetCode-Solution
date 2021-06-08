# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:39:27 2021

@author: brian.hu
"""
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        def dfs(arr) : # 利用dfs把nestedlist中的所有值依序讀出來
            for sub_arr in arr :
                if sub_arr.isInteger() :
                    self.list.append(sub_arr.getInteger())
                else :
                    dfs(sub_arr.getList())
        
        self.list = deque()
        dfs(nestedList)
        
    def next(self) -> int:
        return self.list.popleft()
    
    def hasNext(self) -> bool:
        return self.list        

