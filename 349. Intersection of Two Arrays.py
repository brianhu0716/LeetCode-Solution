# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:23:03 2021

@author: -
"""
'''
解題思路與350雷同
'''
class Solution:
    def intersection(self, nums1, nums2):
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
                    result += [n2]                      
        else:
            for n1 in d1.keys():
                if n1 not in d2.keys():
                    continue
                else:
                    result += [n1]
        return result