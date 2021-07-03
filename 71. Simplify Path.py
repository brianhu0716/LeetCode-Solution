# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:35:55 2021

@author: Brian Hu
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        def findFolder(start, end, path):
            for i in range(start, end):
                if path[i] == '/':
                    return i
            return end
        stack = list()
        i, n = 0, len(path)
        while i < n:
            if path[i] =='.':
                i_next = findFolder(i, n, path)
                if path[i: i_next] == '..': # back to previous folder
                    if stack:
                        stack.pop()
                    i += 2
                elif path[i: i_next] == '.': # no changes
                    i += 1
                else: # ..., ..xxx is treated as folder
                    stack.append(path[i: i_next])
                    i = i_next
            elif path[i].isalpha():
                stack.append(path[i: (i_next := findFolder(i, n, path))])
                i = i_next
            elif path[i] == '/': # no changes
                i += 1
        if not stack:
            return '/'
        ans = '/'
        for dir in stack: # rebuild the simplify path from original form
            ans += dir + '/'
        return ans[: -1] 