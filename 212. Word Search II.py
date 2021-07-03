# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:08:37 2021

@author: Brian Hu
"""
import collections
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(idx,target,x,y,seen) :
            if idx == len(target):
                self.find = True
                self.ans += [target]
                return 
            
            seen[x][y] = True
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]] :
                next_x, next_y = x + dx, y + dy
                if not (0 <= next_x < m) or not (0 <= next_y < n) or self.find : continue
                if not seen[next_x][next_y] and board[next_x][next_y] == target[idx] :
                    dfs(idx + 1,target,next_x,next_y,seen)
            seen[x][y] = False
        letter = set()
        for row in board:
            for s in row:
                letter.add(s)
        
        d = collections.defaultdict(set)
        for word in words:
            if len(set(word) - letter) == 0: # if word has some letters didn't show up in board, we don't need to waste time to search it
                d[word[0]].add(word)
        
        m,n = map(len, (board,board[0]))
        self.ans = list()
        for x in range(m) :
            for y in range(n) :
                if (prefix := board[x][y]) in d.keys():
                    found = list()
                    for target in d[prefix] :
                        self.find = False
                        dfs(1,target,x,y,[[False for _ in range(n)] for _ in range(m)])
                        if self.find : found.append(target)
                    for rmv in found :
                        d[prefix].remove(rmv)
        return self.ans