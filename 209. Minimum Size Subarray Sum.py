# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 01:20:38 2021

@author: Brian
"""
'''
本題要找連續子字串相加後大於等於target的最短長度,思路如下：
(a) 給定雙指標，右指標先移動向右探索未知區域，當當前累積總和(res)大於target時,計算總長度(rp - lp + 1)，接著移動左指標向右，\
    每移動一次，就將其通過的值由當前累積總合中扣除，並檢視當前子序列總和是否還是大於target，若是則既須更新長度，若否則跳出迴圈\
    繼續移動右指標
(b) 重複以上過程值到右指標碰到邊界為止，最後若ans的長度是預設值(inf)，代表整個序列加總都無法滿則要求，最短長度為0
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp,res,ans = 0,0,float('inf')
        for rp in range(len(nums)):
            res += nums[rp]
            while res >= target:
                ans = min(ans,rp - lp + 1)
                res -= nums[lp]
                lp += 1
                
            '''
            if res >= target:
                ans = min(ans,rp - lp + 1)
                while True:
                    res -= nums[lp]
                    lp += 1
                    if res >= target:
                        ans = min(ans,rp - lp + 1)
                    else:
                        break
            '''
        return ans if ans != float('inf') else 0