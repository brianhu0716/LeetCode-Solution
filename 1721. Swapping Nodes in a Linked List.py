# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:23:05 2021

@author: Brian
"""
'''
把把由前往後數第k個node的值與由後往前署第k個node值交換即可
'''
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node = list()
        ptr = head
        while ptr:
            node.append(ptr)
            if ptr.next ==None : break
            ptr = ptr.next
        node[k - 1].val,node[-k].val = node[-k].val,node[k - 1].val # 由前往後數的起始index為1，所以list index要減1才是對的位置
        return head