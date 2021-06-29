# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:45:24 2021

@author: Brian Hu
"""
'''
using dict to save the key, value pair, 
then to check whether the key in string has corresponding replacement value in dict, 
if there doesn't exist the replacement value, we use "?" to subsitute the key
'''
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {letter: dict() for letter in string.ascii_lowercase}
        for key, value in knowledge:
            d[key[0]][key] = value
        i = 0
        while i < len(s):
            if s[i] == "(":
                for j in range(i + 1, len(s)):
                    if s[j] == ")":
                        if s[i + 1: j] in d[s[i + 1]]:
                            char = d[s[i + 1]][s[i + 1: j]]
                            s = s[:i] + char + s[j + 1:]
                            i += len(char)
                        else:
                            s = s[:i] + "?" + s[j + 1:]
                            i += 1
                        break
            else:
                i += 1
        return s