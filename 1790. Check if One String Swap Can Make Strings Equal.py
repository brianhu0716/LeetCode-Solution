# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:11:13 2021

@author: Brian
"""
'''
本題與#859類似

'''
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        i_diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                i_diff += [i]
                if len(i_diff) > 2:
                    return False
        if len(i_diff) == 2 and s1[i_diff[0]] == s2[i_diff[1]] and s1[i_diff[1]] == s2[i_diff[0]]:
            return True
        else:
            return False