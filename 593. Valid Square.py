#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:54:57 2021

@author: brian
"""
"""
a) find s11,s13,s14(p1-p2,p1-p3,p1-p4),if its a valid square, there must be tow 
    of them are equal,whicj means we find a vertex p1 and its two neighbors,
b) then we check whether the two diagonals are equal, if so its a valid square
c) if any of s12,s13,s14 is 0, return False
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:        
        f = lambda x,y : sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) 
        s12,s13,s14 = f(p1,p2),f(p1,p3),f(p1,p4)
        
        if s12 == 0 or s13 == 0 or s14 == 0 : return False 
        
        if s12 == s13 :
            if f(p2,p4) == f(p3,p4) == s12 and s14 == f(p2,p3) : return True
            return False
        elif s12 == s14 :
            if f(p2,p3) == f(p3,p4) == s12 and s13 == f(p2,p4) : return True
            return False       
        elif s13 == s14 :
            if f(p2,p4) == f(p3,p2) == s13 and s12 == f(p4,p3) : return True
            return False
        return False
        