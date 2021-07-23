# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:26:47 2021

@author: Brian Hu
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(ptr):
            flag = False
            if len(self.stack) >= 1 and ptr.val >= self.stack[-1]: # hold a increasing stack to check the current node value is the largest in the path 
                flag = True
                self.count += 1
                self.stack.append(ptr.val)
            for next_ptr in [ptr.left, ptr.right]:
                if next_ptr:
                    dfs(next_ptr)
            if flag: # if we put the current node value in stack, we need to pop it before back to its root
                self.stack.pop()
                    
        self.count, self.stack = 0, [root.val]
        dfs(root)
        return self.count