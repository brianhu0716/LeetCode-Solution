# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:21:23 2021

@author: brian.hu
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def checkValid(row,col,res):
            """
            有效的位置：不能與任一存在的位置同行、同列、同對角線
            """
            for place in res:
                x,y = place[0],place[1]
                if x == row or y == col or abs(x - row) == abs(y - col):
                    return False
            return True
        
        def dfs(row,res):
            if row == n: # 更新答案
                for x,y in res: # 每一個row都只會有一組座標
                    board = ""
                    for _ in range(n): 
                        if _ == y:# 找出當前row被放置皇后的位置
                            board += "Q"
                        else:
                            board += "."
                    #print(board,self.ans)
                    self.ans[-1].append(board)
                self.ans.append([])
                return 
            
            for col in range(n):
                # 確認當前row放置皇后的位置有效後，再找row + 1列的有效位置
                if checkValid(row,col,res): 
                    dfs(row + 1,res + [(row,col)])
                    
            return         
            
        self.ans = [[]]
        #print(self.ans)
        dfs(0,list())
        return self.ans[:-1]
        
        
            