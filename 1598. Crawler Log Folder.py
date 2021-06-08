# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:38:40 2021

@author: Brian
"""
'''
看到"../"代表移到上一層資料夾，lalyer要減1(如果layer已經是0代表已經在最上層，不能再減，維持原樣即可)
看到"./"代表保持原layer，pass即可
看到"x/"代表移到下一層名為x的子資料夾，無論是甚麼layer + 1即可
遍歷完logs後，只要layer還是0，需要任何動作就在最上層，return 0，要是layer為N(N為正整數)，代表需要N次"../"操作才可以回到最上層
return layer即可
'''
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        layer = 0
        for log in logs:
            if log == "../" :
                (layer := layer - 1) if layer != 0 else layer
            elif log == "./" :
                continue
            else:
                layer += 1
        return 0 if layer == 0 else layer