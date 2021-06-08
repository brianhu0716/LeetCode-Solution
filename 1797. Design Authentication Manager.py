# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:34:01 2021

@author: Brian
"""

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.d = dict()
        self.duration = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.d.keys() : return # 根本沒有的項目，直接跳過
        if currentTime >= (self.d[tokenId] + self.duration) : # 過期的項目,直接刪除
            del self.d[tokenId]
            return 
        self.d[tokenId] = currentTime # 沒過期的項目，更新起始使用時間

    def countUnexpiredTokens(self, currentTime: int) -> int:
        expired,n = list(),0
        for key in self.d.keys():
            if currentTime < (self.d[key] + self.duration) : n += 1 # 計算沒過期得項目個數
            else: expired.append(key)
        for key in expired: # 刪除過期項目
            del self.d[key]
        return n