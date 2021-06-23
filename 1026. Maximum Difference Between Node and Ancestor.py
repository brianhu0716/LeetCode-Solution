# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:11:46 2021

@author: Brian Hu
"""
'''
(a) my idea is treat the current ptr.val as ancestor then use dfs to collect the maxima value and minima value of its children.
(b) we update the max absolute difference seen from ancestor
(c) because the current ancestor will be the previous node's children, 
so we need to check whether the current node value is out of bound(maxima value and minima value of its children), 
if so, we need to update them
'''
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(ptr):
            if not ptr.left and not ptr.right: # no children under leaf
                return []
            ancestor = ptr.val
            children = list()
            for next_ptr in (ptr.left, ptr.right): # we collect a list contains maxima value of children and min value of children
                if next_ptr:
                    if not (r := dfs(next_ptr)): # add leaf value
                        children += [next_ptr.val]
                    else: 
                        children += r
            children = set(children) # avoid repeated value
            children_max, children_min = max(children), min(children) # pick out maxima and minima of children
            self.max = max(self.max, abs(ancestor - children_max), abs(ancestor - children_min))
            if ancestor > children_max: # update the maxima if it is necessary
                children_max = ancestor
            elif ancestor < children_min: # update the minima if it is necessary
                children_min = ancestor
            return [children_max, children_min]
    
        self.max = 0
        dfs(root)
        return self.max