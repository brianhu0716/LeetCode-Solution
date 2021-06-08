# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:51:28 2021

@author: brian.hu
"""
"""
目的：將深度相同的node指向下一個深度與她相同的node
做法：
(a) 首先我們建立一個字典，key為深度值，對應的value為上一個具有該深度的指標
(b) 利用dfs由左到右逐一搜索node，
    (b.1) 如果該node的深度已經在key中，則將value的指標的next指向當前的node
    (b.2) 如果該node的深度不在key中，則將value設為當前的node
    將value中當ptr設定為當前的node
(c) 結束dfs後，我們遍歷一次字典的所有深度值，並將value中的指標的next指向None後即為答案
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def Update(ptr_now,depth):
            if depth in self.table : 
                self.table[depth].next = ptr_now
            else:
                self.table[depth] = ptr_now
            self.table[depth] = ptr_now
            return
        
        def dfs(ptr,depth):
            if not ptr.left and not ptr.right :
                Update(ptr,depth)
                return 
            
            Update(ptr,depth) 
            depth += 1
            for next_ptr in [ptr.left,ptr.right]:
                if next_ptr:
                    dfs(next_ptr,depth)
            depth -= 1
            
        self.table = dict()  
        if not root : return None
        dfs(root,0)
        
        for depth in self.table.keys():
            self.table[depth].next = None
        return root