# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:44:11 2021

@author: brian.hu
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.cashe = list()
        self.dict = dict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.dict :
            self.cashe.remove(key)
            self.cashe.append(key)
            return self.dict[key]
        return -1
            
    def put(self, key: int, value: int) -> None:        
        if key in self.dict :
            self.dict[key] = value
            self.cashe.remove(key)
            self.cashe.append(key)
            return 
        if len(self.dict) >= self.capacity :
            rmv_key = self.cashe.pop(0) # cashe超出最大容量時，remove最不常用的key值
            del self.dict[rmv_key]
        self.dict[key] = value
        self.cashe.append(key)
        return 