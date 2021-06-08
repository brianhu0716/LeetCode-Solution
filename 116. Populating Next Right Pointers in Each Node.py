# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:00:01 2021

@author: brian.hu
"""
"""
本題與第117題相同
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