# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:48:12 2021

@author: Brian Hu
"""
'''
row and col are two dictionaries with each key is index of row and col and values are the number showing in the corresponding row and col. 
we continue checking the block(3 * 3) to verify whether the value have already existed in the row, col, or block before. 
If so, we return False, else True
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def SearchBlock(i, j, row,col):
            block = set()
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    if board[m][n] == ".":
                        continue
                    if (board[m][n] in block) or (board[m][n] in col[n]) or (board[m][n] in row[m]):
                        return False
                    block.add(board[m][n])
                    col[n].append(board[m][n])
                    row[m].append(board[m][n])
            return True
                    
        row, col = collections.defaultdict(list), collections.defaultdict(list)
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not SearchBlock(i, j, row, col):
                    return False
        
        return True