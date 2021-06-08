# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:09:05 2021

@author: Brian
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort_sub_array(left_list,right_list):
            lp,rp = 0,0
            #print(left_list)
            #print(right_list)
            l_left = len(left_list)
            l_right = len(right_list)
            merge = list()
            while lp < l_left and rp < l_right:
                if left_list[lp] < right_list[rp]:
                    merge.append(left_list[lp])
                    lp += 1
                else:
                    merge.append(right_list[rp])
                    rp += 1
            merge.extend(left_list[lp:])
            merge.extend(right_list[rp:])
            #print("merge",merge)
            return merge
        
        if len(nums) == 1 : return nums
        ret = []
        while len(ret) != 1:
            if not ret:
                for i in range(0,len(nums),2):
                    if i == len(nums) - 1: # 奇數個
                        ret.append([nums[i]])
                        break
                    else:
                        ret.append(sort_sub_array([nums[i]],[nums[i + 1]]))
                #print("next round",ret)
            else:
                res = list()
                for i in range(0,len(ret),2):
                    if i == len(ret) - 1: 
                        res.append(ret[i])
                        continue # 奇數個
                    res.append(sort_sub_array(ret[i],ret[i + 1]))
                ret = res
        return ret[0]