# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:58:02 2021

@author: Brian
"""

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = list()
        ptr = head
        while ptr :
            node.append(ptr)
            if ptr.next == None : break
            ptr = ptr.next
        if (l := len(node)) == 0 : return head
        k = k % l 
        if k == 0: return head
        new_head = node[-k] # 新的head
        new_head.tail = ptr # 將原Linked_list中的最後一個node的指標指向新的head的尾部
        node[-k - 1].next = None # 將原head中的斷點打掉
        new_head.tail.next = head # 新的頭部尾端指標指向被打斷後的原head
        
        return new_head