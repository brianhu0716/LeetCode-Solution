# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:37:03 2021

@author: Brian Hu
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr = l1
        n1 = ""
        while ptr:
            n1 += str(ptr.val)
            ptr = ptr.next
        ptr = l2
        n2 = ""
        while ptr:
            n2 += str(ptr.val)
            ptr = ptr.next
        
        n = str(int(n1) + int(n2))
        head = ListNode(int(n[0]))
        ptr = head
        for i in range(1,len(n)):
            ptr.next = ListNode(int(n[i]))
            ptr = ptr.next
        return head