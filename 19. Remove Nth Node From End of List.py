# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 00:42:59 2021

@author: Brian
"""
'''
刪除由末尾數過來地n個節點的方式：
將各指標指到的當前節點存到list中，由於要刪除第-n個，因此我們將第-n - 1個節點的next指到-n + 1即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l,node = 0,list()
        while head:
            l += 1
            node.append(head)
            head = head.next
        if n == l:
            node = node[1:]
        elif n == 1:
            node[-n - 1].next = None
        else:
            node[-n - 1].next = node[-n + 1]

        return node[0] if node else None