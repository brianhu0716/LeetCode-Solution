# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 21:43:57 2021

@author: Brian Hu
"""

"""
preorder traversal:
we need to touch the leaf first, then go back step by step to check
whether the next_node(ptr.left or ptr.right) is in delete list. If so,
we can break the connection between next_ptr and ptr then add two children of 
next_ptr in ans list. Until we finish the preorder trversal process, we just 
need to check whether the head is in delete list, if it isn't, we can add head 
in the ans list, else, we will add head.left and head.right to ans if they exist
每次都先退兩格，然後檢查下一個是否在delete list 中，若真，則我們把next_ptr(ptr.left or ptr.right)
斷開，在把next_ptr.left or next_ptr.right 加入答案中  
"""
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root : return root # special case
        def dfs(ptr, to_delete):
            if not ptr.left and not ptr.right:
                return
            if ptr.left: # to bottom left
                dfs(ptr.left, to_delete)
                if ptr.left.val in to_delete:
                    if ptr.left.left: # add the left children to answer if it exists
                        self.ans.append(ptr.left.left)
                    if ptr.left.right: # add the right children to answer if it exists
                        self.ans.append(ptr.left.right)
                    ptr.left = None # cut the node whose value is in to_delete 
            if ptr.right:
                dfs(ptr.right, to_delete)
                if ptr.right.val in to_delete:
                    if ptr.right.left: # add the left children to answer if it exists
                        self.ans.append(ptr.right.left) 
                    if ptr.right.right: # add the right children to answer if it exists****
                        self.ans.append(ptr.right.right)
                    ptr.right = None  # cut the node whose value is in to_delete
        self.ans = list()
        dfs(root, to_delete)
        if root.val not in to_delete: # check whether the root value is in to_delete ot not  
            self.ans.append(root)
        else:
            if root.left:
                self.ans.append(root.left)
            if root.right:
                self.ans.append(root.right)
        return self.ans