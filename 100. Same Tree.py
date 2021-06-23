# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:24:57 2021

@author: Brian Hu
"""

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(ptr1, ptr2):
            #print(ptr1,ptr2)
            # check whether the nodes with same structure share the same value or not 
            if ptr1.val != ptr2.val:
                self.same = False
                return
            # check whether the structure of the two trees are same 
            for next_ptr1, next_ptr2 in [[ptr1.left, ptr2.left], [ptr1.right, ptr2.right]]:
                if not self.same or (not next_ptr1 and not next_ptr2):
                    continue
                if next_ptr1 and next_ptr2:
                    dfs(next_ptr1,next_ptr2)
                else:
                    self.same = False
                    return
        self.same = True
        if p and q:
            dfs(p, q)
            return self.same
        elif not p and not q:
            return self.same
        else:
            return False