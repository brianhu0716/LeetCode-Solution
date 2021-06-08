# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:12:10 2021

@author: Brian
"""
class Node():
    def __init__(self,val):
        self.data = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            else:
                current = current.next
                i += 1
        return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        return 
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        return 
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        node = Node(val)
        current = self.head
        i = 0
        while current:
            if i == index - 1:
                node.next = current.next
                current.next = node
                if not node.next : # 當前是尾部
                    self.tail = node
                return 
            else:
                i += 1
                current = current.next
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            if self.head:
                self.head = self.head.next
                return 
            return
        i = 0
        current = self.head
        while current:
            if i == index - 1:
                if not current.next: # 代表當前是尾部，index已經超出邊界
                    return 
                current.next = current.next.next
                if not current.next: # 代表更新後當前是尾部
                    self.tail = current
                return 
            else:
                current = current.next
                i += 1
        return 
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
[[],[0,10],[0,20],[1,30],[0]]
["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]