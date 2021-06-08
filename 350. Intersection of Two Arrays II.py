# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:14:02 2021

@author: -
"""

class Solution:
    def intersect(self, nums1, nums2):
        d1 ,d2 = {},{}
        for n1 in nums1:
            if n1 not in d1.keys():
                d1[n1] = 1
            else:
                d1[n1] += 1
        for n2 in nums2:
            if n2 not in d2.keys():
                d2[n2] = 1
            else:
                d2[n2] += 1
        result = []
        if len(d1.keys()) >= len(d2.keys()):
            for n2 in d2.keys():
                if n2 not in d1.keys():
                    continue
                else:
                    result += [n2] * min(d1[n2],d2[n2])                       
        else:
            for n1 in d1.keys():
                if n1 not in d2.keys():
                    continue
                else:
                    result += [n1] * min(d1[n1],d2[n1])
        return result

test = Solution()
nums1 = [[1,2,2,1],
         [4,9,5]]
nums2 = [[2,2],
         [9,4,9,8,4]]
for i in range(len(nums1)):
    print(test.intersect(nums1[i],nums2[i]))