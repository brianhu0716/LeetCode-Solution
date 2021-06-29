# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:49:53 2021

@author: Brian Hu
"""
'''
just using binary search
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = list()
        self.length = 0
    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            self.length += 1
            return 
        i, j = 0, self.length - 1
        while i <= j:
            mid = (i + j) // 2
            if self.arr[mid] < num:
                i = mid + 1
            elif self.arr[mid] > num:
                j = mid - 1
            else:
                self.arr.insert(mid, num)
                self.length += 1
                return
        self.arr.insert(i, num)
        self.length += 1
    def findMedian(self) -> float:
        mid = self.length // 2
        if self.length % 2 == 0:
            return (self.arr[mid] + self.arr[mid - 1]) / 2
        return self.arr[mid]
