# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:39:06 2021

@author: Brian
"""
'''
兩個連結串列比大小後形成一個新的連結串列，解法如下：
(a)每次都只比當下兩個連結串列的值，把小的值形成一個新的Node存入list(node)中，並移動較小值的指標到下一個位置進行下一輪比較，
    直到有一個連結串列的指標指到None為止，接者把剩餘的另一個連結串列中剩餘的所有連結放入list的尾端，結束第一部分
(b) 接著我們遍歷list，把前一個next的指標指向後一個node[i]完成後即形成由小到大排序的連結串列
'''
class Node():
    def __init__(self,data):
        self.val = data
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1,ptr2 = l1,l2
        node = list()
        while ptr1 and ptr2:
            if ptr1.val > ptr2.val:
                node.append(Node(ptr2.val))
                ptr2 = ptr2.next
            elif ptr1.val < ptr2.val:
                node.append(Node(ptr1.val))
                ptr1 = ptr1.next
            else:
                node += [Node(ptr2.val),Node(ptr1.val)]
                ptr2 = ptr2.next
                ptr1 = ptr1.next
        node.append(ptr1) if not ptr2 else node.append(ptr2)
        head = node[0]            
        ptr = head
        for i in range(1,len(node)):
            ptr.next = node[i]
            ptr = ptr.next
        return head