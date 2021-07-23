# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:59:42 2021

@author: Brian Hu
"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(ptr):
            if not ptr.left and not ptr.right:
                self.dp[ptr] = ptr.val
                self.max = max(self.max, self.dp[ptr])
                return self.dp[ptr]
            
            res = [ptr.val]
            for next_ptr in [ptr.left, ptr.right]:
                if next_ptr:
                    dfs(next_ptr)
                    res.append(self.dp[next_ptr])
            # since the upper layer can only choose path to either ptr.left or ptr.right, 
            # self.dp is optimized by the concept
            self.dp[ptr] = max(res[0], sum(res)) if len(res) == 2 else \
                            max(res[0], res[0] + res[1], res[0] + res[2])
            # if global max is not pass the root, we need to consider 
            # this situation and add sum(res) to check it
            self.max = max(self.max, self.dp[ptr], sum(res))
            return self.dp[ptr]
        
        self.max, self.dp = float('-inf'), dict()
        dfs(root)
        return self.max