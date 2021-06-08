# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:24:18 2021

@author: brian.hu
"""
"""目標：搜尋二元樹中給定兩指定node的最近共同祖先
解法為當沒有找到任何答案時，我們要把路徑中所有走過的節點都標記為"*"，以方便之後回朔時找到最近
共同祖先，當找到一組解後，之後的遍歷就不再對node做標記，等到找到2個答案後，停止繼續dfs
開始往回找"第一個"被標記為"*"的node即為lca(須注意必須加上lca不存在的情況下才做更新，否則
答案會回溯到root)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(ptr) :
            if self.cnt == 0  : 
                temp = ptr.val
                ptr.val = "*"
                #print(ptr,temp)
            if ptr == p or ptr == q : 
                self.cnt += 1
                if self.cnt == 2 : return 

            for next_ptr in [ptr.left,ptr.right] :
                if self.cnt < 2 and next_ptr :
                    dfs(next_ptr)
            #print("back",ptr,self.cnt)
            if ptr.val == "*" and self.cnt == 2 and not self.lca :
                ptr.val = temp
                self.lca = ptr
        
        self.lca = None
        self.cnt = 0   
        
        dfs(root)
        
        return self.lca 