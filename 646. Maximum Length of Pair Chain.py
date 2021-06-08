# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:28:23 2021

@author: Brian
"""
"""
先把chairs排序，只要現在這個pair的start(pair[0])大於現在檢視的pair[j][1]，代表可以在dp[j]後再加上當前的pair，因此我們可以不斷的透過
這種種方式去檢驗當前dp[i]的最長長度
"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1 for pair in pairs]
        
        for i in range(l := len(pairs)):
            pair = pairs[i]
            for j in range(l - 1,-1,-1):
                if pair[0] > pairs[j][-1]:
                    dp[i] = max(dp[i],1 + dp[j])
        
        return max(dp)