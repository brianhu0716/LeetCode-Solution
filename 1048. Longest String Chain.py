# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:01:17 2021

@author: brian.hu
"""
"""
類似BFS+字典的動態規劃，對於任一一個搜索的字，我們可以考慮在0 ~ n - 1的位置間擇一刪除，檢視
刪除後的字串是否在字典中，如果是的話dp[word_now]由dp[word_now]以及1 + dp[word_before]決定
找最大值
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:           
        words.sort(key = len)
        dictionary = {word : 1 for word in words}
        global_max = 1
        for word in words :
            for i in range(len(word)) :
                if (pred := word[: i] + word[i + 1 :]) in dictionary :
                    dictionary[word] = max(1 + dictionary[pred],dictionary[word])
            global_max = max(global_max,dictionary[word])  
                  
        return global_max