# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 00:55:00 2021

@author: Brian
"""

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def checkUpper(flag, start, end, s):
            for i in range(start, end):
                if flag == s[i]:
                    return i + 1, True
                if s[i].isupper():
                    return end, False
            return end, False
        def checkLower(p, start, end, s):
            cnt = 0
            for i in range(start, end):
                if s[i].isupper():
                    return end, False
                if s[i] == p[cnt]:
                    cnt += 1
                    if cnt == len(p):
                        return i + 1, True
            return end, False
        def findNextUpper(pattern, start, end):
            sub_pattern = list()
            for j in range(start, end):
                if pattern[j].isupper():
                    return j, sub_pattern
                sub_pattern.append(pattern[j])
            return end, sub_pattern
        
        ans, l = list(), len(pattern)
        for query in queries:
            flag, n = True, len(query) # flag indicate whether the query is valid or not, any violation will make it to False
            pq, pp = 0, 0 # pointer of pattern, pointer of query
            while pp < l:
                char = pattern[pp]
                if char.isupper():
                    pq, f = checkUpper(char, pq, n, query) # find the first upper letter matches char and without any other upper letter in the path
                    if pq == n and not f: # pq = n may be either violation or correction but at index n, use f to check it
                        flag = False
                        break   
                    pp += 1
                else:
                    pp, sub_pattern = findNextUpper(pattern, pp, l)
                    if not sub_pattern: continue # between two upper letters might have no lower letter 
                    pq, f = checkLower(sub_pattern, pq, n, query)
                    if pq == n and not f:
                        flag = False
                        break
            if pp != l: # query out of range but pattern still have some elements
                flag = False
            if flag and pq < n - 1: # check no uppercase suffix appear in the last part of query
                for pq in range(pq, n):
                    if query[pq].isupper():
                        flag = False
                        break
            ans.append(False) if not flag else ans.append(True)
        return ans