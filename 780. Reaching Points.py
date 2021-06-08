# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:49:22 2021

@author: Brian
"""

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def helper(sx,sy,tx,ty):
            if sx == tx and sy == ty: return True
            
            elif sx == tx and ty - sy > 0:
                return True if (ty - sy) % sx == 0 else False
            
            elif sy == ty and tx - sx > 0:
                return True if (tx - sx) % sy == 0 else False
            
            elif sx > tx or sy > ty : return False
            
            if tx > ty : 
                return helper(sx,sy,tx - ty,ty)
            elif ty > tx : 
                return helper(sx,sy,tx,ty - tx)
            else : 
                return helper(sx,sy,tx,ty - tx) | helper(sx,sy,tx - ty,ty)
            
        return helper(sx,sy,tx,ty)
'''

9
5
12
8
1
1
3
5
1
1
2
2
1
1
1
1
35
13
455955547
420098884
1
1
1000000000
1
'''
