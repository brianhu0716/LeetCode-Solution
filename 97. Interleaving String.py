# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:49:33 2021

@author: Brian
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def helper(p1,p2,p3,s1,s2,s3): 
            if (p1,p2,p3) in self.d.keys(): return self.d[(p1,p2,p3)]
            if p3 == len(s3) : 
                if p1 == len(s1) and p2 == len(s2) - 1 or p1 == len(s1) - 1 and p2 == len(s2): 
                    return True
                return False
            
            if p1 == len(s1) : 
                if s2[p2 : ] == s3[p3 : ] : return True
                return False
            
            if p2 == len(s2):
                if s1[p1 : ] == s3[p3 : ] : return True
                return False
            
            if s1[p1] != s3[p3] and s2[p2] != s3[p3] : return False
            
            if s1[p1] == s3[p3] and s2[p2] == s3[p3]:
                ans = helper(p1 + 1,p2,p3 + 1,s1,s2,s3) | helper(p1,p2 + 1,p3 + 1,s1,s2,s3) 
                
            elif s1[p1] == s3[p3] :   
                ans = helper(p1 + 1,p2,p3 + 1,s1,s2,s3)
                
            elif s2[p2] == s3[p3] :
                ans = helper(p1, p2 + 1,p3 + 1,s1,s2,s3) 
            
            self.d[(p1,p2,p3)] = ans
            
            return ans
            
        if len(s1) + len(s2) != len(s3) : return False
        
        if s3 == "" : return True
        
        self.d = dict()
        
        ans = helper(0,0,0,s1,s2,s3)
        self.d[(0,0,0)] = ans 
        
        if self.d[(0,0,0)] == True : return True
        
        return False