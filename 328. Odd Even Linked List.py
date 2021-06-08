# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:50:08 2021

@author: Brian
"""
'''
解題思路：
設定兩個Linked_list，其中一個由head開始，另一個由head.next開始，如此一來每做一輪這兩個串列都往前推進兩格，使得由head開始的
連結串列永遠都保持奇數位置的值，而由head.next開始的連結串列永遠都保持偶數位置的值最後在把奇數位置的尾部的指標指向偶數位置即可
*** 這裡可能會有深拷貝的問題存在，如果不用深拷貝的話，迴圈內先移ptr2會導致答案有誤，如果要先移ptr2的話必須引進深拷貝
    在實作時，如果由同一個head切不同串列，更改值的時候一定要從最接近原本head頭部的串列開始改
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd,even = head,head.next
        ptr1,ptr2 = odd,even

        while (ptr1 != None and ptr1.next != None) and (ptr2 != None and ptr2.next != None): 
            ptr1.next = ptr1.next.next
            ptr1 = ptr1.next
            
            ptr2.next = ptr2.next.next
            ptr2 = ptr2.next
        ptr1.next = even
        return odd
'''深拷貝版本
import copy
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd,even = copy.deepcopy(head),copy.deepcopy(head.next)
        ptr1,ptr2 = odd,even

        while (ptr1 != None and ptr1.next != None) and (ptr2 != None and ptr2.next != None): 
            ptr2.next = ptr2.next.next
            ptr2 = ptr2.next
            
            ptr1.next = ptr1.next.next
            ptr1 = ptr1.next

        ptr1.next = even
        return odd