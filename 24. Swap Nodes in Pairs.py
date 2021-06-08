# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:06:14 2021

@author: Brian
"""

'''
交換相鄰兩node的值即可
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        while not head or not head.next : return head
        ptr = head
        while ptr and ptr.next:
            temp = ptr.val
            ptr.val = ptr.next.val
            ptr.next.val = temp
            ptr = ptr.next.next
        return head