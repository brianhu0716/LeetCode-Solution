# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:50:42 2021

@author: Brian Hu
"""
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dq = deque([(entrance[0], entrance[1])])
        level = 0
        seen, m, n = set(), len(maze), len(maze[0])
        while dq:
            res = set()
            for _ in range(len(dq)):
                x, y = dq.popleft()
                if [x, y] != entrance and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                    return level
                seen.add((x, y))
                for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (0 <= i < m) and (0 <= j < n) and (i, j) not in seen and maze[i][j] != '+':
                        res.add((i, j))
            dq = deque(list(res))
            level += 1
        return -1