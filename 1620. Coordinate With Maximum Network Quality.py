# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:40:20 2021

@author: Brian
"""
'''
暴力解，直接在50 * 50的range內搜索每個整數座標能收到訊號的值，最後回傳品質最好的座標即可
'''
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:        
        cord = [float('inf'),float('inf')]
        max_quality = float('-inf')
        for x in range(51):
            for y in range(51):
                res = 0
                for xi,yi,qi in towers:
                    if (dist := sqrt((x - xi) ** 2 + (y - yi) ** 2)) <= radius:
                        res += qi // (1 + dist)
                if res > max_quality: 
                    max_quality = res
                    cord = [x,y]
        return cord
                    