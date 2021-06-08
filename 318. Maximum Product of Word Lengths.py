# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:36:43 2021

@author: brian.hu
"""
import collections
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # sort_words = sorted(words,key = lambda x : len(x))
        d = collections.defaultdict(set)
        for word in words :
            d[word] = set(word)
        
        max_prod = 0
        for i in range(n := len(words)) :
            for j in range(i + 1,n) :
                if not d[words[i]] & d[words[j]] :
                    max_prod = max(max_prod,len(words[i]) * len(words[j]))
        return max_prod