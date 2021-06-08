# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:47:53 2021

@author: Brian
"""
'''
moved_node代表即將要被移動的node
ptr為其實一直都是最早的head，我們只是把它的next指派為即將移動的node(moved_node)的next，接著把moved_node的next接到head，最後再
把moved_node定為head即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr and ptr.next:
            moved_node = ptr.next
            ptr.next = moved_node.next
            moved_node.next = head
            head = moved_node
        return head