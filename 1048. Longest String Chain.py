#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:17:36 2021

@author: brian
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:           
        words.sort(key = len)
        dictionary = {word : 1 for word in words}
        global_max = 1
        for word in words :
            # check word which differ by 1 digit form word is in dict
            # if so, update length
            for i in range(len(word)) : 
                if (pred := word[: i] + word[i + 1 :]) in dictionary :
                    dictionary[word] = max(1 + dictionary[pred],dictionary[word])
            global_max = max(global_max,dictionary[word])  
                  
        return global_max