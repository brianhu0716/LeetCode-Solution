# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:27:43 2021

@author: Brian Hu
"""

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.d1, self.d2 = dict(), dict()
        self.nums2 = nums2
        for num in nums1:
            self.d1[num] = self.d1.get(num,0) + 1
        for num in nums2:
            self.d2[num] = self.d2.get(num,0) + 1

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        new = old + val
        self.d2[old] -= 1
        self.nums2[index] = new 
        self.d2[new] = self.d2.get(new,0) + 1

    def count(self, tot: int) -> int:
        ans = 0
        for n in sorted(self.d1.keys()):
            if n >= tot :  # it means we need a zero or negative value to make nums1[i] + nums2[j] == tot happen, but all element in nums1 and nums2 are garenteed to be positive, so we can stop search here 
                break
            if n in self.d1 and (tot - n) in self.d2:
                ans += self.d1[n] * self.d2[tot - n]
        return ans