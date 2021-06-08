# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 00:35:34 2021

@author: Brian
"""
'''

'''
'''法一'''
class Solution():
    def groupAnagrams(self, words):
        groups = {}
        for word in words:
            key = str(sorted(word)) #
            if key not in groups.keys():
                groups[key] = list()
                groups[key] += [word]
            else:
                groups[key].append(word)
        
        return list(groups.values())
    

'''法二'''
import collections # 引入collections模組
class Solution():
    def groupAnagrams(self, words):
        groups = collections.defaultdict(list) # 宣告一個空字典，其內部的值都是空字串
        for word in words:
            key = str(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())


