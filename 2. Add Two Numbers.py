# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:33:21 2021

@author: Brian
"""

class Node():
    def __init__(self,data):
        self.val = data
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1,ptr2 = l1,l2
        q_before = 0
        while ptr1 and ptr2 :
            summation = q_before + ptr1.val + ptr2.val
            ptr1.val = summation % 10
            q_before = summation // 10
            if ptr1.next == None or ptr2.next == None: break
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if not ptr1.next and not ptr2.next: 
            if q_before == 0: return l1
            ptr1.next = Node(q_before)
            return l1
        if not ptr1.next:
            if q_before == 0: 
                ptr1.next = ptr2.next
                return l1
            else:
                ptr2 =ptr2.next
                ptr3 = ptr2
                while q_before > 0 and ptr3:
                    summation = q_before + ptr3.val
                    ptr3.val = summation % 10
                    q_before = summation // 10
                    if ptr3.next == None: break
                    ptr3 = ptr3.next
                if q_before == 0:
                    ptr1.next = ptr2
                    return l1
                if ptr3.next == None: # q_before已經不為0
                    ptr3.next = Node(q_before)
                    ptr1.next = ptr2
                    return l1
        if not ptr2.next:
            if q_before == 0: return l1
            ptr1 = ptr1.next
            ptr3 = ptr1
            while q_before > 0 and ptr3:
                summation = q_before + ptr3.val
                ptr3.val = summation % 10
                q_before = summation // 10
                if ptr3.next == None: break
                ptr3 = ptr3.next
            if q_before == 0: return l1
            if ptr3.next == None: # q_before已經不為0
                ptr3.next = Node(q_before) 
                return l1