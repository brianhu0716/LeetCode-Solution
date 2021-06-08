# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:47:02 2021

@author: brian.hu
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = [(i,nums[i]) for i in range(len(nums))]
        
        stack,ans = list(),[-1 for _ in nums]
        global_max = float('-inf')
        for idx,val in nums :
            global_max = max(global_max,val)
            #print(val,stack,ans)
            # 維護遞減堆疊結構，遇到比stack[-1]大的值就pop，表示找到最近且比當前大的值
            while stack and stack[-1][1] < val : 
                ans[stack.pop()[0]] = val # 將答案填入正確的位置
            stack.append((idx,val))
            #print(val,stack,ans)
            
        # circular loop    
        for idx,val in nums :
            if not stack : break
            elif stack[-1][1] == global_max : # 遇到全域最大值，直接忽略(沒人比他大)
                while stack and stack[-1][1] == global_max :
                    stack.pop()
                
            while stack and stack[-1][1] < val : # 找到最近且比當前大的值
                ans[stack.pop()[0]] = val # 將答案填入正確的位置
                
        return ans