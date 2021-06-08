# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:23:28 2021

@author: brian.hu
"""

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()

    def insert(self, key: str, val: int) -> None:
        if key in self.dict:
            self.dict[key] = val
        else :
            self.dict[key] = val

    def sum(self, prefix: str) -> int:
        n = len(prefix)
        total = 0
        for key,val in self.dict.items() :
            if key[: n] == prefix :
                total += val
        return total