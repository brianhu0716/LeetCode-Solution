# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:32:48 2021

@author: brian.hu
"""

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """		

        self.prev = TreeNode(float('-inf'))
        self.nodes = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if root.val < self.prev.val:
                self.nodes += [self.prev,root]
            self.prev = root
            inorder(root.right)
        
        inorder(root)
        self.nodes[0].val, self.nodes[-1].val = self.nodes[-1].val, self.nodes[0].val
        return root