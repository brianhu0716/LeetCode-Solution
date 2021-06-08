# -*- coding: utf-8 -*-
"""
Created on Thu May  6 18:51:13 2021

@author: Brian
"""

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def checkSimilar(ref,test):
            diff = []
            for i in range(len(ref)):
                if ref[i] != test[i]:
                    diff.append(i)
                    if len(diff) > 2: return False
            
            test[diff[0]],test[diff[1]] = test[diff[1]],test[diff[0]]
            return test == ref
        
        def dfs(same_group):
            
            for ref in same_group: # we continue expand same_group size until none of string in self.strs is similar to strings in same_groups
                idx = 0
                while idx < len(self.strs):
                    if ref == self.strs[idx] or checkSimilar(list(ref),list(self.strs[idx])): # same or similar
                        same_group.append(self.strs.pop(idx))
                    else:
                        idx += 1
            return same_group
        
        self.strs = strs[:]
        groups = list()
        while self.strs: # continue searching similar until all string are clustered
            groups.append(dfs([self.strs.pop()]))
        
        return len(groups)