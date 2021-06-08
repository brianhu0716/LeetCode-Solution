# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:49:44 2021

@author: Brian
"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l,ans = len(nums),0
        for lp in range(l): # 確定左指標位置
            n1 = nums[lp]
            rp = lp + 2 # 右指標初始化為左指標+ 2的位置(中間有一個中指標)
            for mp in range(lp + 1,l): # 中指標由左指標加1開始往右移動
                rp = max(rp,mp + 1) # 保證右指標至少要大於中指標1個位置
                n2 = nums[mp]
                while rp <= l:
                    if rp == l: # 已經到底(當前中指標的位置到l - 1都可以組成三角形)，更新完後直接break
                        ans += rp - 1 - (mp + 1) + 1 # 計算三角形數的方式：尾：rp - 1,頭：mp + 1,頭尾都要算： + 1
                        break 
                    if n1 + n2 <= nums[rp]: 
                        ans += rp - 1 - (mp + 1) + 1         
                        break
                    else:
                        rp += 1
        return ans   